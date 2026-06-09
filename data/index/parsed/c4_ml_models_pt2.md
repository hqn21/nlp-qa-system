# Topic Modeling

# What is Topic Modeling?

- A type of <span style="color:red">unsupervised machine learning</span> used for text analysis
- Discovers <span style="color:red">latent topics</span> in a collection of documents without human intervention
- Helps in organizing, summarizing, and understanding large text corpora
- Unlike classification, <span style="color:red">topics are not predefined but are derived from patterns in the data</span>

# Key Topic Modeling Techniques

## Latent Dirichlet Allocation (LDA)

- The most widely used topic modeling algorithm
- Assumes each document is a mixture of <span style="color:red">multiple topics</span>, and each topic is a mixture of <span style="color:red">words</span>
- Uses Bayesian probability and Dirichlet distribution to infer topic distributions
- Example use case: Organizing scientific articles into research domains (overlapping topics, long text)

# Key Topic Modeling Techniques

## Non-Negative Matrix Factorization (NMF)

- Uses <span style="color:red">matrix factorization</span> to find hidden patterns in textual data
- Works well for <span style="color:red">high-dimensional data</span> by breaking text down into meaningful  
  components (sparse matrix)
- Does not assume a probabilistic model like LDA (faster)
- Example use case: Extracting themes from customer service chat logs  
  (non-overlapping topics, short text)

# Key Topic Modeling Techniques

## Latent Semantic Analysis (LSA)

- Applies <span style="color:red">Singular Value Decomposition (SVD)</span> to reduce dimensionality and capture topic-word relationships
- Good for <span style="color:red">finding synonym relationships</span> and <span style="color:red">handling noisy data</span>
- Example use case: Improving search engine results based on contextual meaning

# LDA Overview

- **Probabilistic generative model** used for discovering topics in a collection of documents
- Each document is a <span style="color:red">mixture of multiple topics</span>, and each topic is a <span style="color:red">distribution over words</span>
- Utilizes **Dirichlet priors** to control topic distributions
- Uses **Bayesian inference techniques** such as **Gibbs sampling** or **Variational Inference**
- Requires specifying the number of topics (K) beforehand

https://reurl.cc/VzDxj6

# How LDA Works (High-Level)

我

我是誰:  
品種 → 電動人 (topics)  
興趣 → 漫畫、電動

[Diagram/Figure: A cartoon character labeled「我」is shown on the left. A right-pointing arrow leads from the character toward a city skyline image on the right, suggesting the person is going to or searching within an unfamiliar city/place.]

人生地不熟， 哪裡適合 電動人去呢？

# Collect Documents

## 地區 (Documents)

![Figure: Two photographs representing "地區 (Documents)": the upper image shows the entrance of a shopping/commercial area with Chinese signage; the lower image shows a nighttime urban shopping district with tall buildings, lights, and pedestrians. These images convey documents as geographic regions or places being collected.](figure)

## 朋友 (Words)

![Figure: Two cartoon characters representing "朋友 (Words)": a boy character above and a girl character below. These images convey words as friends or individual entities associated with the collected documents.](figure)

# 初始狀態 (隨便猜)

| 地區 (Documents) | 地區特性 / 朋友興趣<br>(Topics) | 朋友 (Words) |
|---|---|---|
| 圖：光華商場的街景照片 | 雙向箭頭連結地區與朋友／興趣<br><br>大雄是文青 | 圖：大雄 |
| 圖：夜間商場／百貨街景照片 | 雙向箭頭連結地區與朋友／興趣<br><br>靜香是網美 | 圖：靜香 |

圖示關係：左側的地區（Documents）透過中間的地區特性／朋友興趣（Topics）與右側的朋友（Words）產生對應；上方對應為「大雄是文青」，下方對應為「靜香是網美」。

# Iterative Update

