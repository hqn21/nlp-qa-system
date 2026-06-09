# QA System

# What is QA System?

# Question Answering (QA)

QA = 使用者輸入問題, 系統自動從資料中找到正確答案。常見 QA 系統分類:

- 按答案形式分類
  - 抽取式 QA(Extractive)
    - 在給定上下文中抽取一段文字為答案
    - SQuAD

範例問題: When was Apple  
founded?

範例回答: 1976

模型行為 / 回答來源 : 模型預測答  
案的開始與結束位置 (token  
span)

# Question Answering (QA)

QA = 使用者輸入問題, 系統自動從資料中找到正確答案。常見 QA 系統分類:

- 按答案形式分類
  - 抽取式 QA(Extractive)
    - 在給定上下文中抽取一段文字為答案
    - SQuAD
  - 生成式 QA(Generative)
    - 重組上下文資訊, 自然語言生成答案
    - 常用於開放域問答或複雜推理
    - T5, GPT, BART

範例問題:How did Steve Jobs  
start Apple?

範例回答:Steve Jobs started  
Apple in 1976 with Steve  
Wozniak.

模型行為 / 回答來源: 模型基於  
context 產生完整句子作答

# Question Answering (QA)

QA = 使用者輸入問題，系統自動從資料中找到正確答案。常見 QA 系統分類:

- 按知識來源
  - 封閉式 QA(Closed-book)
    - 依賴模型內部知識作答（不查資料）
    - 早期ChatGPT、GPT-3

範例問題:Who is the CEO of  
Tesla?

範例回答:Elon Musk

模型行為 / 回答來源: 從訓練過程  
學得的參數生成回答

# Question Answering (QA)

QA = 使用者輸入問題，系統自動從資料中找到正確答案。常見 QA 系統分類:

- 按知識來源
  - 封閉式 QA(Closed-book)
    - 依賴模型內部知識作答(不查資料)
    - 早期ChatGPT、GPT-3
  - 開放式 QA(Open-domain)
    - 先查資料再回答(需要 retrieval 模組)
    - RAG

範例問題:Where was the first  
iPhone released?

範例回答:The first iPhone was  
released in the U.S. in 2007.

模型行為 / 回答來源: 從  
Wikipedia 等文件中擷取資訊後生  
成回答

# Question Answering (QA)

QA = 使用者輸入問題, 系統自動從資料中找到正確答案。常見 QA 系統分類:

- 其他常見QA任務類型
  - 對話式問答（Conversational/Dialogue QA）
    - 需根據上下文多輪對話理解和回答問題
    - CoQA、QuAC
  - 多跳問答（Multi-hop QA）
    - 需要跨多個文檔/段落推理, 整合多個資訊點才能回答問題
    - HotpotQA

> 圖示說明：右下方圓角框強調：QA 系統是多任務技術的集合體（理解、檢索、生成）

# 經典資料集與模型基準

SQuAD

- 抽取式QA
- 每題附一段文章，答案位於文章片段中
- 問題範例：When was Apple founded?
- 文章片段："… Apple Inc. was founded in 1976 by …"

# 經典資料集與模型基準

Natural Questions

- 抽取式 / 開放式QA
- 來自真實 Google 搜尋問題, 答案在 Wikipedia 中
- 問題範例：Who won the NBA championship in 2020?
- 文章片段："... The Los Angeles Lakers won the 2020 ..."

# 經典資料集與模型基準

TriviaQA

- 抽取式 / 開放式QA
- 問題來自線上問答網站，文章為相關網頁內容
- 問題範例：What is the capital of New Zealand?
- 文章片段：" ... Wellington is the capital and second-most populous city ..."

# 經典資料集與模型基準

HotpotQA

- 多跳（multi-hop）QA
- 答案需要整合多段資訊推理得出
- 問題範例：Where was the founder of IKEA born?
- 文章片段：
  - Doc1: "IKEA was founded by Ingvar Kamprad."
  - Doc2: "Kamprad was born in Småland, Sweden."

# 抽取式 QA 的模型架構

- 輸入格式:[CLS] 問題 [SEP] 文章 [SEP]
- 模型輸出:預測答案的開始與結束位置
- 常見模型:
  - BERT / RoBERTa
  - ALBERT(較少參數, 提升效能)
  - XLNet(考慮排列組合)
- 模型學習的是位置分佈而非直接生成答案

# 範例

- 使用 BERT 預測答案區段（Answer Span）
- Question:
  - When was Apple founded?
- Context:
  - Apple Inc. is an American multinational technology company headquartered in Cupertino,  
    California. It was founded in 1976 by Steve Jobs, Steve Wozniak, and Ronald Wayne.
- 輸入
  - [CLS] When was Apple founded? [SEP] Apple Inc. is an American multinational ... founded in  
    1976 ... [SEP]
- 模型預測結果（舉例）:
  - 預測 Start token = 第 34 個字 ("founded")
  - 預測 End token = 第 36 個字 ("1976")
- 預測答案（經過一些精修）:
  - 1976

# QA System Evaluation

- 傳統指標
  - Exact Match (EM)
  - F1 Score
  - ROUGE
- 語意評估指標
  - BERTScore
  - Sentence Similarity
- RAG評估指標
  - LLMs as judges (e.g. RAGAS)
- 人工評估

# RAG

# 為什麼需要 RAG？

傳統 LLM 的限制：參考資料固定、生成幻覺(hallucination)嚴重

- 大型語言模型在訓練後<span style="color:red">無法即時取得外部知識</span>
- 只能依賴訓練語料中學到的統計關聯來生成回答
- 當使用者詢問的是模型未見過、或知識已過時的問題，模型可能會憑空捏造答案  
  (hallucination)

範例:

- 問:「中興大學 2024 年的校長是誰？」
  - GPT-3.5 訓練資料止於 2021, 因此可能會回答過時或錯誤的人選
- 問:「在民法中，債務人不履行契約的法律效果是什麼？」
  - 如果模型只看過片段法條，可能會組出類似法律用語但不具備法律邏輯的  內容

# 為什麼需要 RAG？

Fine-tuning 成本高、靈活性低

- Fine-tuning 需重新訓練整個模型或模型的一部分，加入新的知識
- 缺點如下:
  - **需要大量 GPU 資源與時間**
  - **需人工清洗與標註資料**
  - **每次更新都要重新訓練，不易維護**

範例:

- 公司內部導入 LLM 想要回答「人資制度」相關問題，若走 Fine-tuning 路線:
  - 必須蒐集內部文件 (如職員手冊)
  - 整理為 QA 對應格式
  - 將其微調進模型
  - 之後手冊更新又得重訓一次

<div align="center"><span style="color:red;">非常不靈活</span></div>

# 為什麼需要 RAG？

需要一種可以查資料的生成方式

- RAG就是為了讓模型<span style="color:red">先查資料再回答</span>
- 可即時更新知識，無需重新訓練模型

範例：

- 使用者問:「本公司員工休假規定是什麼？」
  → 系統將問題轉成 embedding  
  → 從向量資料庫中找出《員工手冊》相關段落  
  → 把這些段落餵給生成模型，產生符合政策的回答

