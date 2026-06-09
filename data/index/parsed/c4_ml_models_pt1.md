# Machine Learning Models

# Where Do ML-Based Models Fit in NLP?

**Which model type should be used  
for text analysis?**

## Vector-based models

Convert text into numerical  
representations for further  
processing.

## Probabilistic models

Use statistical probability to  
predict outcomes.

## ML-based models

Learn patterns from data for  
classification and clustering.

## Diagram/Figure description

A central thinking figure asks which model type should be used for text analysis. Three thought bubbles surround it, representing three options:

- Left: **Vector-based models**, illustrated with a document-like icon containing dots, indicating converting text into numerical representations.
- Right: **Probabilistic models**, illustrated with a dice-like probability icon, indicating statistical prediction.
- Bottom: **ML-based models**, illustrated with a network/group icon, indicating learning patterns from data for classification and clustering.

# Vector-Based Models: Feature Representation

- Convert text into numerical form, <span style="color:red">but they do not predict!</span>

Examples:

- **Bag of Words (BoW)** – Word occurrence
- **TF-IDF** – Word importance
- **Word Embeddings** – Word2Vec, GloVe

Used as input for ML models!

# Probabilistic Models: Learning with Probability

- Predict outcomes <span style="color:red">based on probability distributions</span>

Examples:

- **Naïve Bayes:** \(P(\text{Class} \mid \text{Words})\) for text classification
- **Markov Models:** Probabilities of word sequences (e.g., POS tagging)

Can be <span style="color:red">standalone</span> or <span style="color:red">combined with ML!</span>

# Machine Learning-Based Models: Learning from Data

- Learn patterns from labeled/unlabeled data
- Supervised Learning (e.g., Logistic Regression, SVM, Decision Trees)
- Unsupervised Learning (e.g., K-Means Clustering)
- Require <span style="color:red">vectorized input</span> (from Vector-based models) for NLP tasks

# Applications

| Supervised | Unsupervised |
|---|---|
| Spam detection | Topic modeling |
| Sentiment analysis | Latent semantic analysis |
|  | Text summarization |

# Spam Detection

# How Do We Detect Spam?

Three key steps:

1. Convert text into numerical features (Vectorization)
2. Train a model to classify spam vs. ham (ML-based model)
3. Evaluate model accuracy (Precision, Recall, F1-score)

We need a dataset of labeled emails to train the model!

# Step 1: Converting Emails into Features

Text must be converted into numerical format before ML can process it!

- Bag of Words (BoW) – Count how often words appear
- TF-IDF (Term Frequency-Inverse Document Frequency) – Weigh important  
  words
- Word Embeddings (Word2Vec, GloVe) – Capture meaning and context

Example:

| Email Content | TF-IDF Features |
|---|---|
| "Win a free iPhone now!" | Free: 0.8, iPhone: 0.7, Win: 0.9 |
| "Meeting at 10 AM tomorrow" | Meeting: 0.6, Tomorrow: 0.7, 10 AM: 0.8 |

# Step 2: Training Machine Learning Models

We can use different ML models to classify emails:

| Model | Pros | Cons |
|---|---|---|
| Naïve Bayes | Fast & works well on small data | Assumes words are independent |
| Logistic Regression | Simple & interpretable | Struggles with complex text |
| Support Vector Machine (SVM) | Great for text classification | Slow with large datasets |
| Random Forest | Robust & handles noisy data | Requires more computation |

# Step 3: Evaluating Model Performance

How do we measure if our model works well?

- Accuracy – Correct predictions / Total predictions
- Precision – How many predicted spam emails are actually spam?
- Recall – How many actual spam emails were detected?
- F1-Score – Balance between Precision & Recall
- Confusion Matrix

|  | Predicted Spam | Predicted Ham |
|---|---|---|
| Actual Spam | ✅ 50 | ❌ 10 |
| Actual Ham | ❌ 5 | ✅ 100 |

# Sentiment Analysis

# Sentiment Analysis

> "I can't believe I wasted 2  
> hours of my life on that film."

Negative

Neutral

> "Wow, that was a really great film."

Positive

**Diagram/Figure:** The slide illustrates sentiment analysis with three facial icons representing sentiment categories: a red unhappy face labeled **Negative**, a yellow neutral face labeled **Neutral**, and a green happy face labeled **Positive**. A negative review speech bubble points to the **Negative** icon, while a positive review speech bubble points to the **Positive** icon, showing how text can be classified by sentiment.

