# 課程內容 QA 系統 — 設計文件

- **日期**：2026-06-09
- **方案**：A（Vision-first RAG，全雲端 OpenAI）
- **狀態**：設計已確認，待轉實作計畫

---

## 1. 目標與範圍

針對固定的課程投影片內容，讀入一個 CSV 問題檔，對每題填入**簡短且精確**的答案，輸出同格式 CSV。

- **語料**：`docs/slides/` 下 12 份課程投影片 PDF（共約 31MB，多為圖表/示意圖），內容**固定不變**。
- **輸入 CSV**：無 header、2 欄。第 1 欄為問題（中文、英文或中英夾雜），第 2 欄為空。
- **輸出 CSV**：同格式，將第 2 欄填入答案。
- **使用情境**：離線批次評測，一次跑一個 CSV。索引可離線預先建好並永久快取。

### 評分與最佳化目標

- **語意正確（80%）**：人工閱卷或 LLM-as-judge。最高優先。
- **效率/簡潔（20%）**：程式執行效率、回覆速度、答案不冗長。沒有嚴格門檻，「不要慢到誇張」即可。
  - **計時範圍只含「CSV 進來 → 答案填完」的查詢階段**；vision 解析投影片（離線建索引）**不計時**。

### 答案風格

- 簡短、精確，不過度解釋。
- 語言預設**跟隨問題語言**，專有名詞（如 transformer）保留原文。
- 找不到依據時回簡短的「資料不足」，不硬掰。

---

## 2. 模型堆疊（2026-06 當下最強，雲端限 OpenAI）

| 環節 | 模型 | 說明 |
|---|---|---|
| 投影片解析（vision） | **GPT-5.5** | OpenAI 最新旗艦，文件/視覺理解最佳；解析離線一次性、不計時，用最貴最仔細的做法 |
| 語意切塊（chunking） | **GPT-5.5** | LLM 依主題判斷邊界 |
| 答案生成（QA） | **GPT-5.5** | 最吃重 80% 語意分；低 temperature 求穩定 |
| Embedding | **text-embedding-3-large** | OpenAI 最強嵌入模型（無後繼）；3072 維 |
| Rerank | **GPT-5.5 listwise** | OpenAI 無專用 reranker；用 GPT listwise 留在雲端、免本地重依賴 |

> 註：市場上 retrieval 品質更高者為 Voyage `voyage-3-large`、rerank 最強者為本地 `bge-reranker-v2.5-gemma2-lightweight`，但均非 OpenAI 且需本地重依賴；依「雲端只用 OpenAI、避免本地重模型」的限制，採上表選擇。

---

## 3. 整體架構

兩個階段：**A. 離線建索引（一次性，快取重用）** 與 **B. 線上查詢（跑 CSV，計時）**。

```
[12 PDFs] ──render──> [每頁圖] ──GPT-5.5 vision──> [每頁 markdown]
                                                        │
                                          LLM 語意切塊（GPT-5.5）
                                                        ▼
                                          [語意 chunks + 內部 metadata]
                              ┌─────────────────────────┴─────────────────┐
                              ▼                                            ▼
                    [text-embedding-3-large]                       [jieba/BM25 稀疏索引]
                              ▼                                            ▼
                       [dense 向量 / FAISS]                          (一起存成磁碟快取)
                              └──────────────────┬─────────────────────────┘
                                                 ▼
[CSV 問題] ─> 混合檢索(dense+BM25, RRF) ─> GPT-5.5 listwise rerank ─> GPT-5.5 生成 ─> [填入 CSV]
```

### 核心設計決定

- **語意切塊（非依實體頁）**：輸出不需標來源頁碼，chunk 以語意連貫為單位。相關連續頁合併、單頁多主題拆開。目標長度約 200–500 tokens、上限 ~800。
- **vision 解析仍逐頁**：那是 GPT-5.5 看圖的單位；語意切塊是解析後的獨立後處理步驟。
- **metadata 簡化**：只保留內部 `chunk_id`、`deck`（供除錯），不會出現在答案中。生成 prompt 不做來源標註。
- **索引存磁碟快取**：語料小且固定，dense 用 FAISS flat（精確、免重型 DB），稀疏用 BM25。
- **全雲端 OpenAI**：vision、chunking、embedding、rerank、生成皆走 API，零本地重依賴。