# RAG 是什麼？

- Retrieval-Augmented Generation = 檢索 + 生成
- Retriever（檢索器）:
  - 根據使用者查詢，從<span style="color:red">外部資料庫中找出語意相似的文本片段</span>（例如: FAQ、法條、PDF文件段落等）
- Generator（生成器）:
  - 將檢索到的內容作為上下文，<span style="color:red">與使用者問題一起輸入到 LLM 中</span>，產生回答。常見模型如 GPT、LLaMA、T5 等。
- 輸入查詢 → 向量化 → 近似查找相關內容 → 回答生成

# Example

使用者提問:「請問公司出差補助的標準是多少？」

- Retriever:查詢被轉為向量，系統到「內部人資手冊」的向量資料庫中查找相似段落
  - 「每人每日補助上限為新台幣 1,200 元」
  - 「國內交通費需憑票核銷，住宿補助另計」
- Generator:將上述段落 + 原始提問一起輸入 LLM
  - 「根據公司內部人資手冊，出差補助每日上限為 1,200 元，並需提供憑證。住宿與交通費用則另行核銷。」

# Retrieval Augmented Generation

## Diagram

- **Response** is shown as the output from the **LLM**.
- **User Query** is shown entering both the **Embedding Model** and the **LLM**.
- **Text Documents** enter the **Embedding Model**.
- The **Embedding Model** converts the user query and text documents into **Embeddings**.
- The embeddings are stored/used within the bracketed **Vector Database**.
- **Nearest Neighbor Search** operates over the embeddings to identify **Nearest Neighbors**.
- The nearest neighbors are passed upward into the **LLM**.
- The **LLM** combines the user query with retrieved nearest-neighbor information to generate the **Response**.

Visible labels in the diagram:

- Response
- LLM
- Nearest Neighbor Search
- User Query
- Nearest Neighbors
- Embeddings
- Vector Database
- Text Documents

# Retrieval Augmented Generation

## Diagram/Figure description

- `User Query` is sent upward into the system.
- `Text Documents` are processed by an `Embedding Model`.
- The `Embedding Model` converts the `Text Documents` into `Embeddings`.
- The `Embeddings` are stored/used within a `Vector Database`.
- `Nearest Neighbor Search` operates over the `Embeddings`.
- `Nearest Neighbor Search` returns `Nearest Neighbors`.
- The `Nearest Neighbors` are passed to the `LLM`.
- The `User Query` is also passed to the `LLM`.
- The `LLM` generates a `Response`.

Visible labels in the diagram:

- `Response`
- `LLM`
- `Nearest Neighbor Search`
- `Nearest Neighbors`
- `Embeddings`
- `Vector Database`
- `Text Documents`
- `User Query`
- `...`

# Vector Database

- 儲存高維度向量資料的資料庫
  - 這些向量資料通常是來自於自然語言、圖像、影片等經過模型轉換後的 embeddings

- 不像傳統關聯式資料庫用主鍵查找資料，而是用<span style="color:red">向量之間的距離</span>(如餘弦相似度)來找出語意相似的內容

- 範例: FAISS, Qdrant, Weaviate

# 資料預處理

<span style="color:red">Garbage In, Garbage Out</span>

預處理 往往是最耗時、但也最能拉開系統差距的關鍵階段

幾個重要步驟:

- Data Parsing & Extraction
- Data Cleaning
- Chunking
- Embedding
- Metadata Attachment & Indexing

# Data Parsing & Extraction

- 純文字提取
  - 將 PDF、Word、HTML、Markdown 等檔案轉換為純文字

- 版面分析
  - 識別文件中的標題層級、段落邊界、頁首頁尾，甚至把複雜的表格轉譯為 Markdown 格式，以保留原始的邏輯結構

- 多模態處理
  - 遇到圖片或圖表時，呼叫 OCR 或 VLM（視覺語言模型）提取文字與生成圖表摘要

# 版面分析

又稱文件理解 (Document Understanding)，目的是要告訴機器人類如何閱讀文件

[圖示說明：紅色水平箭頭由左指向右，紅色垂直箭頭由上指向下，旁邊標示「由左至右，由上到下」，表示文件閱讀順序與版面分析方向。]

由左至右，由上到下

## About Dataset

### Context

The Natural Questions (NQ) dataset is a comprehensive collection of real user queries submitted to Google Search, with answers sourced from Wikipedia by expert annotators. Created by Google AI Research, this dataset aims to support the development and evaluation of advanced automated question-answering systems. The version provided here includes 89,312 meticulously annotated entries, tailored for ease of access and utility in natural language processing (NLP) and machine learning (ML) research.

### Data Collection

The dataset is composed of authentic search queries from Google Search, reflecting the wide range of information sought by users globally. This approach ensures a realistic and diverse set of questions for NLP applications.

# Digital Eavesdropper: Acoustic Speech Characteristics as Markers of Exacerbations in COPD Patients

Julia Merkus  
*Dept. of Language and Speech*  
*Pathology of Radboud University*  
Nijmegen, Netherlands  
julia.merkus@emailaddress.com

*Abstract*—Research suggests that speech deterioration indicates an exacerbation in patients with chronic obstructive pulmonary disease (COPD). This study provides a comparison of read speech of 9 stable COPD patients and 5 healthy controls (I) and 9 stable COPD patients and 9 COPD patients in exacerbation (II). Results showed a significant effect of condition on the number of (non-linguistic) in- and exhalations per syllable (I, II) and the ratio of voiced and silence intervals (II). Also, sustained vowels by 10 COPD patients in exacerbation were compared with 10 vowels in stable condition (III). Results showed an effect of condition on duration, shimmer, harmonics-to-noise ratio (HNR) and voice breaks. It was concluded that HNR, vowel duration and the number of (non-linguistic) in- and exhalations per syllable show potential for remote monitoring. Further research is needed to examine the validity of the results for natural speech and larger sample sizes.

*Keywords—COPD, lung exacerbations, pulmonary disease*

## I. INTRODUCTION

### A. Speech and Speech Disorders

Each human language consists of a set of vowels and consonants which are combined to form words. During the speech production process, thoughts are converted into spoken utterances to convey a message. The appropriate words and their meanings are selected in the mental lexicon [1]. This preverbal message is then grammatically encoded, during which a syntactic representation of the utterance is built. The sounds are yet to be specified, but the abstract word symbols are assigned to their grammatical function before they are structured in a syntactic frame to determine the order [2]. Subsequently, the message is phonologically encoded. During this stage, a phonetic or articulatory plan is retrieved for each individual lemma and the utterance as a whole. Finally, the speaker produces the utterance according to the phonetic plan [3].

(COPD) by investigating which aspects of speech differ between COPD patients and healthy speakers and which aspects differ between COPD patients in exacerbation and stable COPD patients.

### B. Chronic Obstructive Pulmonary Disease