| 地區 (Documents) | 地區特性 / 朋友興趣<br>(Topics) | 朋友 (Words) |
|---|---|---|
| Figure: Photograph of 光華商場 storefront. | Diagram: A horizontal bidirectional arrow indicates iterative relationship/update between the left side 地區 (Documents) and the right side 朋友 (Words), mediated by 地區特性 / 朋友興趣 (Topics). Beneath the arrow is a rounded rectangle labeled「大雄是文青」. | Figure: Cartoon character representing a friend. |

大雄是文青

# Iterative Update

## 地區 (Documents)

![Photo of 光華商場 storefront, representing a region/document.](image)

再仔細觀察其他人...

## 地區特性 / 朋友興趣  
(Topics)

↔

大雄是文青

![Photo of a person.](image)

電動人

![Photo of a person.](image)

電動人

![Anime character image.](image)

電動人

## 朋友 (Words)

![Cartoon character Nobita, representing a friend/word.](image)

## Diagram/Figure Description

The slide presents an iterative update relationship among three conceptual groups: **地區 (Documents)** on the left, **地區特性 / 朋友興趣 (Topics)** in the center, and **朋友 (Words)** on the right. A horizontal double-headed arrow above the topic label **大雄是文青** indicates a bidirectional/iterative relationship between the observed documents, inferred topics, and associated friends/words. The bottom examples labeled **電動人** represent other observed people/characters used to refine or update the inferred topic/interest.

# Iterative Update

## 地區 (Documents)

![Photo of 光華商場 storefront.](figure)

Visible text in photo includes:

- 光華商場

## 地區特性 / 朋友興趣  
## (Topics)

A horizontal double-headed arrow connects the 地區 (Documents) side toward the 地區特性 / 朋友興趣 (Topics) area, indicating an iterative update relationship between documents and topics.

Rounded rectangle label:

> 大雄是電動人

Below the topic label are three example friends/characters, each associated with the same topic label:

- 電動人
- 電動人
- 電動人

## 朋友 (Words)

![Cartoon character representing 朋友 (Words).](figure)

The diagram conveys that a 地區 (Documents) item is iteratively related to inferred 地區特性 / 朋友興趣 (Topics), and friends/words are associated with those topics, such as identifying 大雄 as 電動人 and matching multiple friends to 電動人.

# Iterative Update

## 地區 (Documents)

**Figure:** A photo of 光華商場.

## 地區特性 / 朋友興趣  
## (Topics)

**Diagram:** A horizontal double-headed arrow connects the document/region side with the topic side, indicating an iterative relationship/update between regions and inferred topics.

**Topic label:** 大雄是電動人

**Figures:** Three friend/word examples are shown under the topic, each labeled:

電動人

電動人

電動人

## 朋友 (Words)

**Figure:** A cartoon character representing a friend/word.

**Figure description:** The slide illustrates an iterative update process: regions/documents are associated with topics based on the friends/words appearing in them. After repeated iterations, 光華商場 is inferred to be strongly associated with the 電動人 topic.

經過多次迭代後，發現光華商場裡  
出現許多電動人，因此定義出: 光  
華商場 = 90% 電動人主題

# Iterative Update

## 地區 (Documents)

![光華商場照片](diagram: a document/location image showing 光華商場.)

## 地區特性 / 朋友興趣  
(Topics)

↔

大雄是電動人

## 朋友 (Words)

![大雄/Nobita cartoon](diagram: a word/friend example. 大雄/Nobita is associated with the topic label「電動人」.)

![Faker photo](diagram: Faker is shown as a friend/word example associated with「電動人」.)

電動人

![person photo](diagram: another friend/word example associated with「電動人」.)

電動人

![anime character image](diagram: another friend/word example associated with「電動人」.)

電動人

## Diagram meaning

The slide illustrates an iterative update relationship between 地區 (Documents), 地區特性 / 朋友興趣 (Topics), and 朋友 (Words). A document/location such as 光華商場 is connected to a topic such as「大雄是電動人」, and multiple friends/words can be associated with the same topic「電動人」. The note explains that the same friend/word can appear under different topics depending on the document/context.

