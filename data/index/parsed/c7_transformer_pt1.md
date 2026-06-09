# Transformer

## Diagram description

A horizontal timeline arrow points from left to right, indicating chronological progression of language models. Blue rounded boxes are connected to the timeline by vertical lines. Models above and below the line are positioned according to their release dates. `ALBERT 2019/09` is shown below and connected vertically beneath `RoBERTa 2019/07`, indicating a close chronological relationship following RoBERTa.

| Model | Date |
|---|---|
| Transformer | 2017/06 |
| GPT | 2018/06 |
| BERT | 2018/10 |
| GPT-2 | 2019/02 |
| RoBERTa | 2019/07 |
| ALBERT | 2019/09 |
| GPT-3 | 2020/05 |
| GPT-4 | 2023/03 |

# RNN

**Diagram description:** The slide shows an RNN unfolded through time and its compact recurrent form. In the unfolded view, `X(t)` feeds into an `RNN` block, which outputs `Y(t)`. The hidden state is passed horizontally to the next `RNN` block, where `X(t+1)` feeds in and `Y(t+1)` is output. An ellipsis indicates this process continues over time. On the right, the compact RNN diagram shows `X` feeding into an `RNN` block, producing `Y`, with a recurrent self-loop indicating the hidden state feeds back into the RNN.

- 每個輸出都要依賴前一個輸出，因此在進行反向訓練時，都會乘上參數越乘越大會造成**梯度爆炸**，導致模型不穩定甚至無法訓練
- 反之，則造成**梯度消失**，導致權重幾乎沒改變

# RNN

|  | RNN | Transformer |
|---|---|---|
| 並行<br>處理<br>能力 | RNN處理下一個詞必須知道前一個詞的結果，因此難以進行並行計算 | Transformer使用**注意力機制**，可以同時處理整個序列的所有元素 |
| 長序列<br>距離依賴<br>問題 | 由於梯度消失和梯度爆炸問題，難以捕捉到序列中長距離詞之間的依賴關係。<br>儘管LSTM和GRU等RNN變體都設計來處理梯度消失問題，但實際效果仍有限 | **注意力機制**使模型直接關注序列中任意兩個位置之間的關係，無論距離多遠，使得它能更好地捕捉長距離關係 |

# Transformer

- 於2017年推出, 將原始的RNN架構改成 Attention mechanism 同時處理輸入序列的所有位置, 並通過多頭注意力等機制捕捉不同層次的特徵
- Transformer 的 Attention mechanism 允許所有位置的計算都可以並行進行

## Diagram

A flowchart shows a machine translation Transformer architecture:

- The input box labeled **機器翻譯** points upward into the **Encoder**.
- The **Encoder** points right to the **Decoder**.
- The **Decoder** points upward to the output box labeled **machine translate**.
- The **Encoder** and **Decoder** are shown as two large yellow blocks inside one enclosing rectangular frame.

# Attention mechanism

當第一眼看到這張圖，注意力集中在哪裡

## Figure

Text on figure:

2009莫拉克颱風  
8/5 20:30 - 8/10 05:30累積雨量

Compass: N, W, E, S

Legend:

單位：mm

- >1,500
- 1,500
- 1,300
- 1,000
- 900
- 800
- 700
- 600
- 500
- 400
- 300
- 200
- 150
- 100
- 60
- 20

NCDR

Scale: 0 12.5 25 50 75 100 Km

Description: The figure is a color-coded map of Taiwan showing accumulated rainfall during 2009 Typhoon Morakot from 8/5 20:30 to 8/10 05:30. Different colors correspond to rainfall amounts in millimeters according to the legend. A thick red rectangle highlights the central-to-southern portion of Taiwan, especially the area with very high rainfall shown in purple, pink, and red, indicating where visual attention is being directed.

# Attention mechanism

## Flowchart

```text
[eyes image]
接收訊息
   ↓  整張圖片
Sensory memory
   ↓  Attention(放入重要的)
Working memory
```

The flowchart conveys that received information from the whole image enters **Sensory memory**, and through **Attention(放入重要的)** important information is placed into **Working memory**.

## Map/Figure

**2009莫拉克颱風**  
**8/5 20:30 - 8/10 05:30累積雨量**

A rainfall accumulation map of Taiwan is shown, with a red rectangular highlight emphasizing the central-to-southern mountainous region where the highest rainfall accumulations appear. The color legend indicates rainfall amount in millimeters, with pink/purple/red regions representing higher rainfall and green/blue regions representing lower rainfall.

**Compass labels:** N, W, E, S

**單位：mm**

| Legend |
|---|
| >1,500 |
| 1,500 |
| 1,300 |
| 1,100 |
| 1,000 |
| 900 |
| 800 |
| 700 |
| 600 |
| 500 |
| 400 |
| 300 |
| 200 |
| 150 |
| 100 |
| 60 |
| 20 |

**NCDR**

**Scale:** 0 12.5 25 50 75 100 Km

# Attention mechanism

**Diagram/Figure:**

- Eyes icon
  - 接收訊息
  - Downward arrow labeled 整張圖片
- Orange box: Sensory memory
  - Downward arrow labeled Attention(放入重要的)
- Yellow box: Working memory
- Red arrow from Attention(放入重要的) points to:
  - 如何依照輸入的重要性
  - 給予相應的權重

**Meaning:** The figure shows information being received visually as a whole image, entering Sensory memory, then through Attention(放入重要的) important information is selected and moved into Working memory. The attention mechanism assigns corresponding weights according to the importance of the input.

# Machine translation

- Sequence-to-sequence (encoder - decoder model)

**Diagram/Figure (left):**

- A document icon labeled `RAW` points to a box labeled `Encoder`.
- The `Encoder` connects via a dashed line to a circle labeled `hidden`.
- The `hidden` circle connects via a dashed arrow to a box labeled `Decoder`.
- The `Decoder` points left toward the generated output text.
- Text shown around the diagram:
  - 資料通過Encoder產生出hidden state
  - 文本生成
  - 翻譯
  - 通過Decoder解析hidden state的內容

**Diagram/Figure (right):**

- A tall rounded rectangle labeled `Encoder` receives `Inputs` from below.
- The `Encoder` is connected to a tall rounded rectangle labeled `Decoder`.
- The `Decoder` receives `Outputs (Shifted right)` from below.
- The `Decoder` outputs `Output probabilities` upward.

source: https://huggingface.co/learn/nlp-course/zh-TW/chapter1/4?fw=pt

# Machine translation without attention

encoder最終隱藏狀態傳遞  
給decoder初始隱藏狀態

information about the  
entire sentence

RNN  
encoder

word-embeddings

機

器

翻

譯

Encoder

\<START>

machine

translation

\<END>

RNN  
decoder

Decoder