*1) Background:* COPD is an umbrella term used to describe progressive lung diseases characterized by airflow limitation. According to the guidelines provided by the Global Initiative for Chronic Obstructive Lung Disease [6, p. 2], the official definition of COPD is “a common, preventable and treatable disease that is characterized by persistent respiratory symptoms and airflow limitation that is due to airway and/or alveolar abnormalities usually caused by significant exposure to noxious particles or gases.”

*2) Prevalence:* The prevalence of COPD worldwide is estimated at roughly 12%, but the percentage differs greatly between different subgroups [7]. Most COPD patients are suffering from stage II COPD (70%), while stage I, III and IV make up respectively 16%, 11% and 3% of the COPD population. The four greatest predictors of COPD are years and intensity of smoking, age, sex and BMI. Most patients suffering from COPD are smokers with a low BMI, over 50 years old and male [7].

Taking into account the three million annual deaths globally, COPD is currently the fourth leading cause of death in high-income countries and it is expected to be the third leading cause in 2020 due to a higher life expectancy and increasing air pollution [6, 8, 9]. However, the lung disease has been overlooked and neglected for a long time by both the public and the pharmaceutical industry. This neglect might be caused in part by the assumption that COPD is a self-inflicted health condition caused by smoking. Although smoking is the leading cause of COPD in high-income countries, over 15%

# Digital Eavesdropper: Acoustic Speech Characteristics as Markers of Exacerbations in COPD Patients

Julia Merkus  
*Dept. of Language and Speech*  
*Pathology of Radboud University*  
Nijmegen, Netherlands  
julia.merkus@emailaddress.com

**Abstract—**Research suggests that speech deterioration  
indicates an exacerbation in patients with chronic obstructive  
pulmonary disease (COPD). This study provides a comparison  
of read speech of 9 stable COPD patients and 5 healthy controls  
(I) and 9 stable COPD patients and 9 COPD patients in  
exacerbation (II). Results showed a significant effect of  
condition on the number of (non-linguistic) in- and exhalations  
per syllable (I, II) and the ratio of voiced and silence intervals  
(II). Also, sustained vowels by 10 COPD patients in exacerbation  
were compared with 10 vowels in stable condition (III). Results  
showed an effect of condition on duration, shimmer, harmonics-  
to-noise ratio (HNR) and voice breaks. It was concluded that  
HNR, vowel duration and the number of (non-linguistic) in- and  
exhalations per syllable show potential for remote monitoring.  
Further research is needed to examine the validity of the results  
for natural speech and larger sample sizes.

**Keywords—**COPD, lung exacerbations, pulmonary disease

## I. INTRODUCTION

### A. Speech and Speech Disorders

Each human language consists of a set of vowels and  
consonants which are combined to form words. During the  
speech production process, thoughts are converted into spoken  
utterances to convey a message. The appropriate words and  
their meanings are selected in the mental lexicon [1]. This pre-  
verbal message is then grammatically encoded, during which  
a syntactic representation of the utterance is built. The sounds  
are yet to be specified, but the abstract word symbols are  
assigned to their grammatical function before they are  
structured in a syntactic frame to determine the order [2].  
Subsequently, the message is phonologically encoded. During  
this stage, a phonetic or articulatory plan is retrieved for each  
individual lemma and the utterance as a whole. Finally, the  
speaker produces the utterance according to the phonetic plan  
[3].

(COPD) by investigating which aspects of speech differ  
between COPD patients and healthy speakers and which  
aspects differ between COPD patients in exacerbation and  
stable COPD patients.

### B. Chronic Obstructive Pulmonary Disease

**1) Background:** COPD is an umbrella term used to  
describe progressive lung diseases characterized by airflow  
limitation. According to the guidelines provided by the  
Global Initiative for Chronic Obstructive Lung Disease [6, p.  
2], the official definition of COPD is “a common, preventable  
and treatable disease that is characterized by persistent  
respiratory symptoms and airflow limitation that is due to  
airway and/or alveolar abnormalities usually caused by  
significant exposure to noxious particles or gases.”

**2) Prevalence:** The prevalence of COPD worldwide is  
estimated at roughly 12%, but the percentage differs greatly  
between different subgroups [7]. Most COPD patients are  
suffering from stage II COPD (70%), while stage I, III and  
IV make up respectively 16%, 11% and 3% of the COPD  
population. The four greatest predictors of COPD are years  
and intensity of smoking, age, sex and BMI. Most patients  
suffering from COPD are smokers with a low BMI, over 50  
years old and male [7].

Taking into account the three million annual deaths  
globally, COPD is currently the fourth leading cause of death  
in high-income countries and it is expected to be the third  
leading cause in 2020 due to a higher life expectancy and  
increasing air pollution [6, 8, 9]. However, the lung disease  
has been overlooked and neglected for a long time by both the  
public and the pharmaceutical industry. This neglect might be  
caused in part by the assumption that COPD is a self-inflicted  
health condition caused by smoking. Although smoking is the  
leading cause of COPD in high-income countries, over 15%

視為同一行

# 版面分析

Block Detection / Segmentation

Element Classification

Reading Order Determination

Structured Output

![Diagram: A dark page-like rectangle containing multiple blue-gray rectangular blocks of varying sizes. The blocks represent segmented layout regions: wide horizontal header/title areas at the top, a large full-width content block below, then multiple content blocks arranged in two columns. The diagram conveys page layout analysis through detecting blocks, classifying elements, determining their spatial/reading relationships, and producing structured output.]()

# Block Detection / Segmentation

- 掃描整個頁面，找出所有有內容的矩  
  形區域(Bounding Boxes)
- 這時系統還不知道這些區塊是什麼，  
  只知道那裡有墨水或像素

**Figure:** A dark page mockup containing multiple light-outlined rectangular bounding boxes. The boxes mark detected content regions: several horizontal header-like blocks at the top, a large full-width block below, and a two-column layout of rectangular content blocks beneath it separated by a vertical dotted line. The figure conveys that the system identifies rectangular areas containing ink or pixels, without yet knowing what each block represents.

# Element Classification

- 系統接著要判定這些矩形區塊的身分
- 它會將區塊標記為：Title、Paragraph、Table、Figure、Caption 或是應當被過濾掉的雜訊（如 頁首/ 頁尾、頁碼）

**圖示說明：** 右側圖示呈現一頁文件中的多個矩形區塊分類結果。不同顏色的框標示不同元素類別與其位置關係：最上方為「標題」，其下為「作者」與「摘要」；頁面中有多個「內文」區塊，左側包含「圖片」區塊及其下方相連的「圖說」，右側中段包含「表格」區塊；頁面底部有被標示為「雜訊」的小區塊，表示應被過濾掉的內容。

# Reading Order Determination

- 機器需要判斷人類眼睛是怎麼移動的。
- 例如:標題 → 摘要 →左欄文字 →右欄文字, 而不是粗暴地由左至右、由上至下(這樣會把左右兩欄的句子硬拼在一起)