> Note: 同一個朋友(word)可以出現在不同主題  
> 例如:Faker出現在光華商場，他代表的是 電動人;但如  
> 果Faker出現在信義區百貨公司代言手錶，他可能代表  
> 時尚/商業

# Iterative Update

## 地區 (Documents)

[Figure: A photograph of 光華商場, representing a 地區 / document.]

## 地區特性 / 朋友興趣  
(Topics)

[Diagram: A central topic label connects the 地區 (Documents) concept on the left with 朋友 (Words) on the right. The rounded box states:]

大雄在光華商場的  
標籤為電動人

[Below the topic statement are three friend/person images, each labeled with the same topic:]

電動人

電動人

電動人

## 朋友 (Words)

[Figure: A cartoon image of 大雄, representing a 朋友 / word.]

# Iterative Update

## 地區 (Documents)

[Figure: A photo of 光華商場 representing a document/place.]

## 地區特性 / 朋友興趣  
(Topics)

[Figure: A rounded rectangle topic label between the document/place and friends/words, with arrows pointing left and right to indicate iterative updating between documents, topics, and words/friends.]

大雄在光華商場的  
標籤為電動人

## 朋友 (Words)

[Figure: A cartoon character representing 大雄/Nobita as a word/friend example.]

[Figure: Three friend/word images below the topic label, each associated with the same topic label.]

電動人

電動人

電動人

如果我們在一個沒去過的地下街 (new  
document), 看到一堆Faker 和研磨在走動  
，雖然我們不知道那是什麼地方，但根據  
LDA可以推測那邊的主題

# 同樣地, 經過多次迭代我們可以推論信義區的主題分佈為…

- 50%: 購物仔
- 30%: 電影仔
- 15%: 網美
- 5%: 電動人

## 圖示說明

中央圖片為信義區街景，代表「信義區」。從中央圖片延伸出多個箭頭，分別指向四個主題類別及其比例：

- 箭頭指向右上方購物女性圖片，表示信義區主題中 **50%** 為「購物仔」。
- 箭頭指向右下方電影院觀眾圖片，表示信義區主題中 **30%** 為「電影仔」。
- 箭頭指向左側拍照女性圖片，表示信義區主題中 **15%** 為「網美」。
- 箭頭指向下方動漫人物圖片，表示信義區主題中 **5%** 為「電動人」。

# Key Concepts in LDA

- **Documents as Topic Mixtures**
  - Example: A research paper might be 60% about AI and 40% about statistics
- **Topics as Word Distributions**
  - Example:
  - Topic 1 (Sports): basketball (0.2), football (0.15), tennis (0.1), player (0.05)...
  - Topic 2 (Technology): AI (0.2), machine (0.15), learning (0.1), neural (0.05)...
- **Dirichlet Distribution**
  - Alpha ($\alpha$): Controls how documents mix topics
    - High $\alpha$ → Documents contain many topics evenly
    - Low $\alpha$ → Documents are dominated by fewer topics
  - Beta ($\beta$): Controls how topics mix words
    - High $\beta$ → Topics share more words
    - Low $\beta$ → Topics are more distinct

# Step-by-Step Process

1. <span style="color:red">Initialize topics randomly</span> for words in each document (Dirichlet Distribution).
2. Iterative topic assignment using Gibbs Sampling
   a. Reassign words to topics based on:
      i. How frequently a topic appears in a document  
      ii. How frequently a word appears in a topic across <span style="color:red">all documents</span>
3. <span style="color:red">Repeat until convergence</span> to stabilize topic distributions.
4. Output final results:
   a. Topic-word distributions (which words belong to which topics)  
   b. Document-topic distributions (which topics dominate which documents)

# Gibbs Sampling

For each word $w_i$ in document $d_i$, reassign its topic based on the **conditional probability:**

$$
P(z_i = k \mid w_i, d_i) \propto \frac{n_{dk} + \alpha}{\sum_k n_{dk} + K\alpha} \times \frac{n_{kw} + \beta}{\sum_w n_{kw} + V\beta}
$$

where:

- $n_{dk}$ = Number of words in document $d$ assigned to topic $k$.
- $n_{kw}$ = Number of times word $w$ appears in topic $k$.
- $\alpha$ = Dirichlet prior for **document-topic distribution**.
- $\beta$ = Dirichlet prior for **topic-word distribution**.
- $K$ = Total number of topics.
- $V$ = Total vocabulary size.

# Gibbs Sampling

For each word $w_i$ in document $d_i$, reassign its topic based on the **conditional probability**:

$$
P(z_i = k \mid w_i, d_i) \propto \frac{n_{dk} + \alpha}{\sum_k n_{dk} + K\alpha} \times \frac{n_{kw} + \beta}{\sum_w n_{kw} + V\beta}
$$

P(標籤 = 網美 | 其他人的狀態)

where:

- $n_{dk}$ = Number of words in document $d$ assigned to topic $k$.
- $n_{kw}$ = Number of times word $w$ appears in topic $k$.
- $\alpha$ = Dirichlet prior for **document-topic distribution**.
- $\beta$ = Dirichlet prior for **topic-word distribution**.
- $K$ = Total number of topics.
- $V$ = Total vocabulary size.

# Gibbs Sampling

For each word $w_i$ in document $d_i$, reassign its topic based on the **conditional probability:**

$$
P(z_i = k \mid w_i, d_i) \propto \frac{n_{dk} + \alpha}{\sum_k n_{dk} + K\alpha} \times \frac{n_{kw} + \beta}{\sum_w n_{kw} + V\beta}
$$

該地區目前的網美比例 + α

*Annotation: The rounded callout “該地區目前的網美比例 + α” is placed beneath the document-topic fraction, indicating the $n_{dk} + \alpha$ component of the conditional probability.*

where:

- $n_{dk}$ = Number of words in document $d$ assigned to topic $k$.
- $n_{kw}$ = Number of times word $w$ appears in topic $k$.
- $\alpha$ = Dirichlet prior for **document-topic distribution**.
- $\beta$ = Dirichlet prior for **topic-word distribution**.
- $K$ = Total number of topics.
- $V$ = Total vocabulary size.

# Gibbs Sampling

For each word $w_i$ in document $d_i$, reassign its topic based on the **conditional probability**:

$$
P(z_i = k \mid w_i, d_i) \propto
\frac{n_{dk} + \alpha}{\sum_k n_{dk} + K\alpha}
\times
\frac{n_{kw} + \beta}{\sum_w n_{kw} + V\beta}
$$

**Annotation:** A rounded callout beneath the topic–word fraction annotates the numerator $n_{kw} + \beta$ with:  
全台北靜香被歸類為網美的次數 + □

where:

- $n_{dk}$ = Number of words in document $d$ assigned to topic $k$.
- $n_{kw}$ = Number of times word $w$ appears in topic $k$.
- $\alpha$ = Dirichlet prior for **document-topic distribution**.
- $\beta$ = Dirichlet prior for **topic-word distribution**.
- $K$ = Total number of topics.
- $V$ = Total vocabulary size.

# API Perspective: Inputs and Outputs

- Inputs: count vectors (bag of words)

|  | text | mining | is | to | find | useful | information | from | text | mined | dark | came |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| D2 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| D3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |

# API Perspective: Inputs and Outputs

- 2 matrixes as output: <span style="color:red">topics x words</span>, document x topics

|        | word1 | word2 | word3 | word4 | word5 | word6 | word7 | word8 |
|--------|-------|-------|-------|-------|-------|-------|-------|-------|
| topic1 |       |       |       |       |       |       |       |       |
| topic2 |       |       |       |       |       |       |       |       |
| topic3 |       |       |       |       |       |       |       |       |
| topic4 |       |       |       |       |       |       |       |       |
| topic5 |       |       |       |       |       |       |       |       |

# API Perspective: Inputs and Outputs

- 2 matrixes as output: <span style="color:red">topics x words</span>, document x topics

## Figure

The figure shows an example of the **topics x words** output as three topic-specific bar charts. Each topic is associated with a ranked list of top words; the blue horizontal bars indicate the relative strength/weight of each word within that topic.