**Diagram/Figure description:** The figure shows an encoder-decoder RNN machine translation model without attention. The input sequence `機 器 翻 譯` is converted through `word-embeddings` and processed left-to-right by the `RNN encoder` through green hidden-state blocks. The final encoder hidden state is highlighted in yellow and labeled as containing `information about the entire sentence`. An orange arrow indicates that the `encoder最終隱藏狀態傳遞 給decoder初始隱藏狀態`, passing this final encoder state to initialize the decoder. The `RNN decoder` begins from `\<START>` and generates output tokens through magenta decoder blocks: `machine`, then `translation`, then `\<END>`, with arrows showing sequential recurrence and output generation.

# Machine translation with attention

每個隱藏狀態都會生成該詞的"key"跟”value”

> 這些 Key 和 Value 就是後續 Attention 機制  
> 會用來做「匹配」與「加權平均」的依據。

**Diagram description:** An RNN encoder processes the Chinese input characters 「機」「器」「翻」「譯」. Each character feeds upward into a shared **word-embeddings** layer, which then feeds into a sequence of hidden states \(h^1 \rightarrow \underline{h^2} \rightarrow h^3 \rightarrow h^4\). Each hidden state has a dashed upward arrow indicating that every hidden state generates the corresponding word’s “key” and “value”, which are later used by the Attention mechanism for matching and weighted averaging.

# Machine translation with attention

(decoder初始隱藏狀態)

\(z^0\)

Query

RNN  
encoder

\(h^1\) → \(h^2\) → \(h^3\) → \(h^4\)

word-embeddings

機　器　翻　譯

<START>

當前輸入需要聚焦的部分

(例如: 今天想吃的口味"辣的食物", 而Query  
就像你的需求或你正在找的特徵)

## Diagram/Figure description

The figure shows an RNN encoder processing the Chinese input sequence 機 → 器 → 翻 → 譯. Each input token is converted through a shared word-embeddings layer, then fed upward into the corresponding encoder hidden state \(h^1\), \(h^2\), \(h^3\), and \(h^4\). The hidden states are connected sequentially from left to right.

The final encoder hidden state \(h^4\) connects via an orange curved arrow to the decoder initial hidden state \(z^0\), indicating that the encoder output initializes or informs the decoder. A vertical `<START>` token also points upward into \(z^0\), representing the decoder start input. The decoder initial hidden state \(z^0\) is labeled as the Query, described as the part of the current input that needs focus.

# Machine translation with attention

## Diagram / figure

The figure shows a machine translation with attention setup:

- `(decoder初始隱藏狀態)` is shown above $z^0$.
- $z^0$ points left to a box labeled `match`.
- The RNN encoder produces hidden states $h^1$, $h^2$, $h^3$, $h^4$ in sequence, with arrows:
  - $h^1 \rightarrow h^2 \rightarrow h^3 \rightarrow h^4$
- $h^1$ points upward to `match`, indicating it is compared with $z^0$.
- Under the hidden states is a bar labeled `word-embeddings`.
- The input characters below the embeddings are:
  - `機`
  - `器`
  - `翻`
  - `譯`
- Each input character points upward into `word-embeddings`, which then points upward to the corresponding hidden state.
- The label `RNN encoder` appears to the left of the encoder hidden states.
- $h^1$ includes the label `(vector)`.

key　用來表示每個輸入元素的特徵

(就像菜單上每道菜的敘述，例如:  
宮保雞丁-"辣"、糖醋排骨-"甜"  
，key代表每道菜的特徵或標籤)

# Machine translation with attention

(scalar)

$\alpha_0^1$

(attention weights or similarity)

代表query向量和每個key向量之間的關聯度

(decoder初始隱藏狀態)

RNN  
encoder

$h^1$ → $h^2$ → $h^3$ → $h^4$

word-embeddings

機　器　翻　譯

$\text{Attention Weights} = \dfrac{QK^T}{\sqrt{d_k}}$

(Transformer version)

## Diagram / figure description

- The input sequence consists of four Chinese characters: 機, 器, 翻, 譯.
- Each character is mapped upward into a shared word-embeddings layer.
- The embeddings feed into an RNN encoder, producing hidden states $h^1$, $h^2$, $h^3$, and $h^4$.
- The hidden states are connected sequentially from left to right: $h^1 \rightarrow h^2 \rightarrow h^3 \rightarrow h^4$.
- The first encoder hidden state $h^1$ is sent upward into a box labeled `match`.
- The decoder initial hidden state $z^0$ is also sent into the `match` box from the right.
- The `match` box outputs the scalar attention weight $\alpha_0^1$ upward.
- This represents computing an attention weight or similarity score between the query vector and each key vector.

# Machine translation with attention

$z^0$

Query

**Diagram/Figure description:**

- The boxed $z^0$ is the **Query**.
- The input characters are shown as four cyan boxes: 機, 器, 翻, 譯.
- Each input character points upward into a gray bar labeled **word-embeddings**.
- The word embeddings point upward into four green hidden-state boxes labeled $h^1$, $h^2$, $h^3$, $h^4$.
- The hidden states are connected left-to-right with arrows: $h^1 \rightarrow h^2 \rightarrow h^3 \rightarrow h^4$.
- The left side labels the hidden states as **Key** and **Value**.
- Above the hidden states are attention weights: $\alpha_0^1$, $\alpha_0^2$, $\alpha_0^3$, $\alpha_0^4$.
- The attention mechanism compares the Query with each Key and uses the corresponding Value to compute the weighted sum.

Key  
Value

word-embeddings

機

器

翻

譯

$h^1$

$h^2$

$h^3$

$h^4$

$\alpha_0^1$

$\alpha_0^2$

$\alpha_0^3$

$\alpha_0^4$

Value向量代表輸入的實際內容  
(菜單上每道的實際內容，當選擇  
了一道菜，這道菜(宮保雞丁)就是  
Value)

$$
attention(Q,K,V)=\sum_{i=1}^{n} similarity(Q,K_i) * V_i
$$

# Machine translation with attention

Note: RNN的key和value為同樣的h, 後  
續的transformer才改良成 \(h_k, h_v\)

Query

Key  
Value

Value向量代表輸入的實際內容  
(菜單上每道的實際內容, 當選擇  
了一道菜, 這道菜(宮保雞丁)就是  
Value)

\[
attention(Q,K,V)=\sum_{i=1}^{n} similarity(Q,K_i) * V_i
\]

## Diagram description

- A boxed \(z^0\) is shown above the encoder states and labeled **Query**.
- Four input tokens appear in cyan boxes: **機**, **器**, **翻**, **譯**.
- Each token points upward into a gray bar labeled **word-embeddings**.
- The embeddings point upward into four green hidden-state boxes labeled \(h^1\), \(h^2\), \(h^3\), \(h^4\).
- The hidden states are connected left-to-right by arrows: \(h^1 \rightarrow h^2 \rightarrow h^3 \rightarrow h^4\).
- Above the hidden states are attention weights: \(\alpha_0^1\), \(\alpha_0^2\), \(\alpha_0^3\), \(\alpha_0^4\).
- The green hidden-state boxes are labeled collectively as **Key** and **Value**, indicating that in the RNN attention diagram the same hidden states \(h\) serve as both keys and values.
- The formula indicates that attention combines values \(V_i\) weighted by their similarity between the query \(Q\) and each key \(K_i\).