**圖示說明：** 右側圖示是一個深色頁面版面，包含由上到下的標題區、摘要區、內文區，以及左右兩欄文字區塊。藍色箭頭標示閱讀順序：先從頂部標題開始，往下到摘要與上方內容，再進入左欄並向下閱讀，接著以斜向箭頭跳到右欄，最後在右欄由上往下閱讀。左右欄之間以虛線分隔，底部有「排除」按鈕。圖中以 1 到 10 的標記表示各文字區塊或閱讀節點，強調閱讀順序應根據人類視線移動與版面結構判斷，而不是單純由左至右、由上至下排列。

# Structured Output

- 根據前面的分類與順序，將提取出的  
  內容轉換成 Markdown 或 HTML 等  
  結構化格式，保留原始文件的語意階  
  層

> 圖示：右側為一個未經分析的範例文件頁面，以灰色邊框框出，內容混雜標題、作者、段落、表格描述、圖片亂碼與頁碼，呈現尚未轉換為結構化格式前的原始文字狀態。

```text
大型語言模型評估指南
楊小明
本文介紹了 RAG 系統...
隨著 AI 的發展, 評估 這張表顯示了我
們
RAG 系統變得越來 在不同資料集上
的
越重要。傳統的檢索 測試結果。模型
A
方法已經無法滿足 的準確率最高, 達
複雜推理的需求。到了 95%。
[圖片亂碼] 模型A 95% 模型B 80%
因此我們提出了新 綜合以上數據, 我
的圖譜架構。們認為...
Page 1
```

<span style="color:red">未經分析的範例</span>

# Structured Output

```json
{
  "element_type": "Title",
  "text": "大型語言模型評估指南",
  "metadata": {
    "page_num": 1,
    "bounding_box": [100, 50, 500, 80]
  }
},
{
  "element_type": "Abstract",
  "text": "本文介紹了 RAG 系統...",
  "metadata": {
    "page_num": 1,
    "parent_section": "大型語言模型評估指南"
  }
},
```

JSON 結構化（適合Chunking階段）

# 大型語言模型評估指南

**作者:** 楊小明

## 摘要

本文介紹了 RAG 系統...

## 1. 簡介 (左欄內文)

隨著 AI 的發展，評估 RAG 系統變得越來越重要。傳統的檢索方法已  
經無法滿足複雜推理的需求。

![系統架構圖](image_001.png)  
*圖 1:本研究提出的進階RAG 系統架構*

因此我們提出了新的圖譜架構。

## 2. 實驗結果 (右欄內文)

這張表顯示了我們在不同資料集上的測試結果。模型A 的準確率最高  
，達到了 95%。

| 模型名稱 | 準確率 | 召回率 |
|:---|:---|:---|
| 模型 A | 95% | 92% |
| 模型 B | 80% | 78% |

綜合以上數據，我們認為..

Markdown 結構化（適合餵給LLM）

圖示說明：左側展示以 JSON 將文件元素拆成 `element_type`、`text`、`metadata` 等欄位，適合 Chunking 階段；右側展示同一份內容以 Markdown 保留標題、作者、段落、圖片與表格結構，適合餵給 LLM。

# 版面分析工具

- Rule-based
  - 利用 PDF 檔案底層的字元座標 (X, Y)、字體大小與字型粗細來寫判斷規則。例如：字體最大且置中的是標題、Y 座標間距小的是同一段落
  - e.g. PyMuPDF
  - 速度極快、幾乎不耗算力;但遇到掃描檔(沒有底層文字座標)、複雜的雙欄或不規則排版時，規則就會徹底失效
- CV-based / Deep Learning
  - 把 PDF 轉成圖片, 把排版分析當作物件偵測任務來做
  - e.g. YOLO, LayoutLM, PaddleOCR
- Vision-Language Model, VLM
  - 直接使用VLM, 如 ChatGPT 或 Gemini, 將文件截圖丟給它, 下 Prompt 請它將內容轉成 Markdown 格式
  - 效果最好, 但運算成本高且處理速度較慢

# Data Cleaning

- 提取出來的文字通常夾雜大量雜訊
- 刪除多餘的空白、換行符號、特殊的亂碼字符
- 移除不具資訊價值的頁碼、浮水印、或是網頁抓取時殘留的 HTML 標籤、導覽列  
文字
- 將特定的格式統一，例如日期格式統一、繁簡轉換、全半形標點符號統一等

# Chunking

- LLM 和 Embedding 模型都有 Context Window的長度限制
- 必須將長篇文章切分成多個較小的Chunks
- 切得太大, 容易包含過多雜訊導致檢索不精準;切得太小，又會喪失上下文的語意連貫性

```text
大型語言模型（LLM）的評估是確保模型在特定任務中表現良好的關鍵過程。通常，評估會涉
及準確度、流暢度以及安全性。而在構建檢索增強生成（RAG）系統時，文本切塊
（Chunking）是一個基礎步驟。切塊的好壞直接影響到向量檢索的精準度。如果切塊太小，可
能遺失上下文；如果切塊太大，則可能包含過多噪音，導致 LLM 難以提取核心資訊。透過調整
區塊大小和重疊，開發者可以優化資訊檢索的顆粒度。重疊部分確保了跨區塊的語境連貫性。
例如，在處理長篇技術文件時，保留 10% 到 20% 的重疊通常能獲得較佳的檢索效果。當前的
切塊技術正從單純的字數切分演進到基於語義結構的切分，以提高人工智慧對文本理解的深度
與廣度。高品質的資料處理是所有 AI 專案成功的墊腳石。
```

**圖示/關係描述：** 左側是一段長篇文字；右側將同一段文字切分成四個較小區塊。區塊 #1、區塊 #2、區塊 #3 各為 100 字，區塊 #4 為 84 字。相鄰區塊之間保留重疊文字，藍色標示重疊部分，用來維持跨區塊的語境連貫性。

| 區塊 | 字數 | 內容 |
|---|---:|---|
| 區塊 #1 | 100 字 | 大型語言模型（LLM）的評估是確保模型在<br>特定任務中表現良好的關鍵過程。通常，<br>評估會涉及準確度、流暢度以及安全性。<br>而在構建檢索增強生成（RAG）系統時，<br>文本切塊（Chunking）是一個基礎步驟。<br>切塊的 |
| 區塊 #2 | 100 字 | Chunking）是一個基礎步驟。切塊的好壞<br>直接影響到向量檢索的精準度。如果切塊<br>太小，可能遺失上下文；如果切塊太大，<br>則可能包含過多噪音，導致 LLM 難以提取<br>核心資訊。透過調整區塊大小和重疊，開<br>發者可 |
| 區塊 #3 | 100 字 | 心資訊。透過調整區塊大小和重疊，開發<br>者可以優化資訊檢索的顆粒度。重疊部分<br>確保了跨區塊的語境連貫性。例如，在處<br>理長篇技術文件時，保留 10% 到 20% 的重<br>疊通常能獲得較佳的檢索效果。當前的切<br>塊技術正 |
| 區塊 #4 | 84 字 | 常能獲得較佳的檢索效果。當前的切塊技<br>術正從單純的字數切分演進到基於語義結<br>構的切分，以提高人工智慧對文本理解的<br>深度與廣度。高品質的資料處理是所有 AI<br>專案成功的墊腳石。 |