| Topic 1 | Topic 2 | Topic 3 |
|---|---|---|
| software | people | search |
| microsoft | government | people |
| virus | us | mail |
| security | uk | site |
| anti | home | spam |
| court | rights | users |
| us | law | google |
| people | without | sites |
| legal | house | number |
|  |  | web |

Example of topics x words (barchart of top words per topic)

# API Perspective: Inputs and Outputs

- 2 matrixes as output: topics x words, <span style="color:red">document x topics</span>

**Figure:** A bar chart representing a document-by-topics output distribution. The x-axis lists Topic 1, Topic 2, Topic 3, Topic 4, and Topic 5. Topic 1 has the largest bar, Topic 3 has a smaller bar, and Topic 2, Topic 4, and Topic 5 have no visible bars, indicating little or no association with those topics.

# API Perspective: Inputs and Outputs

- 2 matrixes as output: topics x words, <span style="color:red">document x topics</span>

**Figure/diagram description:** A bar chart represents the **document x topics** output. The x-axis is labeled with Topic 1, Topic 2, Topic 3, Topic 4, Topic 5. Topic 1 has the tallest bar, Topic 3 has a smaller bar, and the other topics have no visible bars. A callout connects the bar chart to topic-word interpretations, showing that a document can have weight on multiple topics when its words relate to those topics.

> Topic 1 was related to: Microsoft, viruses,  
> security, ...
>
> Topic 3 was related to: Google, search, spam,  
> ...
>
> What if our document is about <u>viruses</u> acquired  
> through <u>spam</u>?

# The Actual API

```python
X = CountVectorizer().fit_transform(text)

lda = LatentDirichletAllocation()
lda.fit(X) # not fit(X, Y)
Z = lda.transform(X) # returns docs x topics matrix
```

# The Actual API

```python
z = lda.fit_transform(x) # all at once

# where is the topics x words matrix?
topics = lda.components_

# the topics are "internal" to the model, documents are not
# we can pass in new data to be transformed under the
# existing topics
z_test = lda.transform(x_test)
```

# Non-Negative Matrix Factorization (NMF)

- Factorization-based topic modeling method.
- Decomposes a <span style="color:red">document-term</span> matrix into two lower-dimensional matrices.
- Ensures that all matrix values remain <span style="color:red">non-negative</span>, making the results easier to interpret.
- Works well with TF-IDF-weighted text representations.
- Requires predefining the number of topics (K) beforehand.

# Recommender Systems

- You want to recommend movies to users, but there many ways
- Let’s simplify this: a good recommendation is a movie that a user would rate highly
- Recommendation list is simply a list of movies ordered by predicted rating
- Our task is simple: predict unknown ratings

**Figure:** A Netflix interface showing rows of movie and TV show posters (e.g., “Popular on Netflix,” “Trending Now,” “Thrillers”), illustrating a recommender system presenting ordered lists of content to a user.

# The Rating Matrix

- M users (rows), N movies (columns) → \(M \times N\) matrix
- Important: we don’t know most of the values
- Why? Just think about how many movies exist. How many have you seen?  
  Rated?
- It’s a **sparse** matrix
- Different notion of sparisty from  
  TF-IDF (zero vs. missing)
- Goal: fill in missing values

| User | La La Land | Toy Story 4 | Bring Him Home | Zootopia | Interstellar | The Greatest Showman |
|---|---:|---:|---:|---:|---:|---:|
| User 1 | 5 |  | 8 | 7 |  |  |
| User 2 | 9 | 10 | 8 | 9 |  |  |
| User 3 | 6 | 6 |  | 6 | 10 | 7 |
| User 4 | 8 |  |  |  | 6 | 10 |

The figure shows a sparse user-movie rating matrix: users are represented by avatar rows, movies are represented by poster columns, and observed ratings appear as numbers in some cells while unrated or unknown values are blank.

# Matrix Factorization

\[
R \approx WH
\]

## Diagram