# Classification or Regression

- Typically we consider sentiment analysis to be a classification task
- When we have multiple classes, we can also treat it as regression task
- Ex: 4.2 positive, -3.5 negetive

**Figure:** A visual sentiment/rating scale showing rows of five-star ratings decreasing from 5 yellow stars to 1 yellow star with the remaining stars dark, paired with five face icons ranging from very negative/angry (red) to very positive/happy (green). The figure conveys that sentiment can be represented as ordered classes or as a continuous regression-style score.

# Types of Sentiment Analysis

- **Binary Sentiment Analysis:** Classifies text as positive or negative.
- **Ternary Sentiment Analysis:** Categorizes text as positive, negative, or neutral.
- **Fine-Grained Sentiment Analysis:** Uses a scale (e.g., very positive, positive, neutral, negative, very negative).
- **Aspect-Based Sentiment Analysis:** Identifies sentiment towards <span style="color:red">specific aspects of a product or service.</span>
  - For example, in a restaurant review like 'The food was amazing, but the service was slow,' aspect-based sentiment analysis would classify 'food' as positive and 'service' as negative.
- **Emotion Detection:** Recognizes emotions such as happiness, anger, sadness, etc.

# Approaches to Sentiment Analysis

- Lexicon-Based Approach:
  - Uses predefined word lists (sentiment lexicons) to determine sentiment.
    - Ex: 讚、喜歡、優秀, 各得 +1 分;爛、討厭、雷, 各得 -1 分
  - 除此之外, 也會針對否定詞、程度副詞、標點符號等另行處理
    - 不好 → -1*1
    - 好吃 → +1; 超級好吃 → +1.5; 稍微好吃 → +0.5
    - 誇張 vs 誇張！！！
  - Example approach: SentiWordNet, AFINN.
- Machine Learning-Based Approach:
  - Uses algorithms such as Naive Bayes, Support Vector Machines (SVM), and Deep Learning.
  - Requires training data labeled with sentiment.

# Sentiment Analysis Tools & Libraries

- VADER
  - Suitable for social media sentiment analysis. It is rule-based and works well with short, informal text such as tweets.
  - Ex: LOL, WTF
- TextBlob
  - Simple API for NLP tasks, including sentiment analysis. Good for beginners and lightweight applications.
- BERT & Transformer Models
  - State-of-the-art NLP models that improve sentiment classification by understanding contextual meaning in text.

# Challenges in Sentiment Analysis

- **Sarcasm & Irony**
  - ex: 老師講的笑話真的太好笑了，不用開冷氣也不會熱
- **Context Understanding**
  - ex: 我沒事
  - Context 1 (陌生人) → postive or neutral
  - Context 2 (另一半) → negative !!!
- **Domain Dependency**
  - 劇情發展完全不可預測！ vs 系統運作狀態不可預測
- **Scope of Negation**
  - ex: 我不覺得這部電影的特效做得很好, 但配樂還算可以。
  - “不”的影響範圍到底有多遠？

# Real-World Applications of Sentiment Analysis

- **Customer Feedback Analysis:** Understanding user satisfaction in reviews.
- **Social Media Monitoring:** Identifying public sentiment about brands and events.
- **Political Analysis:** Assessing public opinion on political issues.
- **Stock Market Predictions:** Analyzing sentiment from financial news and tweets.
- **Healthcare & Mental Health Monitoring:** Detecting signs of depression or stress through text analysis.

# Text Summarization

# Text Summarization

- We do this all the time
  - Scientific paper abstracts
  - Executive summaries in professional documents
  - ...
- Summary also helps AI

**Diagram/Figure:** A document labeled “Document” with multiple highlighted lines is shown on the left. An arrow points from it to a shorter document labeled “Summary” on the right, conveying that text summarization transforms a longer document into a shorter summary retaining selected key information.

# Why Text Summarization Helps AI

- “Summarization” is an aspect of “learning”
- E.g. In everyday conversations, we often paraphrase (i.e. summarize) what people tell you
- Summarization is a way for learning systems to demonstrate understanding of a concept
- Summarization can also be used for reducing the size of tokens passing to models (e.g. ChatGPT)

# 2 Types of Summarization

**Extractive Summarization:**