# Machine translation with attention

"黃金獵犬是一種非常聰明且友好的狗"

**當Query是"狗"這個詞，可能會關注到"黃金獵犬"和"友好"兩個詞:**

- **黃金獵犬**的key可能對應〝狗的一種〞的特徵，而Value則是具體的〝黃金獵犬〞這個含義
- **友好**的key可能對有〝狗的特性〞的特徵，而Value則是具體〝友好〞這個詞的含義

計算得到"黃金獵犬"和"友好"的權重後，注意力機制會用這些權重對Value進行加權平均，得到一個詞的上下文向量，這 \(c_i^0\) 向量捕捉"狗"這個詞在上下文中的含意

# Machine translation with attention

\[
attention(Q,K,V)=\sum_{i=1}^{n} similarity(Q,K_i) * V_i
\]

## Diagram/Figure

The figure shows machine translation with attention:

- Source tokens: 機, 器, 翻, 譯
- The source tokens feed upward into **word-embeddings**.
- **word-embeddings** feed into encoder hidden states:
  - \(h^1\)
  - \(h^2\)
  - \(h^3\)
  - \(h^4\)
- The hidden states are connected sequentially from \(h^1 \rightarrow h^2 \rightarrow h^3 \rightarrow h^4\).
- Each hidden state produces an attention score:
  - \(\alpha^1_0\)
  - \(\alpha^2_0\)
  - \(\alpha^3_0\)
  - \(\alpha^4_0\)
- The scores pass through **softmax** to produce normalized attention weights:
  - \(\bar{\alpha}^1_0\)
  - \(\bar{\alpha}^2_0\)
  - \(\bar{\alpha}^3_0\)
  - \(\bar{\alpha}^4_0\)
- Each normalized attention weight is multiplied by its corresponding hidden state value using multiplication nodes marked \(×\).
- The weighted values are summed using a plus node marked \(+\).
- The sum produces \(c^0\).
- The red label **value** points to the hidden-state values used in the weighted sum.
- On the decoder side, **<START>** feeds upward into \(z^0\), which feeds upward into \(c^0\), followed by **...**.
- An orange arrow connects \(h^4\) to \(z^0\).
- The right side is labeled **decoder**.

# Machine translation with attention

## Diagram

- Input tokens: 機 器 翻 譯
- A gray bar labeled `word-embeddings` maps the input tokens upward into encoder hidden states:
  - $h^1 \rightarrow h^2 \rightarrow h^3 \rightarrow h^4$
- The final encoder state $h^4$ connects to the decoder initial state $z^0$.
- Decoder states:
  - $z^0 \rightarrow z^1$
  - `<START>` feeds into $z^0$
  - `machine` feeds into $z^1$
- The label `decoder` appears beside the decoder states.
- Attention matching:
  - $h^1$ feeds upward into a box labeled `match`
  - $z^1$ connects by a curved arrow into `match`
  - `match` outputs the attention value $\alpha^1_1$ upward.

# Machine translation with attention

## Diagram / figure

- Encoder input tokens: 機, 器, 翻, 譯
- word-embeddings
- Encoder hidden states: $h^1$, $h^2$, $h^3$, $h^4$
- Attention scores into softmax:
  - $\alpha_1^1$
  - $\alpha_1^2$
  - $\alpha_1^3$
  - $\alpha_1^4$
- softmax
- Normalized attention weights:
  - $\bar{\alpha}_1^1$
  - $\bar{\alpha}_1^2$
  - $\bar{\alpha}_1^3$
  - $\bar{\alpha}_1^4$
- value
- Attention weight values shown in red:
  - $0$
  - $0$
  - $0.5$
  - $0.5$
- Each normalized attention weight is multiplied by its corresponding encoder hidden state using $\times$ nodes:
  - $\bar{\alpha}_1^1 \times h^1$
  - $\bar{\alpha}_1^2 \times h^2$
  - $\bar{\alpha}_1^3 \times h^3$
  - $\bar{\alpha}_1^4 \times h^4$
- The weighted values are summed with a $+$ node to produce the context vector $c^1$.
- The encoder hidden states are connected sequentially:
  - $h^1 \rightarrow h^2 \rightarrow h^3 \rightarrow h^4$
- An orange arrow connects $h^4$ to the decoder initial state $z^0$.
- decoder
- Decoder states:
  - $z^0$
  - $z^1$
- Decoder inputs:
  - `<START>` feeds into $z^0$
  - machine feeds into $z^1$
- Decoder state transition:
  - $z^0 \rightarrow z^1$
- Context vectors are associated with decoder steps:
  - $z^0 \uparrow c^0 \uparrow \ldots$
  - $z^1 \uparrow c^1 \uparrow \ldots$

# Machine translation with attention

## Diagram description

The slide illustrates machine translation with attention.

- An encoder processes the input sequence through word-embeddings:
  - 機
  - 器
  - 翻
  - 譯
- The word-embeddings feed into encoder hidden states:
  - $h^1 \rightarrow h^2 \rightarrow h^3 \rightarrow h^4$
- Each hidden state produces an attention score for decoder step 1:
  - $\alpha_1^1$
  - $\alpha_1^2$
  - $\alpha_1^3$
  - $\alpha_1^4$
- These scores pass through **softmax**, producing normalized attention weights:
  - $\bar{\alpha}_1^1$
  - $\bar{\alpha}_1^2$
  - $\bar{\alpha}_1^3$
  - $\bar{\alpha}_1^4$
- The displayed attention values are:
  - $0$
  - $0$
  - $0.5$
  - $0.5$
- Each normalized attention weight multiplies its corresponding hidden state value, and the products are summed to form the context vector:
  - $c^1$
- The decoder begins from $z^0$, connected from the encoder final state $h^4$, and proceeds:
  - $z^0 \rightarrow z^1 \rightarrow z^2$
- Decoder inputs:
  - `<START>` feeds into $z^0$
  - `machine` feeds into $z^1$
  - `translation` feeds into $z^2$
- Context vectors are associated with decoder states:
  - $c^0$ above $z^0$
  - $c^1$ above $z^1$
- The decoder continues with ellipses above the context outputs.

## Text in figure

value

softmax

word-embeddings

decoder

$h^1$

$h^2$

$h^3$

$h^4$

$\alpha_1^1$

$\alpha_1^2$

$\alpha_1^3$

$\alpha_1^4$

$\bar{\alpha}_1^1$

$\bar{\alpha}_1^2$

$\bar{\alpha}_1^3$

$\bar{\alpha}_1^4$

$0$

$0$

$0.5$

$0.5$