# 常見策略

- Fixed-size chunking
  - 例如設定每 200 個 Token 切一塊，並設定一定的 Overlap (例如 50 個 Token)以防止一個完整的句子被硬生生從中間截斷
- Recursive chunking
  - 按照特定標點符號的優先順序 (例如先依據段落 \n\n 切，若還是太大則依據句號 。 切，最後才依據逗號，切)，盡可能保持句子的完整性
- Semantic chunking
  - 利用小型的 Embedding 模型計算相鄰句子的語意相似度，如果兩句話的意思發生了明顯的轉折 (Cosine Similarity 低於某個閾值)，就切斷
  - 能確保同一個 Chunk 都在討論同一個主題

# Embeddings

## Diagram

- **N-Texts** → **NLP** → **N-Word Embeddings**
  - **N-Texts** are depicted as a stack of text documents.
  - **NLP** is depicted with gears, indicating processing.
  - **N-Word Embeddings** are depicted as stacked numeric vectors with example values: `0.3`, `0.02`, `0.8`, `0.6`, `...`, `0.4`.

- **N-Images** → **CNN/Vision Transformer** → **N-Image Embeddings**
  - **N-Images** are depicted as a stack of images, with the front image showing a dog.
  - **CNN/Vision Transformer** is depicted with gears, indicating processing.
  - **N-Image Embeddings** are depicted as stacked numeric vectors with example values: `0.3`, `0.02`, `0.8`, `0.6`, `...`, `0.4`.

The diagram conveys that multiple texts or images are transformed by their respective models into corresponding embedding vectors.

# Multimodel Vector DB

- Clip Model (Contrastive Language-Image Pre-Training)
- Trained on image & text

## Diagram

Embeddings represent text & image features

The figure illustrates the CLIP workflow:

1. **Contrastive pre-training**
   - Text input example: “Pepper the aussie pup”
   - The text is passed through a **Text Encoder** to produce text embeddings \(T_1, T_2, T_3, \ldots, T_N\).
   - An image is passed through an **Image Encoder** to produce image embeddings \(I_1, I_2, I_3, \ldots, I_N\).
   - A similarity matrix compares image embeddings against text embeddings, with entries such as:
     - \(I_1 \cdot T_1\)
     - \(I_1 \cdot T_2\)
     - \(I_1 \cdot T_3\)
     - \(\ldots\)
     - \(I_1 \cdot T_N\)
     - \(I_2 \cdot T_1\)
     - \(I_2 \cdot T_2\)
     - \(I_2 \cdot T_3\)
     - \(\ldots\)
     - \(I_2 \cdot T_N\)
     - \(I_3 \cdot T_1\)
     - \(I_3 \cdot T_2\)
     - \(I_3 \cdot T_3\)
     - \(\ldots\)
     - \(I_3 \cdot T_N\)
     - \(\ldots\)
     - \(I_N \cdot T_1\)
     - \(I_N \cdot T_2\)
     - \(I_N \cdot T_3\)
     - \(\ldots\)
     - \(I_N \cdot T_N\)

2. **Create dataset classifier from label text**
   - Labels shown:
     - plane
     - car
     - dog
     - ...
     - bird
   - Labels are inserted into the prompt: “A photo of a {object}.”
   - The prompt is passed through a **Text Encoder** to produce text embeddings \(T_1, T_2, T_3, \ldots, T_N\).

3. **Use for zero-shot prediction**
   - An image is passed through an **Image Encoder** to produce an image embedding \(I_1\).
   - The image embedding is compared with text embeddings using similarities such as:
     - \(I_1 \cdot T_1\)
     - \(I_1 \cdot T_2\)
     - \(I_1 \cdot T_3\)
     - \(\ldots\)
     - \(I_1 \cdot T_N\)
   - The highest matching text prompt identifies the image as: “A photo of a dog.”

Source: https://github.com/openai/CLIP

# Image Querying

```text
Query → CLIP Embeddings → Vector DB → Result
```

Diagram description: A query image of a dog is passed through CLIP Embeddings, producing vector representations. These embeddings are used to search a Vector DB, which returns a visually similar dog image as the Result.

# Text Querying

```text
„dog in
grassland“
```

Query → CLIP Embeddings → Vector DB → Result

**Diagram description:** A text query labeled **Query** containing “„dog in grassland“” is passed through **CLIP Embeddings**, then searched in a **Vector DB**, producing a **Result** image of a dog standing on grassland.

# Metadata Attachment & Indexing

- 將生成的向量存入向量資料庫時，除了向量本身，還會搭配 metadata
- e.g. 文件檔名、作者、發布日期、來源 URL、所在的章節標題、甚至是該區塊的
  上一塊與下一塊的 ID
- Metadata 是進行進階檢索的核心
  - 例如，若使用者問「2025 年這篇論文的結論是什麼？」，系統可以先透過  metadata 過濾掉所有
    2025 年以外或非論文的檔案，再進行向量相似度比對，可以大幅提升檢索的精準度與速度

# Retriever

功能:

- 根據使用者的Query從外部知識庫中擷取語意最相關的資料段落
- 通常透過向量化查詢 + ANN 完成
- 輸出格式通常為多段文字(Top-K passages)

流程步驟:

1. 使用語言模型 (如Sentence-BERT) 將 Query 向量化
2. 在向量資料庫中進行相似度搜尋 (例如: 找出最靠近的前3 段落)
3. 將這些段落傳給 Generator 做生成

Retriever 常見工具:

- 向量資料庫:FAISS、Qdrant、Weaviate
- 向量模型:Sentence-BERT、MiniLM、Instructor-XL、OpenAI Embeddings

# Approximate Nearest Neighbor, ANN

- 由於高維度向量空間的計算非常耗時，向量資料庫會使用 ANN 技術 (如  
  HNSW、IVF、PQ 等) 來大幅加速查詢:
  - 犧牲一點查詢精度，換取大幅提升查詢速度
  - 常見的演算法如:
    - HNSW (Hierarchical Navigable Small World)
    - IVF (Inverted File Index)
    - PQ (Product Quantization)

https://www.pinecone.io/learn/series/faiss/hnsw/

# Hierarchical Navigable Small World

概念:

- 建立一個<span style="color:red">分層圖結構</span>, 每層都是一個小世界圖(Small World Graph)，高層維持全局連結，低層細節更密集。
- 查詢時，從上層開始逐層往下，逐步靠近目標

優點:

- 查詢速度快，準確率高
- 適合中大型資料集 (數萬到數百萬筆)

圖示:

三個堆疊的平面代表 HNSW 的分層圖結構。最上層較稀疏，標示有 **entry point**，查詢從此進入；藍色箭頭表示在同一層中沿著連結移動以靠近目標，並透過垂直虛線逐層下降到更低層。中層與底層包含更多節點與更密集的連結，虛線表示同一節點在不同層之間的對應關係。底層標示黃色的 **query vector**，搜尋最終在底層靠近並找到標示為 **nearest neighbor** 的節點。

https://www.pinecone.io/learn/series/faiss/hnsw/

# Hierarchical Navigable Small World