- Selects key sentences or phrases directly from the original text.
- Example: News summarization by picking the most relevant sentences.
- Tools: TextRank, LexRank, Sumy, RAKE.

**Abstractive Summarization:**

- Generates a summary using new words while retaining the original meaning.
- Example: Human-like rewriting of a paragraph in a more concise form.
- Tools: BERTSUM, Pegasus, T5, GPT-based models.

**Diagram/Figure:** Two document icons compare summarization types. The left document is labeled “Extractive” and shows highlighted lines within the document, indicating that selected sentences or phrases are taken directly from the original text. The right document is labeled “Abstractive” and has an arrow pointing to two short green summary snippets, indicating that the original content is rewritten into new summarized wording.

# Text Summarization with TF-IDF

- Split the document into sentences
- Score each sentence
- Rank each sentence by those scores
- Summary = top scoring sentences

# Sentence Splitting & TF-IDF

- Sentence tokenization (splitting document into sentences) can be done with NLTK (nltk.sent_tokenize(your_text))
- Built TF-IDF matrix, treating each sentence as if they were documents
- In previous example, the TF-IDF matrix was document x terms
- In this case, it will be sentences x terms

|  | incubation | mean | of | period | risk | the | transmission |
|---|---|---|---|---|---|---|---|
| Sentence1 | high | medium | o | medium | o | o | o |
| Sentence2 | o | medium | o | medium | o | o | o |
| Sentence3 | o | o | o | o | medium | o | high |

# Scoring Each Sentence

- $\text{Score} = \text{Average}(\text{non-zero TF-IDF values})$
- E.g. if row = $[0, 1, 0, 0, 0, 2, 3, 0, 0, 0]$, then score = $\text{avg}(1, 2, 3) = 2$
- Why mean and not sum?
- The sum would be biased toward longer sentences

# What to Do with the Scores

- Idea: sort the scores, pick the sentences with the highest scores
- How? There are multiple options: choose what works best for you
- Simple: top N sentences (e.g. top 5, top 10)
- Also simple: top N words, top N characters (e.g. if limited by space)
- Top X% of sentences, top X% of words / characters

# TextRank

- Split the document into sentences
- Preprocessing
- <span style="color:red">Score each sentence</span>
- Rank each sentence by those scores
- Summary = top scoring sentences

- TextRank is an alternative method of scoring each sentence
- All the other steps remain

# PageRank

- TextRank is based on PageRank, Google’s state-of-the-art search ranking method ~20 years ago which beat all competitors and led to Google becoming one of the largest tech companies in the world
- The Internet is made up of web pages, each of which can potentially be returned as a search result
- We would like to compute a <span style="color:red">score</span> for each webpage

**Figure:** Google PageRank logo with a horizontal progress/rank bar underneath, illustrating the concept of assigning a PageRank score to webpages.

# The Secret to PageRank

- The secret to scoring each web page is the <span style="color:red">random walk</span>
- Starting from an arbitrary page, randomly select a link, go to that page, repeat forever…
- After a “long time”, the probability of landing on any particular page is <span style="color:red">constant (convergence)</span>
- Doesn’t matter where you start!

**Diagram/Figure:** A directed web-link graph visualizes PageRank as a random walk. Each circular node is a web page, and its size corresponds to its long-run landing probability/PageRank score. Arrows represent links that the random walker may follow. The graph includes labeled pages **A 3.3%**, **B 38.4%**, **C 34.3%**, **D 3.9%**, **E 8.1%**, and **F 3.9%**, plus five small peripheral pages each labeled **1.6%**. Page **B** is the largest and most central node, receiving many incoming links; **C** is also large and linked bidirectionally with **B**. Other pages and peripheral nodes point into pages such as **B** and **E**, illustrating how link structure determines the converged random-walk probabilities.

# PageRank Intuition

- A web page with <span style="color:red">more incoming links</span> is more <span style="color:red">popular</span>, and will have a higher chance of being landed on
- A web page few or no links is not popular, so the probability of going there is smaller
- These probabilities are the PageRank scores

## Diagram/Figure

The figure shows a directed web graph where each circular node represents a web page and each arrow represents a link from one page to another. The size of each node corresponds to its PageRank score/probability.

Nodes shown:

| Node | PageRank score |
|---|---:|
| A | 3.3% |
| B | 38.4% |
| C | 34.3% |
| D | 3.9% |
| E | 8.1% |
| F | 3.9% |
| unlabeled purple nodes | 1.6% each |