The slide shows a matrix factorization relationship:

- A large matrix labeled **R (M x N)** is approximately equal to the product of:
  - A tall matrix labeled **W (M x K)**
  - A wide matrix labeled **H (K x N)**

\[
R\ (M \times N) \approx W\ (M \times K)\ H\ (K \times N)
\]

A callout explains:

> When we multiply W and H together, the result is an MxN matrix, with no missing values!

# How to Find W & H?

- We “train” ML models by defining a loss function and then finding the values of W and H that would minimize that loss
- E.g. squared error between predictions and true ratings

## Diagram

The diagram illustrates matrix factorization: \(R = WH\).

- \(R\): an \(m \times n\) matrix with genes as rows and samples as columns.
- \(W\): an \(m \times k\) matrix representing metaassays/metasamples.
- \(H\): a \(k \times n\) matrix representing metagenes.
- The relationship shown is:

\[
R = WH
\]

# NMF Output

**Diagram:** A large matrix labeled “Documents x Words” is approximately factorized (\(\approx\)) into two smaller matrices:

\[
\text{Documents x Words} \approx W(M \times K) \times H(K \times N)
\]

- The matrix \(W (M \times K)\) is labeled with “Documents” along the vertical axis and “Topics” along the horizontal axis.
- The matrix \(H (K \times N)\) is labeled with “Topics” along the vertical axis and “Words” along the horizontal axis.
- A callout states: “The same outputs as LDA!”

# Latent Semantic Analysis

- LSA is just the application of a well-known ML technique (**SVD**) applied to a  
  term-document matrix
- Just like applying Naive Bayes or Logistic Regression to vectors
- By studying these techniques, you’ll improve your skills in other areas too  
  (e.g. computer vision)

# Singular Value Decomposition (SVD) Intuition

- SVD is useful for reducing dimensionality
- SVD is useful for visualizing your data
- SVD works by finding the best rotation of your data points

# Reducing Dimensionality

- In NLP, data is typically high-dimensional (many columns)
- Often, # features >> # samples
- More dimensions = more data to process = more time spent
- Reduce dimensionality = pipeline is more efficient and fast

|  | I | love | dogs | hate | and | knitting | is | my | hobby | passion |
|---|---|---|---|---|---|---|---|---|---|---|
| Doc 1 | 0.18 | **0.48** | 0.18 |  |  |  |  |  |  |  |
| Doc 2 | 0.18 |  | 0.18 | **0.48** | 0.18 | 0.18 |  |  |  |  |
| Doc 3 |  |  |  |  | 0.18 | 0.18 | **0.48** | **0.95** | **0.48** | **0.48** |

# Example: Reducing Dimensionality

- Project all the data points down to the line
- The data is described by a single variable, **size**
- We only need 1 dimension

**Diagram/Figure:** A scatter plot with **Human Weight** on the horizontal axis and **Human Height** on the vertical axis. Blue data points cluster around an upward-sloping red line, showing that height and weight increase together. The red line represents a single “size” dimension onto which all data points can be projected. A lower-left region on the line is labeled **"Small Size"**, and an upper-right region is labeled **"Big Size"**, indicating that positions along the line correspond to increasing overall size.

# Visualization

- Visualization is always useful in data science and ML
- The world is only 3-D, how can we see data that is 1000-D?

## Figure

Two side-by-side plots illustrate common machine learning tasks:

- **Classification**: A scatter plot with two groups of points (blue circles clustered in the lower-left and purple plus signs clustered in the upper-right). A red dashed diagonal line separates the two classes.
- **Regression**: A scatter plot of blue points following an upward trend. A red dashed line represents the fitted regression line through the data.

# Rotation

- To understand how this works, we should think “backwards”
- Why do we do dimension reduction? We believe our data has smaller number  
  of dimensions, but was embedded into a larger dimensional space

**Figure:** A 3-D surface plot with axes labeled \(x/L(x)\), \(y/L(y)\), and \(z\), showing a curved 2-D surface embedded in 3-D space, with contour lines projected onto the base plane. A callout points to the surface and reads: “A 2-D object embedded in 3-D space”.