概念:

- 建立一個<span style="color:red">分層圖結構</span>, 每層都是一個小  
  世界圖(Small World Graph)，高層維  
  持全局連結，低層細節更密集
- 查詢時，從上層開始逐層往下，逐步靠  
  近目標

優點:

- 查詢速度快，準確率高
- 適合中大型資料集(數萬到數百萬筆)

圖示說明：右側圖示呈現 HNSW 的分層圖結構。最上層有一個標示為「entry point」的進入點，查詢從高層開始，沿著藍色箭頭在各層節點間導航；虛線表示同一資料點在不同層之間的對應關係。搜尋會逐層往下移動，到較低層更密集的圖中繼續靠近目標。底層標示「query vector」的黃色節點代表查詢向量，搜尋最終找到標示為「nearest neighbor」的最近鄰節點。

> 就像從地圖的世界地圖開始，逐層放大到  
> 城市圖、街道圖，最終找到最近的店家

https://docs.oracle.com/en/database/oracle/oracle-database/23/vecse/understand-inverted-file-flat-vector  
-indexes.html

# Inverted File Index

概念:

- 將所有向量分成多個 <span style="color:red">區域(cell)</span>，查詢時只  
  在最接近的幾個區域內比對。
- 使用 **K-means** 來預先將資料切成不同區  
  塊。

優點:

- 節省查詢成本，不必遍歷全部資料
- 適合高維度向量的大型資料集

圖示：右側圖將向量空間分割成多個由邊界隔開的區域（cell），標示為 **#1、#2、#3、#4、#5**。每個區域內包含不同顏色的向量點，表示 K-means 將資料預先分群到不同區塊；查詢時只需在最接近的幾個區域內進行比對，而不必遍歷全部資料。

https://docs.oracle.com/en/database/oracle/oracle-database/23/vecse/understand-inverted-file-flat-vector  
-indexes.html

# Inverted File Index

## 概念:

- 將所有向量分成多個區域(cell)，查詢時只  
  在最接近的幾個區域內比對。
- 使用 **K-means** 來預先將資料切成不同區  
  塊。

## 優點:

- 節省查詢成本，不必遍歷全部資料
- 適合高維度向量的大型資料集

## 圖示說明

右上圖是一個向量空間被分割成多個區域的示意圖，區域以淺藍色邊界劃分，並標示為 **#1**、**#2**、**#3**、**#4**、**#5**。不同顏色的叉號代表不同區域中的資料點，黑色點代表各區域的中心或查詢相關的參考點。圖中表達的是：資料會依照相近程度被分配到不同 cell 中，查詢時只需要在最接近的幾個區域內比對，而不是遍歷全部資料。

> 好比把整座圖書館依主題分區(法律區、醫  
> 學區)，你要找一本「關於醫療法律的書」，  
> 就先進醫學區與法律區，減少遍歷全部書  
> 架的成本

https://towardsdatascience.com/similarity-search-product-quantization-b2a1a6397701/

# Product Quantization

概念:

- 將每個高維度向量切成多段<span style="color:red">子向量</span>，並對每段分別進行量化編碼。
- 查詢時只比對子向量的近似代表，達到<span style="color:red">壓縮資料、加速比對</span>的目的。

優點:

- 節省儲存空間(將向量壓縮成位元編碼)
- 適合儲存與查詢超大規模資料集

## 圖示說明

右側圖示展示 Product Quantization 的編碼流程：

- `original vector`：最上方一條原始向量。
- `subvectors`：原始向量被切分成多個子向量。
- `clustering`：每個子向量分別進入各自的聚類空間，與多個 `centroids` 比較，選擇 `closest centroid`。
- `quantized vectors`：每段子向量被量化為最接近的 centroid 代表色塊。
- `reproduction values`：各段量化後以索引值表示，依序為 `50`、`118`、`29`、`47`。
- `PQ code`：這些 reproduction values 組成 Product Quantization code。
- `Encoding using quantization`：整體流程表示透過量化將原始向量編碼為較短的 PQ code。

https://towardsdatascience.com/similarity-search-product-quantization-b2a1a6397701/

# Product Quantization

概念：

- 將每個高維度向量切成多段<span style="color:red">子向量</span>，並對每段分別進行量化編碼。
- 查詢時只比對子向量的近似代表，達到<span style="color:red">壓縮資料、加速比對</span>的目的。

優點：

- 節省儲存空間（將向量壓縮成位元編碼）
- 適合儲存與查詢超大規模資料集

圖示：

- `original vector`：最上方一條完整的原始向量。
- `subvectors`：原始向量被切分成多個子向量。
- `clustering`：每個子向量分別進行分群；圖中標示 `centroids`、`subvector`、`closest centroid`，表示子向量會被指派到最接近的 centroid。
- `quantized vectors`：每段子向量以其最接近的 centroid 顏色表示，形成量化後的向量。
- `reproduction values`：量化後各段以代碼值表示，圖中依序為 `50`、`118`、`29`、`47`。
- 整體關係：原始向量 → 切成子向量 → 各段獨立分群並找最近 centroid → 轉成量化向量 → 以 reproduction values 編碼。

> 像是用大方向來做快速估算：你找一張臉，  
> 先比膚色、再比眼距、再比嘴型，各部份做  
> 粗略匹配，不逐像素對照

# Generator

功能：

- 接收使用者查詢與 Retriever 擷取的內容
- 將它們結合起來輸入語言模型，生成符合語意、上下文的自然語言回答
- 負責回應的<span style="color:red">流暢性、完整性與推理能力</span>

Generator 通常為：

- 預訓練的 LLM, 如 GPT、LLaMA、T5、Flan-T5、Mistral 等
- 這些模型使用“Query + Context”當成 Prompt, 並生成對應答案

# Example

Question: How do I reset my password?

Context:

1. To reset your password, go to Settings > Security.

2. You can also click ‘Forgot Password’ on the login page.

Answer:

→（模型開始生成）

# RAG 與 Fine-tuning 比較

|  | Fine-tuning | RAG |
|---|---|---|
| 可更新性 | 需重新訓練 | 可即時查詢 |
| 成本 | 高 | 低 |
| 知識更新 | 難 | 容易 |
| 幻覺控制 | 部分有效 | 可降低風險 |

# RAG 與 Fine-tuning 比較

|  | Fine-tuning | RAG |
|---|---|---|
| 可更新性 | 需重新訓練 | 可即時查詢 |
| 成本 | 高 | 低 |
| 知識更新 | 難 | 容易 |
| 幻覺控制 | 部分有效 | 可降低風險 |

RAG是否還有幻覺問題？

# 為什麼 RAG 仍有可能有幻覺？

## 檢索內容錯誤或不足

- 如果 Retriever 沒有找到真正相關的內容(例如查錯段落或漏掉關鍵資訊)  
  ， Generator 只能憑片段或無關內容硬湊答案
- 幻覺來源:Retriever 找錯 → Generator 也會跟著亂講

例子:

- 問:「請問休假規定中的特休天數是多少？」
- Retriever 找到的段落只有「加班費算法」， Generator 只好自由發揮回答「一般為  
  7 天」，但實際錯誤