Relationships conveyed:

- B is the largest node and has many incoming links, so it has the highest PageRank score: 38.4%.
- C is also large and has a high PageRank score: 34.3%.
- B and C link to each other.
- E and F link to each other.
- Several smaller purple nodes with 1.6% PageRank link into more central nodes such as B and E.
- D links upward to A and also toward B.
- The diagram conveys that pages receiving more links, especially from other pages in the graph, receive higher PageRank probabilities.

https://reurl.cc/ezxerm

# Applying PageRank to TextRank

- There are two TextRank methods: <span style="color:red">symmetric</span> and <span style="color:red">asymmetric</span>
- Symmetric is suitable for sentence extraction as we evaluate the similarity  
  between two sentences, there is no direction
- Asymmetric is suitable for keyword extraction because the word order matters
  - Ex: “人工”後面常常接“智慧”, 但“智慧”後面可能常接的是“手錶”、“財產”

# Symmetric TextRank

The symmetric TextRank algorithm:

$$
S(V_i) = (1 - d) + d \times \sum_{V_j \in N(V_i)} \frac{w_{ij}}{\sum_{V_k \in N(V_j)} w_{jk}} S(V_j)
$$

- $S(V_i)$: 句子 i 目前的重要性分數 (Score)
- d : 阻尼係數, 通常設為 0.85。代表15% 的機率會隨機跳到其他句子, 避免分數流動卡死在某個封閉的小圈圈裡
- $N(V_i)$: 與句子 i 相連的所有鄰居節點的集合
- $w_{ij}$: 句子 i 與句子 j 之間的相似度權重
- $\sum V_k \in N(V_j) w_{jk}$ : 這是句子 j 跟它所有鄰居連線的權重總和。把它放在分母，是為了計算出一個分配比例

# Symmetric TextRank

> 假設我們有三個句子 (斷詞版)
> - S1: 機器 學習 很 有趣
> - S2: 機器 學習 很 困難
> - S3: 深度 學習 解決 困難
> 假設所有句子的起始分數都是 1

## Step 1: 計算句子間的相似度

- Can use cooccurence counting or cosine similarity
- S1 與 S2: 共有「機器、學習、很」3 個詞 → \(w_{12}=w_{21}=3\)
- S1 與 S3: 共有「學習」1 個詞 → \(w_{13}=w_{31}=1\)
- S2 與 S3: 共有「學習、困難」2 個詞 → \(w_{23}=w_{32}=2\)

# Symmetric TextRank

## Step 2: 計算分母

- S1 的總權重 \((W_1) = w_{12} + w_{13} = 3 + 1 = 4\)
- S2 的總權重 \((W_2) = w_{21} + w_{23} = 3 + 2 = 5\)
- S3 的總權重 \((W_3) = w_{31} + w_{32} = 1 + 2 = 3\)

> 假設我們有三個句子（斷詞版）
> - S1: 機器 學習 很 有趣
> - S2: 機器 學習 很 困難
> - S3: 深度 學習 解決 困難
>
> 假設所有句子的起始分數都是 1
> - \(w12 = w21 = 3\)
> - \(w13 = w31 = 1\)
> - \(w23 = w32 = 2\)

# Symmetric TextRank

## Step 3: 迭代開始

- Update S1
  - 從 S2 那邊可以分到 \(\frac{3}{5}\) 的比例
  - 從 S3 那邊可以分到 \(\frac{1}{3}\) 的比例
  - \(S(S_1) = (1 - 0.85) + 0.85 * \left(\frac{3}{5} * 1 + \frac{1}{3} * 1\right) = 0.943\)

---

假設我們有三個句子（斷詞版）

- S1: 機器 學習 很 有趣
- S2: 機器 學習 很 困難
- S3: 深度 學習 解決 困難

假設所有句子的起始分數都是  
1

- \(w_{12} = w_{21} = 3\)
- \(w_{13} = w_{31} = 1\)
- \(w_{23} = w_{32} = 2\)
- \(W_1 = 4\)
- \(W_2 = 5\)
- \(W_3 = 3\)

---

\[
S(V_i) = (1 - d) + d \times \sum \left(\frac{\text{彼此的權重}}{\text{對方的總權重}} \times \text{對方的分數}\right)
\]