$c^1$

$z^0$

$z^1$

$z^2$

$c^0$

$c^1$

...

...

`<START>`

machine

translation

機

器

翻

譯

# Machine translation with attention

## Figure description

- Source input tokens: `機`, `器`, `翻`, `譯`
- A gray bar labeled `word-embeddings` maps the source tokens upward into encoder hidden states:
  - $h^1 \rightarrow h^2 \rightarrow h^3 \rightarrow h^4$
- The encoder hidden states are shown in green boxes and connected left-to-right by arrows.
- Above the encoder states, attention scores for decoder step 1 are shown:
  - $\alpha_1^1$, $\alpha_1^2$, $\alpha_1^3$, $\alpha_1^4$
- These scores enter a gray bar labeled `softmax`.
- The softmax outputs normalized attention weights:
  - $\bar{\alpha}_1^1$, $\bar{\alpha}_1^2$, $\bar{\alpha}_1^3$, $\bar{\alpha}_1^4$
- Red example attention values are shown beside the weights:
  - $0$, $0$, $0.5$, $0.5$
- Red label: `value`
- Each normalized attention weight is multiplied with its corresponding encoder value via circled multiplication nodes:
  - $\bar{\alpha}_1^1$ with $h^1$
  - $\bar{\alpha}_1^2$ with $h^2$
  - $\bar{\alpha}_1^3$ with $h^3$
  - $\bar{\alpha}_1^4$ with $h^4$
- The resulting weighted values are summed by a circled plus node to produce:
  - $c^1$

## Decoder side

- An orange arrow connects the encoder side to the first decoder state.
- Decoder hidden states are shown as boxes:
  - $z^0 \rightarrow z^1 \rightarrow z^2 \rightarrow \cdots$
- Inputs to decoder states:
  - `<START>` feeds into $z^0$
  - `machine` feeds into $z^1$
  - `translation` feeds into $z^2$
  - `<END>` appears to the right as a later decoder input/output marker
- Context vectors are associated above decoder states:
  - $c^0$ above $z^0$
  - $c^1$ above $z^1$
  - $c^2$ above $z^2$
- Ellipses `...` indicate continuation above the context vectors and after the decoder states.
- Label on the right: `decoder`

# Self-Attention

“Self-Attention 是一種讓模型在處理序列時，根據句子中其他詞的重要性來重新表示  
每個詞的方法。”

- **每個詞都會：**
  - 對自己和其他詞打分數（ attention weights）
  - 加權平均其他詞的資訊，來重建自己的表示
- **範例：輸入句子：The cat sat**

| Token | 建立表示時會看哪些詞？ |
|---|---|
| The | The, cat, sat |
| cat | The, cat, sat |
| sat | The, cat, sat |

# Self-Attention 計算流程

- 每個 token 都會變成三個向量:
  - Query (Q):我要注意什麼？
  - Key (K):我是什麼樣的資訊？
  - Value (V):我提供什麼資訊？
- 對每個 token, Attention 的輸出是:
  - $\mathrm{Attention}(Q, K, V) = \mathrm{softmax}(QK^T / \sqrt{d}) \times V$ （same as previous）

# Self-Attention

**Diagram:** The token **“The”** is contextualized into **vector(The)**. Curved arrows connect **The**, **cat**, and **sat** back toward **The**, with attention weights **0.2**, **0.5**, and **0.3**, indicating that the representation of **“The”** is recomputed using information from the whole sentence.

vector(The)

The  cat  sat

0.2  0.5  0.3

每個 token 都根據全句的語境來重新理解自己

# Multi-Head Attention

- 把「Self-Attention」這個動作做好幾次（多個 head），每次用不同的視角，然後再把結果組合起來。
  - 用不同角度去看一件事情，然後把觀察結果綜合起來做出更聰明的判斷。
- 單一的 self-attention 只能學到一種語意關係（例如主詞和動詞之間的連結），但語言中常常有很多不同層次的關係（例如語氣、句法結構、同義詞、地點關聯……）。
  - **Multi-head attention 讓模型可以「平行」學會多種關聯。**

# How

- 把輸入的向量 (例如每個詞的表示)  
  → 切成多個子空間 (例如從 512 維切成 8 組，每組 64 維)
- 每個 head:
  - 各自做一次 self-attention (使用自己的 Q, K, V)
  - 得到一組輸出表示
- 把所有 head 的輸出合併，再經過一層線性轉換來融合特徵 (並確保輸出與原始維度一致)

# Example

輸入句子:「The cat sat on the mat」

- head 1:學到「主詞與動詞」的關係
- head 2:學到「介系詞短語」的結構
- head 3:學到「the」通常修飾什麼詞
- …(總共有 8 或 12 個頭)

→ 最後把這些關係理解整合在一起，提升整體表示力

# Comparison

| 類型 | Query 來源 | Key / Value 來源 | 是否看自己 | 常見位置 | 說明 |
|---|---|---|---|---|---|
| Attention<br>(cross) | 一個序列 | 另一個序列 | X | Decoder | 輸出序列 (如翻譯結果) 根據輸入序列 (原文) 的資訊來決定該關注什麼 |
| Self-Attention | 序列自身 | 序列自身 | V | Encoder /<br>Decoder | 每個詞都看整個句子，包括自己，用來捕捉上下文關係 |
| Multi-Head<br>Attention | 多組分開的<br>Q/K/V (切分<br>後的向量) | 同上 (依附於 self<br>或 cross) | V/X | Encoder /<br>Decoder | 把 Attention 機制做多次，從多種角度學語意，提升模型表示力 (可用於 self 或 cross) |

# BERT

# 什麼是 BERT？