# 為什麼 RAG 仍有可能有幻覺？

## **Generator 忽略上下文(常見於強模型)**

- 即使 Retriever 提供了正確段落，生成模型仍可能沒好好看懂上下文或只拿一部分來回答
- 強大的 LLM 有時反而傾向於**自己推測**，而不是老實照段落回答

例子：

- 上下文段落：「公司規定特休年限依到職年資計算，前兩年為 3 天」
- 但模型卻回答：「每年固定 7 天」——基於台灣勞基法

# 為什麼 RAG 仍有可能有幻覺？

## 使用者提問模糊

- 問句本身若語意不清、模糊或語法錯誤，也會導致模型難以正確理解並匹配正確的段落。

例子：

- 問:「可不可以請？」(沒指明請什麼) → 系統可能取回錯誤類型的假別段落 → 幻覺式生成

# 進階RAG

# 檢索前優化

讓使用者的問題變得更適合檢索

- Query Rewriting
  - 利用 LLM 將使用者的問題重新表述為更精準、包含更多領域關鍵字的  查詢
- Query Expansion
  - 產生不同版本的 query
- Query Decomposition
  - 將單一問題拆解成多個子問題（Sub-queries), 或是從不同角度生成多個相似的 查詢，分別進行  
    檢索後再將結果合併
- Metadata filter
  - 用額外資訊過濾掉不相關段落

# Query Rewriting

- Coreference Resolution
  - 模型先根據歷史對話補全完整問題 → 再檢索
  - 例如：「那它的利息怎麼算？」→ 重寫為：「定期存款的利息怎麼算？」
- HyDE (Hypothetical Document Embeddings)
  - 問題(短)跟答案(長)，在向量空間裡的距離其實有很遙遠 （Semantic Gap）
  - 當使用者提出一個簡短的問題時，HyDE 不直接拿問題去檢索，而是先請 LLM產生一個假答案
  - 因為這個假答案的篇幅、句型和用詞，在向量空間中通常會比短問題更接近**真實的長篇參考文件**
  - Query → 什麼是 LLM 的 *Lost in the middle* 現象？
  - Hypothetical document → *Lost in the middle* (迷失在中間)現象是指大型語言模型（LLM）在處理非常長的上下文時.....
  - True document → 根據 *Liu* 等人的實驗研究指出，當輸入給語言模型的上下文長度（ *Context Window*）增加時，模型提取關鍵資訊的效能會呈現 *U* 型曲線。具體而言， ...

# Query Expansion

- 單一的查詢即使寫得再好，也可能因為**詞彙不匹配**而漏掉關鍵資訊
- Multi-Query Generation
  - Query → *LLM 評估方法*
  - Exapnsion → *大型語言模型評估指標、 Generative AI evaluation metrics、如何衡量 LLM 表現*

- Keyword Injection
  - 補上專業術語
  - Query → *如何長肌肉*
  - Keyword exapnsion → *肌肥大 (Hypertrophy)、蛋白質攝取 (Protein intake)*

# Query Decomposition

- Sub-queries
  - Query → 比較 GraphRAG 和 Naive RAG 在處理跨文件實體關聯時的效能差異？
  - Sub1 → 什麼是 GraphRAG？它如何處理實體關聯？
  - Sub2 → Naive RAG 如何處理實體關聯？
  - Sub3 → 這兩者在跨文件處理上的效能評估數據為何？
- Step-back prompting
  - Query → 為什麼我的 x86 組合語言程式碼裡，連續執行了五次 PUSH EAX，然後只執行了兩次 POP EBX 就直接呼叫 RET，程式會發生 Segmentation Fault？
  - Step-back Question → 在 x86 組合語言中，Stack的運作機制是什麼？以及 RET 指令在底層是如何與 ESP 互動的？
  - Retrieved answer → Stack 是一個後進先出 (LIFO) 的記憶體區段。呼叫副程式時，系統會自動將「返回位址」Push 到 Stack 頂部。當程式執行 RET 指令時...
  - Final answer: Decoder(step-back question + retrieved answer) → 你的程式會崩潰，根本原因是...

# Metadata Filter

- 每段文件除了內容本身 (text embedding)，通常還會有一些「額外欄位」，例如:
  - 類別 (例如: FAQ / 條款 / 使用說明)
  - 來源 (PDF 名稱 / 頁碼)
  - 更新日期
  - 主題標籤 (如:「人資」、「法務」、「客服」)

- 透過這些 metadata，我們可以只檢索特定範圍內的資料，避免不相關資料干擾結果

- 應用場景: 多類型文件混在一起時 (例如 PDF + FAQ)

# Example

Query:「公司的病假規定是什麼？」

- 資料庫中有很多資料, 有些來自「法務文件」、有些是「人資手冊」
- 用 metadata filter:
  - 只查「類別=人資」的段落
  - 只查「文件名稱=員工手冊.pdf」

- 這樣可以避免模型檢索到「法律案例」或「產品保固條款」來亂答

# 檢索階段優化

<span style="color:red">優化從資料庫中撈取資訊的精準度與覆蓋率</span>

- Hybrid Search
  - 結合傳統的關鍵字檢索（如 BM25, 擅長精確匹配專有名詞）與密集向量檢索（ Dense Retrieval, 擅長語意理解），並透過 Weight Fusion, RRF等演算法合併結果

# 如何融合？

- Weighted Fusion
  - 先對不同檢索器得到的分數進行正規化
  - 必須針對特定的資料集去微調找出最佳的 α值

\[
Final\_Score = \alpha \cdot Dense\_Score + (1-\alpha) \cdot Sparse\_Score
\]

- RRF (Reciprocal Rank Fusion)
  - R: 檢索器的集合 (例如: {BM25, dense vector})
  - r: 其中一個檢索器
  - rank_r(d): 文件 d 在檢索器 r 中排出的名次 (第 1 名就是 1, 第 2 名就是 2)
  - k:平滑常數 (通常預設為 60), 避免排名第 1 的文件權重過高而碾壓其他結果

\[
RRF\_Score(d) = \sum_{r \in R} \frac{1}{k + rank_r(d)}
\]

# 檢索後優化

<span style="color:red">撈出大量文件後，必須在放入 LLM 的 Context Window 前進行過濾與排序</span>

- Reranking
  - 根據查詢與檢索文件的相關性重新打分排序，將最相關的文本推到最前面
- Context Compression/Filtering
  - 剔除檢索文件中的冗餘資訊，只保留能回答問題的核心句子，以節省 Token 消耗並提升 LLM 回答的準確度

# Re-Ranking

- 向量搜尋可能會找出語意相近但不一定最有用的段落。Re-ranking 是對這些初步找出的段落再做排序，根據它們與問題的關聯性調整先後順序。

- 方式：
  - 使用 BERT 對「Query + Passage」組合打分
    - Ex: [CLS] 特休假最多可以請幾天？ [SEP] 本公司員工每年可享 7 天特休假 [SEP]
  - 重新安排前 K 筆段落，把最有用的放前面