# Embed the 2-D Object in 3-D Space

\[
A_{1\times2} \times M_{2\times3} + \text{Noise} = A'_{1\times3}
\]

M → 旋轉、縮放和傾斜  
Noise → 對每個點加入微小隨機擾  
動，產生 3D 的厚度(雜訊)

\[
A_{1\times2} = [x,y]
\]

**Diagram/Figure description:** A 2-D blue smiley-face point cloud plotted on an \(x,y\) coordinate plane is transformed into a 3-D object inside a cube with axes labeled X, Y, and Z. A thick curved black arrow points from the 2-D plot toward the 3-D cube, indicating embedding the 2-D object into 3-D space. The transformation uses matrix \(M\) for rotation, scaling, and shearing, and adds Noise to each point to create small random perturbations that give the object 3-D thickness.

# Different Angles

**Figure:** Three 3D scatter plots show the same blue point-cloud dataset viewed from different angles. From the upper/left views, the data appears as a thick, noisy spiral/ring-like structure with clustered regions; from the lower-right view, the same structure appears compressed into a diagonal band. The thickness of the point cloud represents added noise. A yellow highlighted cursor marker appears over each view, indicating the same interaction/selection context while the viewing angle changes.

> Thickness is the noise  
> we add

# After Applying SVD

- We recover the happy face
- It’s not at the right orientation, but that’s ok

\[
A = U \Sigma V^T
\]

Vᵀ: 找出資料的最佳觀測視角 (旋轉空間)  
Σ: 決定每個視角的重要性 (大的值是特徵, 小的  
值是雜訊)  
丟棄 Σ 中的微小數值後，重新計算出的 \(A_{\text{clean}}\)  
就是無雜訊的笑臉

**Figure:** A 2D scatter plot with axes ranging from -10.0 to 10.0 shows a blue happy face recovered in a rotated orientation: a circular outline, two filled eyes, and a curved mouth arc. It conveys that SVD found the meaningful orientation of the data and removed the noisy third dimension.

> SVD found the right  
> orientation, and threw away  
> the 3rd “noise” dimension

# Noise Removal

**Diagram description:** Original data dimensions each contain a mixture of data and noise. A transformation/rotation (shown by a right-pointing arrow) changes the axes so that the resulting dimensions separate into pure data dimensions and a pure noise dimension.

> Original data: each dimension is a bit of data + noise

| Original data dimensions |
|---|
| Data + Noise |
| Data + Noise |
| Data + Noise |

→

| Rotated data dimensions |
|---|
| Data |
| Data |
| Noise |

> Rotated data: axes are aligned so that each dimension is pure data or pure noise

# What Does LSA Do?

> The “denoised data” is put into  
> a documents x topics matrix

**Diagram description:** An **X matrix (TF-IDF or counts)** is transformed by **LSA/SVD** into a result consisting of a **Z matrix** and **Noise columns (these are not kept)**. The kept **Z matrix** represents the “denoised data” in a documents x topics matrix.

- X matrix  
  (TF-IDF or counts)
- LSA/SVD
- Z matrix
- Noise  
  columns  
  (these are not  
  kept)

# What Does LSA Do?

## Diagram

An **X matrix (TF-IDF or counts)** is transformed via **LSA/SVD** into a matrix with kept columns and discarded noise columns.

- **X matrix (TF-IDF or counts)** → **LSA/SVD** → **Z matrix** + **Noise columns (these are not kept)**
- The “denoised data” is put into a documents x topics matrix
- The columns are ordered by “importance” (left most is most important)

The resulting matrix shows a narrow left section labeled **Z matrix**, representing the retained denoised topic dimensions, and a wider right section labeled **Noise columns (these are not kept)**, representing discarded less important dimensions.

# What Does LSA Do?

## Diagram

- An **X matrix (TF-IDF or counts)** is transformed via **LSA/SVD** into a **Z matrix**.
- The resulting matrix contains:
  - **Z matrix**
  - **Noise columns (these are not kept)**