---

## 4. 模組切分（單一職責、可獨立測試）

| 模組 | 職責 |
|---|---|
| `indexing/pdf_render.py` | PDF → 每頁 PNG（~150–200 DPI） |
| `indexing/vision_parse.py` | 頁圖 → markdown（GPT-5.5） |
| `indexing/chunk.py` | LLM 語意切塊，組裝 chunk + 內部 metadata |
| `indexing/embed.py` | 產生 embedding（text-embedding-3-large） |
| `indexing/build_index.py` | 串接離線流程並持久化索引 |
| `indexing/cache.py` | 內容雜湊 / manifest / 分層快取與續跑邏輯 |
| `retrieval/dense.py` | FAISS 向量檢索 |
| `retrieval/sparse.py` | jieba 斷詞 + BM25 |
| `retrieval/hybrid.py` | RRF 融合 |
| `retrieval/rerank.py` | GPT-5.5 listwise rerank |
| `qa/answer.py` | 答案生成（prompt 組裝 + 低相關度走「資料不足」） |
| `qa/pipeline.py` | 單題流程串接 |
| `io/csv_io.py` | CSV 讀寫（無 header 2 欄、quoting、BOM、保序） |
| `openai_client.py` | OpenAI API 封裝（重試/退避、計時與 token log） |
| `config.py` | 模型、`top-N`、`k`、RRF、路徑等參數 |
| `__main__.py` | CLI：`index` 建索引、`run --input --output` 跑批次 |

---

## 5. 持久化與快取

存於 `data/index/`，**分層快取，每個昂貴步驟各自獨立存檔**；最貴的 GPT-5.5 vision 解析只跑一次。

| 產物 | 存成 | 重算時機 |
|---|---|---|
| Vision 解析（每頁 markdown） | `parsed/<deck>/<page>.md` + `parsed.jsonl` | 該 PDF 內容變更 |
| 語意 chunks + metadata | `chunks.jsonl` | parsed 變更 |
| Embeddings | `embeddings.npy` + `index.faiss` | chunks 或 embedding 模型變更 |
| BM25 稀疏索引 | `bm25.pkl`（含 jieba 斷詞結果） | chunks 變更 |
| 雜湊清單 | `manifest.json`（各 PDF 的 SHA-256） | 每次建索引比對 |

- **失效判斷用內容雜湊（SHA-256）而非時間戳**。PDF 雜湊未變 → 完全跳過該檔的 vision 解析與 embedding。
- **可續跑**：逐頁 vision 結果即時寫快取；中斷或單頁失敗，重跑時從未完成處接續。
- 簡報永不更改的情境下，第一次 `index` 跑完後，之後皆秒級命中快取，不再呼叫 vision/embedding API。

---

## 6. 資料流

### A. 離線建索引（`nlp-qa-system index`，不計時）

```
for each PDF in docs/slides/:
  1. 算 SHA-256，比對 manifest → 未變則跳過，直接用快取
  2. render 每頁 → PNG（~150–200 DPI，足夠 GPT-5.5 high-detail）
  3. 每頁圖 → GPT-5.5 vision：
       忠實轉錄整頁；文字/條列保留原文；表格→markdown table；
       公式→LaTeX；圖表/流程圖→文字描述其語意與關係
  4. LLM 語意切塊：整個 deck 的逐頁 markdown 依序串起 →
       GPT-5.5 依主題切成自包含語意片段（連續相關頁合併、單頁多主題拆開），
       目標 200–500 tokens、上限 ~800
  5. text-embedding-3-large 批次 embed 所有 chunk
  6. 寫入 parsed.jsonl / chunks.jsonl / embeddings.npy + index.faiss / bm25.pkl / manifest.json
```

vision 解析與語意切塊並行（並行上限）加速一次性建置。

### B. 線上查詢（`nlp-qa-system run --input in.csv --output out.csv`，計時）