- 應用場景:Retriever 回傳的 Top-k 品質參差不齊時

# Example

Query:「公司的病假規定是什麼？」

Retriever 找到 5 段資料:

- 「病假最長不得超過三日」(打分 0.95)
- 「請假須提前一天申請」(打分 0.65)
- 「員工旅遊補助方式」(打分 0.15)

→ 使用 Re-ranker 會把 1 放最前、3 被過濾掉，提高 Generator 使用正確段落的機率。

# Context Compression/Filtering

- 將文本中的停用詞、冗言贅字剔除
- 壓縮前：*根據 Stephen 教授在 2025 年 7 月於日本札幌發表的最新研究指出,*  
  *自動化文獻驗證工具能有效提升效率...*
- 壓縮後：*Stephen 2025年7月 日本札幌研究：自動化文獻驗證工具提升效率...*

# 多輪對話下的檢索難題

- 在「多輪對話」中，<span style="color:red">每一句話的意思都跟上一輪有關</span>
- 但大多數向量檢索系統是單輪設計：每次只根據目前的提問來查資料，忽略上下文

會遇到的問題:

- 使用者問:「那它的利息怎麼算？」
  → 沒有上文「它是什麼？」就查不到對的內容
- 模型可能誤檢索到無關資料，或根本抓不到參考段落

# 多輪對話下的檢索難題

解法方向：

- Query rewriting:
  - 模型先根據歷史對話補全完整問題 → 再檢索
    - 例如：「那它的利息怎麼算？」→ 重寫為：「定期存款的利息怎麼算？」

- 對話上下文壓縮成摘要 Query:
  - 多輪對話整理成一段濃縮摘要後再 查詢

# Modular RAG

## Diagram: Modular RAG

### Modules

The diagram shows a modular RAG system with multiple connected modules:

- **Search**
- **Routing**
- **Predict**
- **Retrieve**
- **Rewrite**
- **Rerank**
- **Read**
- **Demonstrate**
- **Fusion**
- **Memory**
- **RAG**

The central **RAG** area contains:

- **Retrieve**
- **Rewrite**
- **Rerank**
- **Read**

Dashed connections indicate relationships among modules:

- An outer dashed loop connects **Routing**, **Search**, **Predict**, **Fusion**, **Memory**, and **Demonstrate**.
- A central dashed loop connects **Retrieve**, **Rewrite**, **Rerank**, and **Read** around **RAG**.
- The diagram conveys that modular RAG systems can combine routing, search, prediction, memory, demonstration, fusion, rewriting, retrieval, reranking, and reading modules.

### Patterns

The diagram shows four RAG patterns:

#### Naive RAG

**Retrieve**  
↓  
**Read**

#### Advanced RAG

**Rewrite**  
↓  
**Retrieve**  
↓  
**Rerank**  
↓  
**Read**

#### DSP  
[Khattab et al.,2022]

**Demonstrate**  
↓  
**Search**  
↓  
**Predict**

#### ITER-RETGEN  
[Shao et al., 2023]

**Retrieve**  
↓  
**Read**  
↓  
**Retrieve**  
↓  
**Read**

A loop arrow connects the final **Read** back to the top **Retrieve**, indicating iterative retrieval and generation.

**Modular RAG**

- Search Module
  - 使用外部工具搜尋資料
- Memory Module
  - 讓 RAG 系統具備跨輪對話的長期與短期記憶，能夠參考過去的檢索紀錄與對話來修正當前的檢索策略
- Routing Module
  - 根據問題的不同，決定應該使用哪個資料來源或模組來檢索資料  
    (e.g. RAG or GraphRAG)

Gao, Y., Xiong, Y., Gao, X., Jia, K., Pan, J., Bi, Y., ... &  
Wang, H. (2023). Retrieval-augmented generation for  
large language models: A survey. arXiv preprint  
arXiv:2312.10997, 2(1), 32.

# GraphRAG

# 傳統 RAG 的痛點

- 無法回答宏觀的全局問題
  - 例如: 這 100 份財報中，最常被提及的潛在風險是什麼？

- 多跳推理能力弱
  - 如果問題需要把 A 文件中的線索與 B 文件中的線索拼湊起來才能解答，傳統 RAG 往往會失敗  
    ，因為這些碎片在向量空間中未必相近

Edge, D., Trinh, H., Cheng, N., Bradley, J., Chao, A., Mody, A., ... & Larson, J. (2024). From local to global: A graph rag approach to query-focused summarization. arXiv preprint arXiv:2404.16130.

```mermaid
flowchart LR
    SD[Source Documents] -->|text extraction<br/>and chunking| TC[Text Chunks]
    TC -->|domain-tailored<br/>summarization| ER[Entities & Relationships]
    ER -->|domain-tailored<br/>summarization| KG[Knowledge Graph]
    KG -->|community<br/>detection| GC[Graph Communities]
    GC -->|domain-tailored<br/>summarization| CS[Community Summaries]
    CS -->|query-focused<br/>summarization| CA[Community Answers]
    CA -->|query-focused<br/>summarization| GA[Global Answer]
```

**Diagram description:** The pipeline begins at **Indexing Time**, where **Source Documents** undergo **text extraction and chunking** to become **Text Chunks**. These are processed through **domain-tailored summarization** to identify **Entities & Relationships**, which are again summarized in a domain-tailored way into a **Knowledge Graph**. The **Knowledge Graph** is partitioned through **community detection** into **Graph Communities**. At **Query Time**, **Graph Communities** are converted through **domain-tailored summarization** into **Community Summaries**, then through **query-focused summarization** into **Community Answers**, and finally through another **query-focused summarization** step into the **Global Answer**.

**Pipeline Stage:** **Indexing Time** → **Query Time**

Figure 1: Graph RAG pipeline using an LLM-derived graph index of source document text. This graph index spans nodes (e.g., entities), edges (e.g., relationships), and covariates (e.g., claims) that have been detected, extracted, and summarized by LLM prompts tailored to the domain of the dataset. Community detection (e.g., [Leiden, Traag et al., 2019](#)) is used to partition the graph index into groups of elements (nodes, edges, covariates) that the LLM can summarize in parallel at both indexing time and query time. The “global answer” to a given query is produced using a final round of query-focused summarization over all community summaries reporting relevance to that query.

# 查詢階段

- Local search
- Ex: A 教授與 B 實驗室有哪些合作計畫？
  - 抓出關鍵實體 → A教授和B實驗室
  - 到知識圖譜中，找到代表 A 教授和B 實驗室的節點
  - 沿著Edges向外找出與他們有直接或間接關聯的其他節點與資訊
  - 把這些節點、關係描述，以及背後對應的原始文本區塊一起交給 generator
- Global search
- Ex: 這 500 份文獻中，目前該領域最大的三個挑戰是什麼？
  - 讀取某個層級(自訂)所有的社群摘要
  - 假設有20個社群摘要，再根據這 20份摘要產出20個局部答案，並給每個答案一個關聯度評分
  - 把分數最高的幾個局部答案收集起來，統整生成最終的完整回答