- BERT(Bidirectional Encoder Representations from Transformers）是 Google 所開發的預訓練語言模型。
- 它採用 Transformer Encoder 架構，搭配 Multi-Head Self-Attention，讓每個詞能根據整句話中的其他詞來重新建構自身表示，進而同時捕捉前後文的語意關係。
- BERT 使用 雙向語境理解 搭配 非監督式預訓練，可廣泛應用於各種自然語言任務，如文字標記、分類、問答等。

## 圖示說明

「純文字」中的詞「晴天」、「霹靂」經由「每一個詞轉為向量」轉換成 word embedding，例如：

- 晴天 → `[0, 1, 0, 0, 0]`
- 霹靂 → `[0, 0, 0, 1, 0]`

這些 word embedding（⋮）輸入到 BERT，BERT 產生 Contextual representation。

# BERT

由於BERT進行編碼標記時考慮了雙向性，較不容易出現同一個字在不同語境  
(context)下產生歧義的問題

# BERT

由於BERT進行編碼標記時考慮了雙向性，較不容易出現同一個字在不同語境  
(context)下產生歧義的問題

- 植物需要吸收「水分」
- 財務報表裡有「水分」

「水分」乍看之下是相同的詞，只是在不同的情境中具有不同的意義

# BERT

由於BERT進行編碼標記時考慮了雙向性，較不容易出現同一個字在不同語境  
(context)下產生歧義的問題

- 植物需要吸收「水分」 → 植物為了生長所需的水分
- 財務報表裡有「水分」 → 資訊上的不實與虛假

「水分」乍看之下是相同的詞，只是在不同的情境中具有不同的意義

# BERT

由於BERT進行編碼標記時考慮了雙向性，較不容易出現同一個字在不同語境  
(context)下產生歧義的問題

- 植物需要吸收「水分」 → 植物為了生長所需的水分
- 財務報表裡有「水分」 → 資訊上的不實與虛假

「水分」乍看之下是相同的詞，只是在不同的情境中具有不同的意義

word2vec:

不考慮上下文進行編碼的word2vec模型因word vector都一樣，因此無法分辨而產生歧異

BERT:

BERT因會考慮上下文進行編碼，故植物「水分」與財務報表「水分」的word vector不一樣，則不容易產生歧異

# BERT 如何做訓練？

- 在大型未標記的文字語料庫(非監督或半監督式學習)訓練語言模型 (pre-training)
- 針對特定的NLP任務微調此大型模型，利用此模型獲得的大型知識庫(fine-tuning)

**圖示說明：**  
圖中左側為 **Pre-training**：以未標記的句子 A 與句子 B 配對（Unlabeled Sentence A and B Pair）作為輸入，包含 Masked Sentence A 與 Masked Sentence B，經由 BERT 模型進行預訓練，任務包含 **NSP** 與 **Mask LM**。  
圖中右側為 **Fine-Tuning**：將預訓練後的 BERT 套用到不同 NLP 任務，例如 **MNLI**、**NER**、**SQuAD**。以問答任務為例，輸入 Question 與 Paragraph 的 Question Answer Pair，BERT 輸出 **Start/End Span** 以標示答案起訖位置。左右兩側以箭頭連接，表示由 pre-training 得到的 BERT 模型可進一步用於 fine-tuning。

source:https://arxiv.org/pdf/1810.04805.pdf

# BERT 如何做訓練？

預先訓練模型時，必須有充足的語料才能確保訓練的全面性，內容的豐富度是BERT  
模型判斷的關鍵因素之一。因此，BERT模型通常在非常大型的語料庫上進行預先訓  
練，例如 Google 使用 BookCorpus 的 800M 詞和英文維基百科 2500M 詞

預訓練後面會提到！

# BERT 主要模型

- BERT Base :12層編碼器區塊(Encoder blocks), 12個attention heads, 110M個參數
- BERT Large :24層編碼器區塊(Encoder blocks), 16個attention heads, 340M個參數

## 圖示說明

左側圖示為 **BERT_BASE**：一個標示為 **encoder** 的堆疊結構，內含多個 **block**，以數字標示從 1、2 到 12，表示共有 12 層 encoder blocks。

右側圖示為 **BERT_LARGE**：一個標示為 **encoder** 的堆疊結構，內含更多 **block**，以數字標示從 1、2、3、4 到 24，表示共有 24 層 encoder blocks。

# BERT 模型

Google開源了多個版本多個語言的預訓練模型於Github上

- BERT-Large, Uncased（ Whole Word Masking ）

  語言種類：英文

  網路結構：24-layer，1024-hidden，16-heads

  參數規模：340M

- BERT-Base, Uncased

  語言種類：英文

  網路結構：12-layer，768-hidden，12-heads

  參數規模：110M

- BERT-Large, Uncased

  語言種類：英文

  網路結構：24-layer，1024-hidden，16-heads

  參數規模：340M

- BERT-Large, Cased（ Whole Word Masking ）

  語言種類：英文

  網路結構：24-layer，1024-hidden，16-heads

  參數規模：340M

- BERT-Base, Cased

  語言種類：英文

  網路結構：12-layer，768-hidden，12-heads

  參數規模：110M

- BERT-Large, Cased

  語言種類：英文

  網路結構：24-layer，1024-hidden，16-heads

  參數規模：340M

- BERT-Base, Multilingual Cased

  語言種類：104種語言

  網路結構：12-layer，768-hidden，12-heads

  參數規模：110M

- BERT-Base, Multilingual Uncased

  語言種類：102種語言

  網路結構：12-layer，768-hidden，12-heads

  參數規模：110M

- BERT-Base, Chinese

  語言種類：中文

  網路結構：12-layer，768-hidden，12-heads

  參數規模：110M

# BERT 預處理

每個序列之首 → `[CLS]`

用於分開兩個句子的輸入 → `[SEP]`

| Input | `[CLS]` | my | dog | is | cute | `[SEP]` | he | likes | play | `##ing` | `[SEP]` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Token Embeddings | \(E_{[CLS]}\) | \(E_{\text{my}}\) | \(E_{\text{dog}}\) | \(E_{\text{is}}\) | \(E_{\text{cute}}\) | \(E_{[SEP]}\) | \(E_{\text{he}}\) | \(E_{\text{likes}}\) | \(E_{\text{play}}\) | \(E_{\#\#ing}\) | \(E_{[SEP]}\) |
| Segment Embeddings | \(E_A\) | \(E_A\) | \(E_A\) | \(E_A\) | \(E_A\) | \(E_A\) | \(E_B\) | \(E_B\) | \(E_B\) | \(E_B\) | \(E_B\) |
| Position Embeddings | \(E_0\) | \(E_1\) | \(E_2\) | \(E_3\) | \(E_4\) | \(E_5\) | \(E_6\) | \(E_7\) | \(E_8\) | \(E_9\) | \(E_{10}\) |

Diagram meaning: each input token representation is formed by adding its Token Embeddings, Segment Embeddings, and Position Embeddings. `[CLS]` is at the beginning of each sequence. `[SEP]` is used to separate the two sentence inputs. The first sentence segment uses \(E_A\), and the second sentence segment uses \(E_B\).

source:https://arxiv.org/pdf/1810.04805.pdf

# BERT 預處理

**Token Embeddings:** 最淺層嵌入, 代表詞語的淺層特徵, 沒有上下文脈絡

| Input | Token Embeddings | Segment Embeddings | Position Embeddings |
|---|---|---|---|
| [CLS] | \(E_{\text{[CLS]}}\) | \(E_A\) | \(E_0\) |
| my | \(E_{\text{my}}\) | \(E_A\) | \(E_1\) |
| dog | \(E_{\text{dog}}\) | \(E_A\) | \(E_2\) |
| is | \(E_{\text{is}}\) | \(E_A\) | \(E_3\) |
| cute | \(E_{\text{cute}}\) | \(E_A\) | \(E_4\) |
| [SEP] | \(E_{\text{[SEP]}}\) | \(E_A\) | \(E_5\) |
| he | \(E_{\text{he}}\) | \(E_B\) | \(E_6\) |
| likes | \(E_{\text{likes}}\) | \(E_B\) | \(E_7\) |
| play | \(E_{\text{play}}\) | \(E_B\) | \(E_8\) |
| ##ing | \(E_{\text{##ing}}\) | \(E_B\) | \(E_9\) |
| [SEP] | \(E_{\text{[SEP]}}\) | \(E_B\) | \(E_{10}\) |

**Diagram/Figure:** The figure shows BERT input representation construction. For each input token, its Token Embedding is added to its Segment Embedding and its Position Embedding. The first sequence `[CLS] my dog is cute [SEP]` uses segment embedding \(E_A\), and the second sequence `he likes play ##ing [SEP]` uses segment embedding \(E_B\). Position embeddings are assigned sequentially from \(E_0\) to \(E_{10}\).

source:https://arxiv.org/pdf/1810.04805.pdf

# BERT 預處理

**Segment Embeddings:**BERT 可以將句子以成對的方式作為任務的輸入(例如問答)第一個  
句子的每個詞對應相同的Segment Embedding，第二句的每個詞對應第二種

## 圖示說明

圖中展示 BERT 輸入表示由三種 Embeddings 相加組成：Token Embeddings、Segment Embeddings、Position Embeddings。  
輸入序列分成句子A與句子B：句子A的 token 使用相同的 Segment Embedding \(E_A\)，句子B的 token 使用相同的 Segment Embedding \(E_B\)。

| Input | `[CLS]` | `my` | `dog` | `is` | `cute` | `[SEP]` | `he` | `likes` | `play` | `##ing` | `[SEP]` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Token Embeddings | \(E_{[CLS]}\) | \(E_{my}\) | \(E_{dog}\) | \(E_{is}\) | \(E_{cute}\) | \(E_{[SEP]}\) | \(E_{he}\) | \(E_{likes}\) | \(E_{play}\) | \(E_{\#\#ing}\) | \(E_{[SEP]}\) |
| Segment Embeddings | \(E_A\) | \(E_A\) | \(E_A\) | \(E_A\) | \(E_A\) | \(E_A\) | \(E_B\) | \(E_B\) | \(E_B\) | \(E_B\) | \(E_B\) |
| Position Embeddings | \(E_0\) | \(E_1\) | \(E_2\) | \(E_3\) | \(E_4\) | \(E_5\) | \(E_6\) | \(E_7\) | \(E_8\) | \(E_9\) | \(E_{10}\) |

句子A：`[CLS] my dog is cute [SEP]`  
句子B：`he likes play ##ing [SEP]`

source:https://arxiv.org/pdf/1810.04805.pdf

# BERT 預處理

**Position Embeddings:**BERT 學習並使用位置嵌入來表示單詞在句子中的位置。添加這些功能  
是為了彌補 Transformer 的限制。與像 LSTM 這樣的 RNN 不同，BERT 同時對輸入進行平行計  
算，無法自然獲取順序或序列資訊，因此需要這種特殊手段來增強其性能。

**Diagram/Figure:** The figure shows that each input token representation is formed by adding three embeddings: Token Embeddings + Segment Embeddings + Position Embeddings. Segment Embeddings use \(E_A\) for the first sentence and \(E_B\) for the second sentence. Position Embeddings assign sequential positions \(E_0\) through \(E_{10}\) to the tokens.

\[
\text{Input representation}_i = \text{Token Embedding}_i + \text{Segment Embedding}_i + \text{Position Embedding}_i
\]

| Input | [CLS] | my | dog | is | cute | [SEP] | he | likes | play | ##ing | [SEP] |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Token Embeddings | \(E_{[CLS]}\) | \(E_{my}\) | \(E_{dog}\) | \(E_{is}\) | \(E_{cute}\) | \(E_{[SEP]}\) | \(E_{he}\) | \(E_{likes}\) | \(E_{play}\) | \(E_{\#\#ing}\) | \(E_{[SEP]}\) |
| Segment Embeddings | \(E_A\) | \(E_A\) | \(E_A\) | \(E_A\) | \(E_A\) | \(E_A\) | \(E_B\) | \(E_B\) | \(E_B\) | \(E_B\) | \(E_B\) |
| Position Embeddings | \(E_0\) | \(E_1\) | \(E_2\) | \(E_3\) | \(E_4\) | \(E_5\) | \(E_6\) | \(E_7\) | \(E_8\) | \(E_9\) | \(E_{10}\) |

source:https://arxiv.org/pdf/1810.04805.pdf

# BERT 預訓練

- **下一句子預測 (Next Sentence Prediction, NSP)**

- 針對理解句子之間關係的任務，問答系統很適合詮釋此種任務的例子

## 圖示說明

句子A與句子B作為輸入，以虛線箭頭送入 BERT；BERT 進行「判斷」，並輸出兩種可能關係：

- B是否料庫中A之後的下一句子
- 語料庫中的一句隨機句子

# BERT 預訓練

- **遮罩語言模型 (Masked Language Modeling, MLM)**
- 訓練一個語言模型來預測字詞時，從「序列本身」去預測缺失的單詞
- 因此，將某些字詞替換為[MASK]，在對模型進行訓練，使其預測這個缺失的詞

「今天的陽光溫暖而明媚，讓人感到無比愉悅。」

↓

「今天的[MASK]而明媚，讓人感到無比愉悅。」

*圖示說明：向下箭頭表示將原句中的部分字詞替換為 [MASK]，形成遮罩後的句子，讓模型根據序列本身預測缺失的詞。*

# BERT 微調

- 句子分類判斷, 如:情緒分析、文章分類
- 將想要分類的句子輸入BERT後，開頭加上代表分類符號[CLS], 再將該符號位置的輸出丟給線性分類器，由線性分類器去預測句子類別，只需微調BERT和訓練分類器

## Diagram / Figure

Diagram text:

- class
- Linear Classifier
- Trained from Scratch
- Input: single sentence,
  output: class
- Example:
  Sentiment analysis (our HW),
  Document Classification
- BERT → Fine-tune
- [CLS]
- \(W_1\)
- \(W_2\)
- \(W_3\)
- sentence
- Created with EverCam
  http://www.camdemy.com

Diagram meaning and relationships:

A single sentence is represented as tokens beginning with `[CLS]`, followed by \(W_1\), \(W_2\), \(W_3\). These inputs go into BERT, which is fine-tuned. The output corresponding to the `[CLS]` position is passed upward into a Linear Classifier. The Linear Classifier is trained from scratch and outputs the predicted class. The task is single-sentence input with class output, such as Sentiment analysis (our HW) or Document Classification.

# BERT 微調

- 將句子中每個詞分類:句子裡的每一個詞彙都要決定屬於哪個類別
- 輸入一個句子，再將每個詞彙的輸出都丟入線性分類器裡，讓其決定這個詞彙所屬類別

**Figure description:** A BERT token classification / slot filling architecture. The input is a single sentence represented as `[CLS] W1 W2 W3`, with the label `sentence` underneath. Each token is fed upward into a BERT block labeled `BERT`. The contextual outputs from BERT go upward into separate linear classifiers labeled `Linear Cls`, and each classifier outputs a `class`. The figure states: `Input: single sentence, output: class of each word`.

**Example: Slot filling:** The sentence shown is `arrive Taipei on November 2ⁿᵈ`, with word-level classes:

- `arrive` → `other`
- `Taipei` → `dest`
- `on` → `other`
- `November` → `time`
- `2ⁿᵈ` → `time`

Created with EverCam  
http://www.camdemy.com

# BERT 微調

- 判斷句子關係: 讓機器學習推論一句話，給機器一個前提或假設，根據前提或假設推論對錯
- 輸入兩個句子，句子相接處放入[SEP]再將開頭處的輸出丟給分類器判斷

## 圖示

圖中展示 BERT 用於兩句輸入的分類任務：

- Input: two sentences, output: class
- Example: Natural Language Inference
- Given a “premise”, determining whether a “hypothesis” is T/F/ unknown.
- 輸入序列為：`[CLS] W1 W2 [SEP] W3 W4 W5`
  - `W1 W2` 屬於 Sentence 1
  - `W3 W4 W5` 屬於 Sentence 2
  - `[SEP]` 放在兩個句子之間
- 整個序列輸入 BERT。
- BERT 對每個 token 產生輸出表示。
- `[CLS]` 位置的輸出送入 `Linear Classifier`。
- `Linear Classifier` 輸出 `Class`。

圖中文字：

- Class
- Linear Classifier
- BERT
- [CLS]
- W1
- W2
- [SEP]
- W3
- W4
- W5
- Sentence 1
- Sentence 2
- Created with EverCam
- http://www.camdemy.com

# BERT 的問題

- BERT在預訓練時會出現[MASK]，而在微調中並不會出現，因此造成預訓練與微調不匹配
- 句子長度限制為512，超過長度的文本只能截斷
- BERT的訓練數據中只有15%的標記被預測，被預測的詞有80%被mask、10%替換成隨機詞、10%保持不變，導致模型需要更多訓練步驟來收斂

## 圖示

The quick brown fox jumps over the lazy dog

↓  
挑出序列15%固定的詞被選為是否 mask

The quick <span style="color:red">brown</span> fox jumps over the <span style="color:red">lazy</span> dog

↓  
“brown” -> [mask] (80%機率)  
“lazy” -> crazy (10%機率)

The quick [mask] fox jumps over the crazy dog

**圖示說明：** 原始句子先從序列中挑出15%的詞作為預測對象（圖中以紅色標示 brown 和 lazy），接著依機率將被選中的詞替換：brown 被替換為 [mask]，lazy 被替換為隨機詞 crazy，形成最終輸入句子。

# BERT

**Diagram:** BERT is the central model. Arrows extend from BERT to related models with dates and notes:

| From | To | Date | Note |
|---|---|---|---|
| BERT | RoBERTa | 2019/07 | 更大更強 |
| BERT | ELECTRA | 2020/03 | 對抗學習、訓練高效 |
| BERT | TinyBERT | 2019/9 | 模型更小、推理更快 |
| BERT | XLNet | 2019/06 | 結合Permutation Language Model 和 Transformer XL 機制 |
| BERT | ALBERT | 2019/09 | 矩陣分解、參數共享、內存更小 |

# XLNet

- XLNet引入了<span style="color:red">排列語言模型(Permutation Language Model)</span>，通過對輸入序列進行不同的排列組合，生成多種可能的排列順序，在訓練時能夠同時考慮詞的上下文訊息
  - 與BERT不同，BERT透過MLM捕捉上下文，而XLNet通過對輸入序列的排列組合進行訓練，避免了MLM的侷限性
  - 例如：輸入句子"A B C D"，XLNet會考慮"A C D B"、”B C A D”、"B D C A"等24種排列

Input: "The cat sat on the mat"

**MLM:**

"The cat [mask] on the mat"

**PLM:**

Permute to “sat cat mat The on the”  
Predict "sat" | Context: {}  
Predict "cat" | Context: {sat}  
Predict "mat" | Context: {sat cat}  
Predict "The" | Context: {sat cat mat}  
Predict "on" | Context: {sat cat mat The}  
Predict "the" | Context: {sat cat mat The on}

**Diagram description:** The figure contrasts MLM and PLM. MLM masks a word in the original sentence and predicts it from surrounding context, while PLM permutes the input order and predicts each token sequentially using the tokens that appeared earlier in the permutation as context.

# XLNet

- XLNet引入了排列語言模型(Permutation Language Model), 通過對輸入序列進行不同的  
  排列組合，生成多種可能的排列順序，在訓練時能夠同時考慮詞的上下文訊息
  - 與BERT不同，BERT透過MLM捕捉上下文，而XLNet通過對輸入序列的排列組合進行訓練，避  
    免了MLM的侷限性
  - 例如: 輸入句子"A B C D"，XLNet會考慮"A C D B"、”B C A D”、"B D C A"等24種排列

Input: "The cat sat on the mat"

**MLM:**

"The

**PLM:**

Permute to “sat cat mat The on the”  
Predict "sat" | Context: {}  
Predict "cat" | Context: {sat}  
Predict "mat" | Context: {sat cat}  
Predict "The" | Context: {sat cat mat}  
Predict "on" | Context: {sat cat mat The}  
Predict "the" | Context: {sat cat mat The on}

> Note: 並不是真的改變字的順序，  
> 而是透過Attention Mask 來模擬排  
> 列組合的預測順序 (skip)

**Diagram/Figure description:** The slide contrasts MLM and PLM for the input sentence "The cat sat on the mat". The PLM side shows a permuted prediction order, “sat cat mat The on the”, where each token is predicted sequentially using only the previously predicted tokens as context. A note explains that XLNet does not actually change the word order, but uses an Attention Mask to simulate the prediction order of different permutations.

# XLNet

- 利用<span style="color:red">Transformer-XL機制</span>解決傳統Transformer模型處理長序列時的侷限性
  - 傳統Transformer是一次性處理一段固定長度的文本，例如 512個字，然後在處理下一段 512個字  
    ，這兩段之間沒有連續性（Context Fragmentation）

**圖示說明：** 右下方圖示標題為「Transformer (Training)」。圖中將序列分成兩段：Segment 1（\(x_1, x_2, x_3, x_4\)）與 Segment 2（\(x_5, x_6, x_7, x_8\)），中間以箭頭表示從第一段到第二段的處理流程。每個 segment 內有多層節點與斜線連結，表示 Transformer 在訓練時於各自固定長度片段內進行注意力連結；兩個 segment 之間沒有跨段連結，表達段落之間缺乏連續性。

# XLNet

- 利用Transformer-XL機制解決傳統Transformer在
  - 傳統Transformer是一次性處理一段固定長度的文本
  ，這兩段之間沒有連續性（Context Fragmentation）
- Transformer-XL的改進
  - **分段遞迴機制 (Segment-level Recurrence Mechanism)**：將文章分成多個片段，在處理第二段
  時，模型還會處理前一段產生的隱藏狀態(記憶)，因此第二段的輸出將會考慮上一段的內容

## 圖示說明：Transformer-XL (Training)

圖中展示 Transformer-XL 在訓練時的片段級遞迴關係。序列位置從 \(x_1\) 到 \(x_{12}\) 分成多個 segment。虛線框中的 \(x_5\) 到 \(x_8\) 表示前一段的 hidden states，標示為 **Fixed (No Grad)**，代表這些記憶會被保留但不進行梯度更新。右側 \(x_9\) 到 \(x_{12}\) 標示為 **New Segment**，表示目前正在訓練的新片段。綠色連線表示新片段會 attend 到前一段保留下來的記憶；灰色連線表示 segment 內部或相鄰位置之間的 attention 關係。

# XLNet

- 利用<span style="color:red">Transformer-XL機制</span>解決傳統Transformer模型處理長序列時的侷限性
  - 傳統Transformer是一次性處理一段固定長度的文本，例如 512個字，然後在處理下一段 512個字  
    ，這兩段之間沒有連續性（Context Fragmentation）
- Transformer-XL的改進
  - **分段遞迴機制 (Segment-level Recurrence Mechanism)**: 將文章分成多個片段，在處理第二段  
    時，模型還會處理前一段產生的隱藏狀態(記憶)，因此第二段的輸出將會考慮上一段的內容
  - **相對位置編碼 (Relative Positional Encoding)**: 每個詞的位置是相對於其他詞的位置，與傳統  
    的絕對位置編碼不同

```text
“我 喜歡 吃 蘋果”                         句1:我 喜歡 吃 蘋果      → "喜歡" 是位置2, "蘋果" 是位置4
"我"與"喜歡"的距離是+1                    句2:我 討厭 吃 蘋果      → "討厭" 是位置2, "蘋果" 是位置4
"我"與"蘋果"的距離是+3                    絕對位置編碼
        .                                  → 模型只能記住「第 2個字 + 第4個字」的關係， what if 我 超級 無敵 喜歡 吃 蘋果？
        .                                  相對位置編碼
        .                                  → 無論哪一句，「動詞」與「蘋果」的距離都是 +2
        .                                  → 模型能學到「動詞影響後面第 2個詞」，而非只記住在第幾位上出現
                                           → 可類推至「其實 我 超級 愛 吃 鳳梨」這樣的新句子
```

圖示描述：左側以「我 喜歡 吃 蘋果」說明相對距離，例如「我」與「喜歡」距離為 +1，「我」與「蘋果」距離為 +3；右側比較絕對位置編碼與相對位置編碼，指出絕對位置編碼記住詞在第幾位的關係，而相對位置編碼學習詞之間的相對距離，因此可泛化到新句子。

# XLNet

- 利用Transformer-XL機制解決傳統Transformer的問題
  - 傳統Transformer是一次性處理一段固定長度的文本，如果句子被分成兩段，這兩段之間沒有連續性（Context Fragmentation）

> 補充：分段遞迴機制必須搭配相對位置編碼，否則  
> 新舊 segment 的絕對位置會產生衝突

- Transformer-XL的改進
  - **分段遞迴機制 (Segment-level Recurrence Mechanism)**: 將文章分成多個片段，在處理第二段時，模型還會處理前一段產生的隱藏狀態(記憶)，因此第二段的輸出將會考慮上一段的內容
  - **相對位置編碼 (Relative Positional Encoding)**: 每個詞的位置是相對於其他詞的位置，與傳統的絕對位置編碼不同

“我 喜歡 吃 蘋果”  
"我"與"喜歡"的距離是+1  
"我"與"蘋果"的距離是+3  

.  
.  
.  

句1: 我 喜歡 吃 蘋果　　　　→ "喜歡" 是位置2, "蘋果" 是位置4  
句2: 我 討厭 吃 蘋果　　　　→ "討厭" 是位置2, "蘋果" 是位置4  

**絕對位置編碼**  
→ 模型只能記住「第 2個字 + 第4個字」的關係，what if 我 超級 無敵 喜歡 吃 蘋果？  

**相對位置編碼**  
→ 無論哪一句，「動詞」與「蘋果」的距離都是 +2  
→ 模型能學到「動詞影響後面第 2個詞」，而非只記住在第幾位上出現  
→ 可類推至「其實 我 超級 愛 吃 鳳梨」這樣的新句子

# RoBERTa

在BERT的基礎上做了調整

- 增大batch-size、訓練數據更多（提升模型收斂穩定度與最終表現）
- static masking 換成 dynamic masking
  - **static masking**:BERT在處理訓練數據時，會先處理好哪些位置要被 mask，因此訓練時同一句話被mask的位置跟方式都是一樣的
  - **dynamic masking**:RoBERTa在訓練時才進行實時mask，所以訓練時同一句話 mask的位置跟方式都是隨機的，存在多種可能
- 移除NSP任務(下一句子預測)，RoBERTa發現NSP對模型的效果沒有提升，只保留MLM

# 分詞的優化

- 在開始訓練之前，模型需要先建立Tokenizer / Vocabulary將文字轉成ID
- 將Character-level 分詞 (WordPiece)換成 Byte-level BPE(Byte Pair Encoding)
  - 在 BERT 的分詞過程中，單詞 "word" 會先被拆分為 "w"、"o"、"r"、"d" 這四個字元。接著，分詞器會根據語料中最常見的相鄰字元對 (例如 "wo")進行合併，變成 "wo"、"r"、"d"。這個合併過程會重複進行，直到達到預設的合併次數或詞彙表大小。最終， "word" 可能會被切分為 "wo" 和 "rd" 這樣的子詞。即使如此，所有最基本的字元 (如 "w"、"o"、"r"、"d")也會保留在詞彙表中，以保證能處理任何新詞。
  - 在RoBERTa中會以UTF-8編碼儲存，例如漢字"哭"的UTF-8編碼是三個字節 (0xE5,0X93,0xAD), 再進行Byte-level BPE時，每個字節被視為 1個token:"E5","93",”AD”，在訓練的BPE詞彙表查詢這三個序列是否常出現在數據集，並決定是否合併

# Character-level BPE VS Byte-level BPE

- Character-level BPE 的缺點:
  - 遇到未見過的字元 (特別是 Unicode 字元) 時, 無法處理, 且詞彙表需要包含所有可能的字元,  
    導致詞彙表膨脹。
- Byte-level BPE 的優點:
  - 因為是以 byte 為單位, 所以可以處理 Unicode 中任意語言, 包含 emoji、罕見字等
  - 詞彙表只需包含 256 個基本 bytes, 節省空間, 且不會出現無法編碼的情況