公式圖示描述：每個節點 \(V_i\) 的分數由阻尼項 \((1-d)\) 加上所有相鄰節點貢獻的總和組成；每個相鄰節點的貢獻為「彼此的權重 / 對方的總權重」乘上「對方的分數」。

# Symmetric TextRank

## Step 3: 迭代開始

- Update S2
  - 從 S1 那邊可以分到 ¾ 的比例
  - 從 S3 那邊可以分到 ⅔ 的比例
  - \(S(S_2) = (1 - 0.85) + 0.85 * (¾ * 1 + ⅔ * 1) = 1.354\)

## 假設我們有三個句子（斷詞版）

- S1: 機器 學習 很 有趣
- S2: 機器 學習 很 困難
- S3: 深度 學習 解決 困難

假設所有句子的起始分數都是  
1

- \(w_{12} = w_{21} = 3\)
- \(w_{13} = w_{31} = 1\)
- \(w_{23} = w_{32} = 2\)
- \(W_1 = 4\)
- \(W_2 = 5\)
- \(W_3 = 3\)

## 公式

\[
S(V_i) = (1 - d) + d \times \sum \left(\frac{\text{彼此的權重}}{\text{對方的總權重}} \times \text{對方的分數}\right)
\]

## 圖示說明

右上角灰色圓角框列出三個斷詞後的句子 S1、S2、S3，並假設所有句子的起始分數都是 1。框中同時列出句子之間的對稱權重 \(w_{ij} = w_{ji}\)，以及每個句子的總權重 \(W_1\)、\(W_2\)、\(W_3\)。底部黑色區塊呈現 Symmetric TextRank 的更新公式，表示某句子的分數由阻尼係數 \(d\)、相鄰句子彼此的權重、對方的總權重與對方的分數共同決定。

# Symmetric TextRank

## Step 3: 迭代開始

- Update S3
  - 從 S1 那邊可以分到 ¼ 的比例
  - 從 S2 那邊可以分到 ⅖ 的比例
  - $S(S_3) = (1 - 0.85) + 0.85 * (¼ * 1 + ⅖ * 1) =0.703$

> 假設我們有三個句子（斷詞版）
>
> - S1: 機器 學習 很 有趣
> - S2: 機器 學習 很 困難
> - S3: 深度 學習 解決 困難
>
> 假設所有句子的起始分數都是  
> 1
>
> - w12 = w21 = 3
> - w13 = w31 = 1
> - w23 = w32 = 2
> - $W_1 = 4$
> - $W_2 = 5$
> - $W_3 = 3$

$$
S(V_i) = (1 - d) + d \times \sum \left(\frac{\text{彼此的權重}}{\text{對方的總權重}} \times \text{對方的分數}\right)
$$

圖示說明：右上角框列出三個句子 S1、S2、S3，以及它們之間的對稱權重關係；$w12 = w21$、$w13 = w31$、$w23 = w32$ 表示句子彼此之間的相似度權重是雙向相同的，$W_1$、$W_2$、$W_3$ 表示各句子的總權重。底部公式表示每個句子的分數由阻尼係數 $d$、相鄰句子的權重比例，以及對方句子的分數共同更新。

# Symmetric TextRank

Step 3: 迭代開始

- Update S3
  - 從 S1 那邊可以分到 ¼ 的比例
  - 從 S2 那邊可以分到 ⅖的比例
  - \(S(S_3) = (1 - 0.85) + 0.85 * (\frac{1}{4} * 1 + \frac{2}{5} *1) =0.703\)

---

假設我們有三個句子（斷詞版）

- S1: 機器 學習 很 有趣
- S2: 機器 學習 很 困難
- S3: 深度 學習 解決 困難

假設所有句子的起始分數都是  
1

- w12 = w21 = 3
- w13 = w31 = 1
- w23 = w32 = 2
- \(W_1 = 4\)
- \(W_2 = 5\)
- \(W_3 = 3\)

圖示說明：右上方灰色圓角框列出三個句子、所有句子的起始分數，以及句子之間的對稱權重與各句子的總權重。

---

**第一輪結束後：**  
S1 : 1→0.94  
S2: 1→**1.35**  
S3: 1→0.7  
Repeat Step3 直到收斂

圖示說明：左下方灰色圓角框顯示第一輪迭代後，S1、S2、S3 的分數由 1 更新為 0.94、1.35、0.7，並提示重複 Step3 直到收斂。