```
讀 CSV（無 header、2 欄）
載入磁碟索引（mmap FAISS + pickle BM25 + chunks，毫秒級，幾乎不佔計時）
run 階段絕不觸發任何索引建置

對每題 question（跨題並行，上限如 8）:
  1. 混合檢索：
       dense：embed(question) → FAISS top-N
       sparse：jieba 斷詞(question) → BM25 top-N        （N≈20）
       RRF 融合（1/(60+rank)）→ 候選 top-N
  2. Rerank：GPT-5.5 listwise 依相關度重排 → top-k（k≈6）
  3. 生成：GPT-5.5
       system：只依提供片段回答；簡短精確、不多餘解釋；
               用問題語言、專有名詞保留原文；找不到回「資料不足」
       user：question + top-k chunks
       → 答案字串（低 temperature）
  4. 填入第 2 欄

寫出 CSV（同格式、保序）
```

### 預設參數（`config.py` 可調；因快取，重調查詢階段免費即時）

- 檢索 `top-N = 20`、rerank 後 `k = 6`
- RRF 標準融合 `1/(60+rank)`
- 生成低 temperature

---

## 7. 錯誤處理與效率（對應 20%）

- **API 穩定性**：`openai_client` 統一封裝，所有呼叫含指數退避重試；達上限記 log 並回傳明確錯誤，不讓整批 crash。
- **查詢階段並行**：async + 並行上限同時處理多題；瓶頸在 API 往返，並行縮短整批時間。每題計時路徑 = 1 次 rerank + 1 次生成。
- **建索引並行 + 可續跑**：逐頁 vision 並行；即時寫快取；中斷/單頁失敗可接續，單頁最終失敗則跳過標記、不阻斷整個 deck。
- **找不到答案**：rerank 後最高相關度低於門檻或生成判斷上下文不足 → 回簡短「資料不足」，避免亂答。
- **CSV 穩健性**：無 header 2 欄；UTF-8/BOM 容錯；逗號/引號/換行用標準 quoting；保持列順序；空白/異常列安全跳過。
- **可觀測性**：log 各階段耗時與 token 用量。
- **效率備案**：若日後嫌慢，rerank 可降為更輕量或加開關；預設保留以顧 80% 語意分。

---

## 8. 測試策略

原則：OpenAI 呼叫藏在 `openai_client` 介面後，測試注入 fake，快速/確定/零成本。採 TDD。

### 單元測試（注入 fake LLM/embedding）

| 模組 | 測什麼 |
|---|---|
| `io/csv_io` | 無 header 2 欄讀寫往返；quoting；UTF-8/BOM；列順序保持；異常列安全跳過 |
| `retrieval/sparse` | jieba 斷詞 + BM25 排序，中文/英文/中英夾雜 |
| `retrieval/dense` | 給定 fake 向量，top-N cosine 排序正確 |
| `retrieval/hybrid` | RRF 融合：已知兩排名 → 預期結果 |
| `retrieval/rerank` | fake LLM 回傳已知順序 → 驗證重排 + 取 top-k |
| `indexing/chunk` | 語意切塊組裝、長度上下限、過短頁合併 |
| `indexing/cache` | 雜湊命中跳過、PDF 變更才重算 |
| `qa/answer` | prompt 組裝；低相關度走「資料不足」分支 |
| `qa/pipeline` | 單題端到端（全 fake 依賴） |

### 整合測試

- 小 fixture（幾頁合成 page-markdown + stub vision/embedding）→ 建索引 → 跑含 2–3 題 CSV → 斷言答案有填、格式不變、保序。
- 真 API 冒煙測試以 env var / pytest marker 隔離，預設不進 CI。

### 評測輔助（非單元測試）

- **目前無標註 dev set**：參數採合理預設，並用少量自選問題做人工抽查校準。
- 查詢重跑免費（命中快取），可快速 A/B `top-N / k / RRF` 觀察答案變化。
- 若日後取得標註 dev set（問題+標準答案），再加 script 量化準確度。

工具：`pytest`。

---

## 9. 相依套件（初步）

- `openai`（API）
- `pymupdf`（PDF render）
- `faiss-cpu`（dense 檢索）
- `rank-bm25`、`jieba`（稀疏檢索 + 中文斷詞）
- `numpy`
- `pytest`（測試）

---

## 10. 待實作時決定的細節

- vision 解析 prompt 與語意切塊 prompt 的具體措辭。
- 「資料不足」相關度門檻的實際數值（無 dev set，先用合理預設 + 人工抽查校準）。
- 並行上限與重試次數的實際值（依 API rate limit 調整）。