- The “denoised data” is put into a documents x topics matrix
- This means when you plot the data with 2-dimensions, you’re choosing the best 2 dimensions to show
- The columns are ordered by “importance” (left most is most important)

# LSA in Code

```python
# can use Scikit-Learn or Numpy/Scipy
# Numpy/Scipy is more useful for detailed computations
from sklearn.decomposition import TruncatedSVD

# create an object - you use num components
# e.g. 2 for visualization, cross-validation, etc.
model = TruncatedSVD(n_components=2)

# train/fit the model
model.fit(X)

# alternatively, can use term-document matrix
# if you want word vectors instead of document vectors
model.fit(X.T)
```

# LSA in Code

```python
# transform data
Z = model.transform(X)

# all in one step
Z = model.fit_transform(X)

# note: Z has shape N x K (K = number of "hidden topics")
# note: unsupervised learning
```

# Choosing the Right Number of Topics

- Setting <span style="color:red">too few</span> topics: Oversimplifies the data, leading to broad and uninformative topics
- Setting <span style="color:red">too many</span> topics: Overfitting, making results harder to interpret
- Methods to determine optimal topic numbers:
  - **Coherence Score**
    - Measures how semantically related the top topic words are
    - Higher = more meaningful topics
  - **Perplexity Score**
    - Measures how well the model predicts unseen data
    - Lower = better generalization
    - Mainly for LDA

# Coherence Score

**Figure:** A line chart plots **Coherence Score** (y-axis) against **Number of Topics (k)** (x-axis). The coherence score rises from about 0.35 at \(k=2\), reaches a highlighted peak labeled **Optimal Topic Number (k=8)** at about 0.65, then declines and fluctuates as \(k\) increases toward 20. The left rising region is annotated **Underfitting (Too few topics)**, and the right fluctuating region is annotated **Overfitting (Too many topics)**.

- Are top words in a topic meaningfully related?
- Example:
  - High coherence: apple, banana, grape, orange
  - Low coherence: apple, engine, democracy, pillow
- Computed using <span style="color:red">word co-occurrence</span> or <span style="color:red">semantic similarity</span> (e.g., C\_v, UMass)
- <span style="color:red">Higher is better</span>
- Good for evaluating topic <span style="color:red">interpretability</span>

# Perplexity Score

**Figure (line chart): Perplexity Score vs. Number of Topics (k)**

- X-axis: Number of Topics (k)
- Y-axis: (Lower is Better) Perplexity Score
- The curve shows perplexity decreasing as the number of topics increases.
- At \(k=2\), the chart is annotated: High Perplexity, Poor Prediction (k=2)
- At \(k=8\), a green point marks the chart annotation: Elbow Point (k=8)
- At \(k=20\), the chart is annotated: Diminishing Returns, Slower Decrease (k=20)
- The relationship conveyed is that increasing the number of topics lowers perplexity sharply at first, then improvement slows after the elbow point.

- Measures model's ability to predict <span style="color:red">unseen documents</span>
- Lower perplexity → better generalization
- Common in language modeling
- But:
  - Doesn’t guarantee meaningful or interpretable topics
  - A model with low perplexity can still produce incoherent topics
- Not always aligned with human judgment

# Calculating Perplexity Score (skip)

對於一個語料庫 $D$：

$$
\mathrm{Perplexity}(D) = \exp\left(-\frac{\sum_{d \in D} \log P(w_d)}{\sum_{d \in D} N_d}\right)
$$

- $P(w_d)$：模型對文件 $d$ 的所有詞語的聯合機率
- $N_d$：文件 $d$ 中的總詞數
- 結果越低 → 表示模型能更好地解釋這些資料

# Challenges in Topic Modeling

- Choosing the right number of topics
- Interpreting abstract topics
  - Topics are probabilistic, not always clear-cut
- Handling short texts
  - Tweets, chat messages, and fragmented text pose challenges
- Noise in text
  - Presence of irrelevant words and misspellings affects quality