---

\[
S(V_i) = (1-d) + d \times \sum \left(\frac{\text{彼此的權重}}{\text{對方的總權重}} \times \text{對方的分數}\right)
\]

圖示說明：右下方黑色公式框表示 Symmetric TextRank 的分數更新公式；每個節點的新分數由阻尼係數 \(d\)、與相鄰節點之間的權重、相鄰節點的總權重，以及相鄰節點分數共同決定。

# Evaluating Summarization Quality

## How to Assess Summarization?

- Evaluating summarization requires both <span style="color:red">automatic</span> and <span style="color:red">human</span> evaluation methods.
- Key criteria: Relevance, Fluency, Coherence, Conciseness, and Faithfulness.

# Automatic Evaluation – ROUGE

- Recall-Oriented Understudy for Gisting Evaluation
- In summarization, omission is worse than redundancy
- ROUGE-N (N-gram matching) & ROUGE-L (Longest Common Subsequence)

Reference: 小明 喜歡 吃 蘋果

Generated: 小明 非常 喜歡 吃 紅色 的 蘋果

ROUGE-1 (是否有關鍵字):

- Overlap: 小明、喜歡、吃、蘋果
- \( \text{Recall} = 4/4 = 100\% \)
- \( \text{Precision} = 4/7 = 57.1\% \)
- \( \text{F1-score} = 72.7\% \)

# Automatic Evaluation – ROUGE

- <span style="color:red">Recall</span>-Oriented Understudy for Gisting Evaluation
- In summarization, omission is worse than redundancy
- ROUGE-N (N-gram matching) & ROUGE-L (Longest Common Subsequence)

Reference: 小明 喜歡 吃 蘋果

Generated: 小明 非常 喜歡 吃 紅色 的 蘋果

ROUGE-2 (是否流暢):

- Overlap: [喜歡 吃]
- $\text{Recall} = 1/3 = 33.3\%$
- $\text{Precision} = 1/6 = 16.7\%$
- $\text{F1-score} = 22.2\%$

# Automatic Evaluation – ROUGE

- <span style="color:red">Recall</span>-Oriented Understudy for Gisting Evaluation
- In summarization, omission is worse than redundancy
- ROUGE-N (N-gram matching) & ROUGE-L (Longest Common Subsequence)

Reference: 小明 喜歡 吃 蘋果

Generated: 小明 非常 喜歡 吃 紅色 的 蘋果

ROUGE-L (句子架構):

- LCS: 小明 → 喜歡 → 吃 → 蘋果 (長度為 4)
- $\text{Recall} = \text{len(LCS)}/\text{len(Ref)} = 4/4 = 100\%$
- $\text{Precision} = \text{len(LCS)}/\text{len(Gen)} = 4/7 =57.1\%$
- $\text{F1-score} = 72.7\%$

# Automatic Metrics

| Metric | Description | Strengths | Limitations |
|---|---|---|---|
| ROUGE | Measures <span style="color:red">overlap of n-grams</span><br>between generated and<br>reference summaries | Fast, widely used,<br>good for extractive<br>summaries | Favors surface similarity,<br>ignores meaning |
| BLEU | Counts <span style="color:red">n-gram overlaps</span> | Good for short<br>summaries | Penalizes paraphrasing,<br>not ideal for summarization |
| METEOR | Uses stemming & synonym<br>matching | More robust than<br>BLEU | Computationally complex |
| BERTScore | Uses deep learning to measure<br>semantic similarity | Captures meaning<br>better than<br>ROUGE/BLEU | Requires pre-trained<br>models |

# Human Evaluation

| Aspect | Description | Example Evaluation Criteria |
|---|---|---|
| Relevance | Captures key information from source | Are essential details included? |
| Fluency | Grammatically correct & readable | Does the summary read smoothly? |
| Coherence | Logical sentence connections | Does the summary flow naturally? |
| Conciseness | Brief yet informative | Does it remove unnecessary words? |
| Faithfulness | Accurately reflects source content | Is it free from misinformation? |

# Challenges in Text Summarization

- **Context Understanding:** Struggling to capture deep semantic meaning, especially in long documents.
- **Coherence:** Summaries assembled from extracted sentences may lack natural logical flow.
- **Information Loss:** High risk of omitting crucial details from the source text.
- **Bias & Hallucination:** AI-generated summaries might introduce misinformation.