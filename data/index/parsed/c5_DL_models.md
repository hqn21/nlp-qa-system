# Announcement

- 期中考
  - 4/22 (三)14:10 ~ 16:00
  - 地點: 337, 338 (請參考ilearning 公告)
  - 範圍C1~C5
  - No open book
  - 考試開始30分鐘後不得入場
- Office hour
  - 4/20 18:30-21:00 at this class
  - 若有課程相關問題可以前來
- 期末專題
- 學習活動(課堂練習)

# Deep Learning Models

# Why Move from Traditional NLP to Deep Learning?

- Traditional NLP relies on <span style="color:red">hand-crafted features</span> (e.g., Bag-of-Words, TF-IDF).
  - Formula is designed by human
- Often fails to capture <span style="color:red">context, word order</span>, or <span style="color:red">semantics</span>.
- Struggles with sarcasm, polysemy (e.g., "bank"), and long-distance dependencies.
- Deep learning allows <span style="color:red">automatic feature learning</span> from data.
- Enables more powerful, context-aware models.

# Why Deep Learning Works Well in NLP

- Learns word meaning through <span style="color:red">dense vectors</span> (embeddings).
- Captures syntax, semantics, and contextual relationships.
- Scales to <span style="color:red">large corpora</span> and diverse domains.
- Enables <span style="color:red">end-to-end learning</span> from raw input to prediction.
- Flexible and adaptable across NLP tasks.

# What to Watch Out for When Using Deep Learning in NLP

- **Data Hungry:** Requires large, labeled datasets for training.
- **Computationally Expensive:** Needs powerful hardware (GPU/TPU).
- **Interpretability:** Deep models are often black boxes.
- **Overfitting:** Especially with small or biased data.
- **Ethical Issues:** May reproduce or amplify biases in data.

# Preprocessing Considerations in Deep Learning NLP

# Stemming and Lemmatization

- Sometimes skipped in DL pipelines due to learned representations
  - 深度學習模型能學到 running、runs、ran 在空間中複雜關係，強行把它們都砍成 run，反而可能破壞了原本細微的語態資訊

- May still help in low-resource settings or when training from scratch
  - 如果資料量很小，深度學習模型可能無法自行學到複雜的時態變化，這時或許就可以手動做一些處理

# Stopword Removal

- Sometimes skipped in DL pipelines due to learned representations
- May still help in low-resource settings or when training from scratch
- Optional; models like BERT often benefit from keeping them
  - 停用詞通常會帶有重要的關係資訊
  - Ex: “Flight <span style="color:red">from</span> Paris <span style="color:red">to</span> London” vs “Flight <span style="color:red">to</span> Paris <span style="color:red">from</span> London”

# Padding and Truncation

- In Tensorflow, input sequences must all have equal length
- Use special tokens (e.g., [PAD] or 0)
- \(\text{padded\_seq} = \text{pad\_sequences}(\text{unpadded\_seq})\)
- RNNs have trouble “remembering” the past, so it’s usually more useful to  
  have padding at the front

```text
unpadded_sequences = [
    [1, 2, 3, 4, 5],
    [1, 6, 7, 4, 8],
    [1, 9, 10]
]
```

GPU 無法處理這個  
3x?的矩陣，除非將  
batch size改為1

➡️

```text
padded_sequences = [
    [1, 2, 3, 4, 5],
    [1, 6, 7, 4, 8],
    [0, 0, 1, 9, 10]
]
```

The figure shows an unpadded list of sequences of unequal lengths being transformed into padded sequences of equal length. The shorter sequence `[1, 9, 10]` is padded at the front with two `0` tokens to become `[0, 0, 1, 9, 10]`, matching the length of the other sequences.

# Shapes

- An array containing padded sequences of ints representing sentences will have the shape \(N \times T\)
- N = # of documents or batch size, T = max document length

```python
padded_sequences = [
    [1, 2, 3, 4, 5],
    [1, 6, 7, 4, 8],
    [0, 0, 1, 9, 10]
]
```

Figure: The boxed example shows `padded_sequences` as an array of 3 padded integer sequences, each of length 5, illustrating an \(N \times T\) shape where \(N = 3\) documents/sequences and \(T = 5\) maximum document length.

# Embedding

- Consider a generic task, like trying to predict whether or not a user will purchase something on your website
- One data point you have is how the user got to your site:
  - Search (e.g. google)
  - Advertisement
  - Friend
- Can you just assign numbers? 0 = Search, 1 = Ad, 2 = Friend? No…
- One-hot encoding: \([1,0,0]\) = Search, \([0,1,0]\) = Ad, \([0,0,1]\) = Friend
- If \(w_1\) is large/positive, search users are more likely to purchase
- If \(w_2\) is large/negative, ad users are less likely to purchase

# Same Strategy for NLP

- Treat each word as a category, and create a big feature vector with one position for every possible word, e.g.  
  \([1,0,0,\ldots,0]\) = “a”  
  \([0,1,0,\ldots,0]\) = “aa”  
  …  
  \([0,0,0,\ldots,1]\) = “zygote”
- We can then do our usual \(W^T x + b\) computation where x = one-hot vector

# Is One-Hot Encoding Enough?

- One-hot encoded vectors are not “useful” geometrically

![Diagram description: On the left, a scatter plot shows two clusters of points, blue and red, separated roughly by a dashed diagonal line. A green callout over the bottom of the plot says: Recall: vectors should be "useful". On the right, a cube represents binary one-hot-like vector space with vertices labeled 000, 001, 010, 011, 101, 110, and 111. The label “cat 100” appears near one vertex, “airplane” appears near 001, and “feline” appears inside the cube, illustrating that geometrically related words are not necessarily close or meaningfully arranged in one-hot encodings.](diagram)

# Big Picture

- What we’ve effectively done is created a table / database of word vectors for each word - word index is a query into the table
- We hope that these vectors will have some useful structure (unlike one-hot vectors)

**Diagram/Figure:** A vector-space diagram shows word vectors drawn as arrows from a common origin to labeled points. The words “cat,” “feline,” and “jaguar” appear as nearby magenta points, indicating related animal concepts. The words “airplane,” “helicopter,” and “jet” appear as green points farther to the right, indicating a separate related cluster of aircraft concepts. The figure conveys that learned word vectors can have meaningful geometric structure, where semantically related words are positioned closer together.

# Other Embedding Approaches

- Word2Vec
  - Learn from predicting context
- GloVe
  - Learn from word co-occurrence counts
- Train your own embedding layer
  - Embedding(V, D) in Keras / PyTorch
  - Learns embeddings directly from your task data
- FastText
  - Subword-based embedding
  - Breaks words into character n-grams
- Contextual Embeddings (BERT, GPT)
  - Embeddings change based on sentence context

# CNN x NLP

# 1-D Convolution

- Slide the filter along every position, multiply and add

**Diagram description:** A 1-D input sequence `[0, 3, 4, 5]` is shown three times, labeled `I`, `II`, and `III`. A red filter window of length 2, with filter positions labeled `1` and `2`, slides across the sequence:
- `I`: the filter covers `0` and `3`
- `II`: the filter covers `3` and `4`
- `III`: the filter covers `4` and `5`

# 1-D Convolution Example

- Input sequence

| 1 | 2 | 3 | 2 | 1 |
|---|---|---|---|---|

- Filter

| 1 | -1 |
|---|---|

- Result

| -1 | -1 | 1 | 1 |
|---|---|---|---|

Diagram description: The input sequence `1, 2, 3, 2, 1` is processed by the filter `1, -1`, producing the result `-1, -1, 1, 1`. The filter compares adjacent values as it slides across the input sequence.

https://cezannec.github.io/CNN_Text_Classification/

# Convolution on Text

- Using 1-D convolution

|  |  |  |  |
|---|---:|---:|---:|
|  |  |  |  |
| this → | 0.2 | 0.4 | -0.3 |
| movie → | 0.1 | 0.2 | 0.6 |
| has → | -0.1 | 0.4 | -0.1 |
| amazing → | 0.7 | -0.5 | 0.4 |
| diverse → | 0.1 | -0.2 | 0.1 |
| characters → | 0.6 | -0.3 | 0.8 |

**Figure description:** The diagram shows a sentence represented as a vertical word embedding matrix, with each word mapped to a 3-dimensional vector. A cyan-highlighted window covers the top portion of the matrix, illustrating a 1-D convolution filter sliding vertically over consecutive word rows. To the right is a vertical stack of empty cells representing the resulting feature map/output values produced as the convolution window moves down the text.

https://cezannec.github.io/CNN_Text_Classification/

# 1-D Convolutional Kernels

**Diagram:** A 1-D convolutional kernel is shown as a 2-row by 3-column matrix. The horizontal dimension is labeled “width = length of embedding,” and the vertical dimension is labeled “height = numbers of words to look at in sequence.”

**width = length of embedding**

**height = numbers of words to look at in sequence**

| 0.5 | 0.4 | 0.7 |
|---:|---:|---:|
| 0.2 | -0.1 | 0.3 |

Note: you don’t have to worry about the <span style="color:red">width</span> (e.g. embedding size) when creating a 1-D Conv layer, just as you don’t need to deal with the <span style="color:red">depth</span> (e.g. input channels in images) when using a 2-D Conv layer

https://cezannec.github.io/CNN_Text_Classification/

# Recognizing General Patterns

## Diagram / figure description

The figure shows a convolution-like pattern detector applied to word-vector matrices. The same \(2 \times 3\) filter is compared against highlighted two-word windows in two different phrases. The dot products produce similar positive scores, indicating that both windows match the same general pattern.

## Word-vector matrix: “the good movie”

|       |     |     |      |
|-------|-----|-----|------|
| the → | 0.2 | 0.4 | -0.1 |
| good → | 0.7 | -0.5 | 0.3 |
| movie → | 0.1 | 0.2 | 0.6 |

Highlighted window: `good`, `movie`

## Filter

|     |      |     |
|-----|------|-----|
| 0.5 | 0.4  | 0.7 |
| 0.2 | -0.1 | 0.3 |

\[
0.5 * 0.7 + 0.4 * -0.5 + 0.7 * 0.3
\]

\[
+ \quad 0.2 * 0.1 + -0.1 * 0.2 + 0.3 * 0.6
\]

\[
= 0.54
\]

## Word-vector matrix: “a fantastic song”

|             |     |      |      |
|-------------|-----|------|------|
| a →         | 0.1 | 0.3  | -0.2 |
| fantastic → | 0.8 | -0.6 | 0.3  |
| song →      | 0.2 | 0.3  | 0.5  |

Highlighted window: `fantastic`, `song`

\[
0.5 * 0.8 + 0.4 * -0.6 + 0.7 * 0.3
\]

\[
+ \quad 0.2 * 0.2 + -0.1 * 0.3 + 0.3 * 0.5
\]

\[
= 0.53
\]

Found pattern: a **positive** thing

# CNN for Text in Code

```python
i = Input(shape=(T,))
x = Embedding(V + 1, D)(i)
x = Conv1D(32, 3, activation='relu')(x)
x = MaxPooling1D(3)(x)
x = Conv1D(64, 3, activation='relu')(x)
x = MaxPooling1D(3)(x)
x = Conv1D(128, 3, activation='relu')(x)
x = GlobalMaxPooling1D()(x)
# OR: x = Flatten()(x)
x = Dense(1)(x)
# OR: x = Dense(K)(x)
```

| Layer | Output Shape | Description |
|---|---|---|
| Input | (batch_size, 100) | Token ID 序列 |
| Embedding | (batch_size, 100, 50) | 詞向量 |
| Conv1D (32 filters) | (batch_size, 98, 32) | 區域特徵 |
| MaxPool1D(3) | (batch_size, 32, 32) | 降維 |
| Conv1D (64 filters) | (batch_size, 30, 64) | 更深層特徵 |
| MaxPool1D(3) | (batch_size, 10, 64) | 再降維 |
| Conv1D (128 filters) | (batch_size, 8, 128) | 更深層次抽象 |
| GlobalMaxPool1D | (batch_size, 128) | 變成固定長度的句子表示 |
| Dense(1) | (batch_size, 1) | 預測結果（如情感分類） |

# RNN x NLP

# Why CNN Is Not Enough

- CNNs are great for capturing <span style="color:red">local patterns</span> in text, such as short phrases like "not good" or "very happy". But they come with limitations:
  - CNNs only capture <span style="color:red">fixed-size n-gram features</span>.
  - They struggle with <span style="color:red">long-distance dependencies</span> in language.
    - Example: “The book I bought yesterday was amazing.” → “book” and “amazing” are far apart.
  - CNNs are <span style="color:red">position-invariant</span>, meaning they don't inherently understand <span style="color:red">word order</span>.
- To model sequence and context over time, we need a model that remembers previous inputs—this is where **RNNs** come in.

# Recurrent Neural Networks Introduction

**Figure:** A neural network diagram with two input nodes on the left, three hidden nodes in the middle, and two output nodes on the right. Directed arrows connect the input layer to the hidden layer and the hidden layer to the output layer, indicating information flowing from left to right through the network.

# Recurrent Neural Networks Introduction

**Figure:** A neural network diagram with two input nodes on the left, three hidden nodes in the middle, and two output nodes on the right. Light gray arrows show feedforward connections from inputs to hidden nodes and from hidden nodes to outputs. Colored curved arrows loop among and into the hidden nodes, illustrating recurrent connections where hidden-state information is passed forward through time to the same network at the next time point.

傳遞給下一個時間  
點的自己

# Why should we use RNNs?

- Consider classifying words (e.g. parts-of-speech: noun, verb, etc.)
- Suppose we use an ANN:

**Diagram:** A simple feed-forward ANN for POS tagging. An **Input word** \(x\) feeds upward into hidden layer \(h\), which feeds upward into output \(y\), labeled **Output POS tag**.

# Problem with ANN

- Sometimes there can be multiple possible answers, which can only be disambiguated with context
- E.g. “bank” has several meanings
  - Financial institution (maybe higher chance of spam)
  - “River bank” (maybe lower chance of spam)
  - As a verb (and still has multiple meanings)

“Your bank has requested your password.”  
“Let’s take a walk on the river bank.”  
“Would you bank on it?”  
“I bank with Bank of America.”

**Figure description:** The example sentences illustrate how the word “bank” can take different meanings depending on context: a financial institution, a river bank, a verb phrase, or banking with a named institution.

# Back to Our Classification Problem - ANN

**Diagram:** A sequence of independent feed-forward ANN classifiers is shown for words \(1\) through \(T\). Each word position has a vertical chain of three circular nodes connected by upward arrows: \(x \rightarrow h \rightarrow y\). The bottom node \(x\) corresponds to the input for a word, the middle node \(h\) is the hidden representation, and the top node \(y\) is the output. The columns are labeled:

- Output 1  
  \(y\)  
  \(h\)  
  \(x\)  
  Word 1

- Output 2  
  \(y\)  
  \(h\)  
  \(x\)  
  Word 2

- Output 3  
  \(y\)  
  \(h\)  
  \(x\)  
  Word 3

- ...

- Output T  
  \(y\)  
  \(h\)  
  \(x\)  
  Word T

# Back to Our Classification Problem -RNN

## Diagram

A recurrent neural network unrolled over time from Word 1 to Word T.

- **Word 1**
  - `x` feeds upward into `h`
  - `h` feeds upward into `y`
  - `y` is labeled **Output 1**
- **Word 2**
  - `x` feeds upward into `h`
  - `h` feeds upward into `y`
  - `y` is labeled **Output 2**
- **Word 3**
  - `x` feeds upward into `h`
  - `h` feeds upward into `y`
  - `y` is labeled **Output 3**
- **...**
  - `x` feeds upward into `h`
  - `h` feeds upward into `y`
- **Word T**
  - `x` feeds upward into `h`
  - `h` feeds upward into `y`
  - `y` is labeled **Output T**

The hidden states `h` are connected left-to-right across time steps by arrows:

`h` at **Word 1** → `h` at **Word 2** → `h` at **Word 3** → `h` at **...** → `h` at **Word T**.

# Back to Our Classification Problem -RNN

## Diagram

An unrolled RNN over a sequence of words from `Word 1` to `Word T`.

Text shown in the diagram:

- `Output 1`
- `Output 2`
- `Output 3`
- `...`
- `Output T`
- `y`
- `h`
- `x`
- `Word 1`
- `Word 2`
- `Word 3`
- `...`
- `Word T`

The diagram shows repeated RNN time steps. At each time step, an input `x` from a word feeds upward into a hidden state `h`, which feeds upward into an output `y`. Hidden states `h` are connected from left to right across time steps by arrows, representing recurrence through the sequence.

A highlighted path begins at `Word 1` / `x`, passes through the hidden states `h` across the sequence, and ends at `Output T` / `y`, indicating that information from earlier words can influence the final output.

# Problem Types RNNs Can Solve

## Many-to-One

- Definition: Multiple inputs → Single output
- Examples:
  - Spam detection
  - Sentiment analysis

## Many-to-Many

- Definition: Each input → corresponding output
- Examples:
  - Part-of-speech tagging
  - Time series anomaly detection

## Diagram/Figure

The figure contrasts two RNN problem structures:

- **many to one**: Multiple input elements feed into a sequence of hidden states, and only the final hidden state produces a single output.
- **many to many**: Multiple input elements feed into a sequence of hidden states, and each hidden state produces its own corresponding output.

# What Do We Do with h(t)?

- h(t) is the output of RNN at each time step

**Diagram:** An unrolled RNN across time steps. Each time step has an input node `x` feeding upward into a hidden state node `h`. The hidden states are connected left-to-right by arrows, representing recurrent transitions over time. The hidden outputs are labeled \(h_1\), \(h_2\), \(h_3\), \(\ldots\), \(h_T\), indicating the RNN output at each time step.

# What Do We Do with \(h(t)\)?

- Many-to-One

**Diagram description:** A many-to-one recurrent structure is shown. Each time step has an input node \(x\) feeding upward into a hidden state node \(h\). Hidden states connect left-to-right across time with arrows, labeled \(h_1\), \(h_2\), \(h_3\), \(\ldots\), \(h_T\). Only the final hidden state \(h_T\) feeds upward into the output node \(y\).

> Only compute this  
> for many-to-one

# What Do We Do with \(h(t)\)?

- Many-to-Many

**Diagram:** An unrolled recurrent neural network showing a many-to-many sequence mapping. Each time step contains an input node \(x\), a hidden state node \(h\), and an output node \(y\). The input \(x\) feeds upward into \(h\), \(h\) feeds upward into \(y\), and each hidden state passes information horizontally to the next hidden state. The hidden states are labeled across time as \(h_1\), \(h_2\), \(h_3\), \(\ldots\), \(h_T\), indicating a sequence of inputs producing a sequence of outputs.

# What Do We Do with \(h(t)\)?

- Many-to-Many

> Note: the same weights are used at every time step for each layer (weight sharing)

**Diagram:** An unrolled recurrent neural network over multiple time steps. At each time step, an input node \(x\) feeds upward into a hidden state node \(h\), which feeds upward into an output node \(y\). Hidden states are connected horizontally from left to right, showing recurrence over time: \(h_1 \rightarrow h_2 \rightarrow h_3 \rightarrow \cdots \rightarrow h_T\). Each time step produces an output \(y\), illustrating a many-to-many sequence mapping.

# Other Options for Many-to-One

- CNN

  Diagram: \(T \times D\) input → Conv → Pool → Conv → Pool → \(T \times M\) output

- RNN

  Diagram: A sequence of input nodes labeled \(x\) feed upward into hidden nodes labeled \(h\). The hidden nodes are connected left-to-right as recurrent hidden states labeled \(h_1\), \(h_2\), \(h_3\), ..., \(h_T\), with upward output arrows from each hidden node.

  Also \(T \times M\) output, since we have \(T\) hidden vectors each of size \(M\)

- CNN

  \(T \times D\) input

  **Diagram:** \(T \times D\) input → Conv → Pool → Conv → **Global** Max Pool → Dense

  Callout: In both cases, we reduce \(T \times M\) to \(M\)

- RNN

  **Diagram:** A sequence of recurrent hidden states \(h\) connected left-to-right, labeled \(h_1\), \(h_2\), \(h_3\), ..., \(h_T\). Each hidden state feeds upward into a long **Global** Max Pool layer spanning the entire sequence. The **Global** Max Pool output feeds upward into Dense.

- CNN

  \(T \times D\) input → Conv → Pool → Conv → **Global** Max Pool → Dense

  Callout: In both cases, we reduce \(T \times M\) to \(M\)

- RNN

  Diagram meaning/relationships: a sequence of recurrent hidden states labeled \(h\) passes information left-to-right through time, with state labels \(h_1\), \(h_2\), \(h_3\), ..., \(h_T\). Each hidden state feeds upward into a long **Global Max Pool** layer, which reduces the sequence representations to a single vector. This output feeds upward into Dense, producing Sentiment: negative. The word “Terrible” is highlighted at an early time step, with an orange path indicating its contribution through Global Max Pool to the negative sentiment prediction.

  Labels shown: Dense; Sentiment: negative; **Global** Max Pool; \(h\); \(h_1\); \(h_2\); \(h_3\); ...; \(h_T\); “Terrible”; ...

# Stacking RNN Layers

- Note: one common mistake is confusing \(T\) with \(M\)
- The **sequence length (\(T\))** is not the same as the **size of the hidden vectors (\(M\))**  
  (each circle does not represent a scalar)
- Normally we would not vary the size of the hidden layers (e.g. normally \(M_1 = M_2\))

**Figure:** A stacked RNN diagram showing a vertical flow from input \(x\) to hidden layer \(h\) to hidden layer \(h'\) to output \(y\). The input \(x\) is labeled \(T \times D\), the first hidden layer \(h\) is labeled \(T \times M_1\), and the second hidden layer \(h'\) is labeled \(T \times M_2\). The hidden layers \(h\) and \(h'\) each have recurrent connections over time, indicated by looped arrows with black square delay markers.

# RNN in Tensorflow

```text
i = Input(shape=(D,))
x = Dense(M, activation=’relu’)(i)
x = Dense(K)(x)
model = Model(i, x)
```

**Diagram:** A feed-forward network with nodes `x` → `h` → `y`. The lower node `x` points upward to hidden node `h`, which points upward to output node `y`.

```text
i = Input(shape=(T, D))
x = SimpleRNN(M)(i)
x = Dense(K)(x)
model = Model(i, x)
```

**Diagram:** A recurrent neural network with nodes `x` → `h` → `y`. The input node `x` points upward to hidden node `h`, which points upward to output node `y`. The hidden node `h` also has a recurrent self-loop, shown as a loop returning to `h` with a black square indicating the recurrent connection/delay.

# Output: Many-to-One

```python
i = Input(shape=(T, D))
x = SimpleRNN(M)(i)
x = Dense(K)(x)
model = Model(i, x)
```

## Diagram/Figure

- **many to one**
- **Input:** $\{x_1, x_2, \ldots, x_T\}$  
  $(T \times D)$
- **Produces** $\{h_1, h_2, \ldots, h_T\}$, **but only** $h_T$ **is kept** $(M)$
- **Output:** $y_T$ $(K \text{ vector})$

The figure shows a many-to-one RNN: an input sequence $\{x_1, x_2, \ldots, x_T\}$ feeds into recurrent hidden states $\{h_1, h_2, \ldots, h_T\}$ over time. Although hidden states are produced at each time step, only the final hidden state $h_T$ is kept and passed upward to produce the final output $y_T$, a $K$ vector.

# Output: Many-to-Many

```python
i = Input(shape=(T, D))
x = SimpleRNN(M, return_sequences=True)(i)
x = Dense(K)(x)
model = Model(i, x)
```

## Diagram/Figure

The diagram is labeled **many to many**. It shows a recurrent sequence model with multiple time steps: input vectors at each time step feed upward into hidden states, hidden states are connected horizontally across time, and each hidden state feeds upward to an output at the corresponding time step.

- Produce \(\{y_1, y_2, \ldots, y_T\}\) \((T \times K)\)
- Produce \(\{h_1, h_2, \ldots, h_t\}\), and keep everything \((T \times M)\)

# Output: Many-to-Many

```python
i = Input(shape=(T, D))
x = SimpleRNN(M, return_sequences=True)(i)
x = Dense(K)(x)
model = Model(i, x)
```

The Dense layer “knows” how to  
handle a single vector and a time  
series of vectors as input

**Diagram/figure:** A many to many recurrent model shows a sequence of inputs feeding a sequence of recurrent hidden states, with connections between hidden states across time. Keeping all hidden states produces \(\{h_1, h_2, \ldots, h_T\}\), and keep everything \((T \times M)\). A Dense layer then produces \(\{y_1, y_2, \ldots, y_T\}\) \((T \times K)\).

# Output: Many-to-One (another way)

```python
i = Input(shape=(T, D))
x = SimpleRNN(M, return_sequences=True)(i)
x = GlobalMaxPooling1D()(x)
x = Dense(K)(x)
model = Model(i, x)
```

**Diagram/Figure:** A “many to one” diagram shows multiple input time steps feeding into recurrent outputs, followed by a **GlobalMaxPool** layer that reduces the sequence of outputs into a single output vector. A callout states: “Output again is a vector of size M”.

# Stacking Layers

```python
i = Input(shape=(T, D))
x = SimpleRNN(32, return_sequences=True)(i)
x = SimpleRNN(32)(x) # default is return_sequences=False
x = Dense(K)(x)
model = Model(i, x)
```

**many to many stacked**

Diagram: A stacked recurrent network is shown across three time steps. Bottom input blocks feed upward into a first recurrent layer, which feeds upward into a second recurrent layer. Horizontal arrows connect recurrent units across time within each layer, and vertical arrows connect lower-layer outputs to upper-layer inputs. The final upper recurrent unit feeds upward into a single output block.

# Easy to Use LSTMs and GRUs (Preview)

```python
i = Input(shape=(T, D))
x = LSTM(M)(i)
x = Dense(K)(x)
model = Model(i, x)
```

```python
i = Input(shape=(T, D))
x = GRU(M)(i)
x = Dense(K)(x)
model = Model(i, x)
```

# Modern RNN Units

- LSTM - Long Short-Term Memory
- GRU - Gated Recurrent Unit
- GRU is like a simplified version of the LSTM (less parameters and thus more  
  efficient)

**Figure: LSTM**

An unrolled recurrent network diagram labeled **LSTM**. A previous recurrent block **A** receives input $x_{t-1}$ and outputs hidden state $h_{t-1}$. Its state flows into a central detailed LSTM unit at time $t$, which receives input $x_t$ and uses gates labeled $\sigma$, $\sigma$, $\tanh$, and $\sigma$ with multiplication nodes $\times$, an addition node $+$, and a $\tanh$ activation to control information flow. The central LSTM outputs hidden state $h_t$ upward and passes state/hidden connections to the next recurrent block **A**, which receives input $x_{t+1}$ and outputs hidden state $h_{t+1}$.

# Limitations of Vanilla RNNs

- While RNNs can capture word order and dependencies, they have their own issues:
  - **Vanishing gradients:** Difficult to learn long-range dependencies (early inputs get "forgotten")
  - **Slow to train:** Because each step depends on the previous one, RNNs are <span style="color:red">not parallelizable</span>

Vanishing gradients: https://www.youtube.com/watch?v=8z3DFk4VxRo

# How Does the Problem Manifest?

- Ask your simple RNN: “On what day was Albert Einstein born?”
- By the time the RNN has “read” the whole article, it forgot what was at the beginning!

**Figure:** A screenshot of the Wikipedia article for **Albert Einstein**. The opening paragraph includes Einstein’s birth and death dates, with **“14 March 1879 – 18 April 1955”** highlighted in green. The figure illustrates that the answer to the question appears near the beginning of a long article, but a simple RNN may forget this early information by the time it processes the entire text.

Visible text in figure:

**Albert Einstein**

From Wikipedia, the free encyclopedia

“Einstein” redirects here. For other people, see Einstein (surname). For other uses, see Albert Einstein (disambiguation) and Einstein (disam...

Albert Einstein (/ˈaɪnstaɪn/ EYEN-styne;[4] German: [ˈalbɛɐ̯t ˈʔaɪnʃtaɪn] (listen); 14 March 1879 – 18 April 1955) was a German-born theoretical physicist[5] who developed the theory of relativity, one of the two pillars of modern physics (alongside quantum mechanics).[3][6]:274 His work is also known for its influence on the philosophy of science.[7][8] He is best known to the general public for his mass–energy equivalence formula $E = mc^2$, which has been dubbed "the world's most famous equation".[9] He received the 1921 Nobel Prize in Physics "for his services to theoretical physics, and especially for his discovery of the law of the photoelectric effect",[10] a pivotal step in the development of quantum theory.

# Gated Recurrent Unit (GRU)

- First and foremost, it has the same “API” as the simpleRNN

**Diagram description:** Two stacked block diagrams compare `SimpleRNN` and `GRU`. In both diagrams, \(x(t)\) and \(h(t-1)\) enter the block from the left, and \(h(t)\) exits to the right. This conveys that both `SimpleRNN` and `GRU` take the same inputs and produce the same output.

Top diagram:

\[
x(t),\ h(t-1) \rightarrow \text{SimpleRNN} \rightarrow h(t)
\]

Bottom diagram:

\[
x(t),\ h(t-1) \rightarrow \text{GRU} \rightarrow h(t)
\]

# GRU

Simple RNN unit, for comparison

$$
h_t = \tanh(W_{xh}^{T} x_t + W_{hh}^{T} h_{t-1} + b_h)
$$

$$
z_t = \sigma(W_{xz}^{T} x_t + W_{hz}^{T} h_{t-1} + b_z)
$$

$$
r_t = \sigma(W_{xr}^{T} x_t + W_{hr}^{T} h_{t-1} + b_r)
$$

$$
h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tanh(W_{xh}^{T} x_t + W_{hh}^{T}(r_t \odot h_{t-1}) + b_h)
$$

# GRU

Simple RNN unit, for comparison

$$
h_t = \tanh(W_{xh}^{T}x_t + W_{hh}^{T}h_{t-1} + b_h)
$$

$$
z_t = \sigma(W_{xz}^{T}x_t + W_{hz}^{T}h_{t-1} + b_z)
$$

$$
r_t = \sigma(W_{xr}^{T}x_t + W_{hr}^{T}h_{t-1} + b_r)
$$

$$
h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tanh(W_{xh}^{T}x_t + W_{hh}^{T}(r_t \odot h_{t-1}) + b_h)
$$

Diagram/figure: A rounded rectangle defines the symbols used in the GRU equations:

z(t) = update gate vector  
r(t) = reset gate vector  
h(t) = hidden state

# GRU

- z(t), r(t), h(t) are all vectors of size M
- M is a hyperparameter (“number of hidden units / features”)
- This implies the shape of all the weights
- Any weight going from x(t) is D x M
- Any weight going from h(t) is M x M
- All bias terms are of size M

$$
z_t = \sigma(W_{xz}^{T}x_t + W_{hz}^{T}h_{t-1} + b_z)
$$

$$
r_t = \sigma(W_{xr}^{T}x_t + W_{hr}^{T}h_{t-1} + b_r)
$$

$$
h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tanh(W_{xh}^{T}x_t + W_{hh}^{T}(r_t \odot h_{t-1}) + b_h)
$$

# What is the GRU Doing?

- z(t) = update gate vector
- “Should I take the new value for h(t), or should I keep the old value, h(t-1)?”
- Vanishing gradient means the RNN forgets things in the past
- Now, we can explicitly remember the previous h(t-1) (If z(t) small)
- If z(t) → 1, then forget h(t-1)

\[
z_t = \sigma(W_{xz}^{T}x_t + W_{hz}^{T}h_{t-1} + b_z)
\]

\[
r_t = \sigma(W_{xr}^{T}x_t + W_{hr}^{T}h_{t-1} + b_r)
\]

\[
h_t = (1 - z_t)\odot h_{t-1} + z_t \odot \tanh(W_{xh}^{T}x_t + W_{hh}^{T}(r_t \odot h_{t-1}) + b_h)
\]

**Figure/diagram description:** The equations illustrate the GRU update. The update gate \(z_t\) controls how much of the previous hidden state \(h_{t-1}\) is kept versus how much of the new candidate hidden value is used. The reset gate \(r_t\) controls how much of \(h_{t-1}\) contributes to the candidate hidden state. The terms \((1 - z_t)\odot\) and \(z_t \odot\) are highlighted with green boxes to emphasize the interpolation between keeping the old hidden state and taking the new candidate value.

**Thought bubble:** Circle with a dot is element-wise multiplication

# Interpreting the GRU

- (Forget about the reset gate for now)

\[
h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tanh(W_{xh}^{T}x_t + W_{hh}^{T}(r_t \odot h_{t-1}) + b_h)
\]

\[
h_t = p(keep\ h_{t-1})h_{t-1} + p(discard\ h_{t-1})SimpleRNN(x_t, h_{t-1})
\]

Diagram/figure: Light gray arrows connect parts of the GRU equation to the interpretive equation below: \((1 - z_t)\) corresponds to \(p(keep\ h_{t-1})\), \(h_{t-1}\) corresponds to \(h_{t-1}\), \(z_t\) corresponds to \(p(discard\ h_{t-1})\), and the \(\tanh(\cdots)\) candidate update term corresponds to \(SimpleRNN(x_t, h_{t-1})\).

# Reset Gate

- Reset gate → whether to look up old data when generating new hidden state
- Update gate → whether to update the database now

$$
r_t = \sigma(W_{xr}^{T}x_t + W_{hr}^{T}h_{t-1} + b_r)
$$

$$
h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tanh(W_{xh}^{T}x_t + W_{hh}^{T}(r_t \odot h_{t-1}) + b_h)
$$

The figure highlights \(r_t\) in the term \((r_t \odot h_{t-1})\), showing that the reset gate controls how much of the previous hidden state \(h_{t-1}\) is used when generating the new hidden state.

# LSTM (Long Short-Term Memory)

- Think of it as “like the GRU” but with more state vectors and gates

## Figure: RNN, LSTM, GRU comparison

The figure compares three recurrent neural network cell structures:

### RNN

A simple recurrent cell where the previous hidden state $h_{t-1}$ and current input $x_t$ are combined and passed through a $\tanh$ activation to produce the current hidden state $h_t$ and output $o_t$.

Labels shown: RNN, $h_{t-1}$, $x_t$, $\tanh$, $o_t$, $h_t$

### LSTM

An LSTM cell with more state vectors and gates. It maintains a cell state flowing from $C_{t-1}$ to $C_t$, controlled by gates:

- forget gate $f_t$
- input gate $i_t$
- candidate cell state $\tilde{C}_t$
- output gate $o_t$

The cell uses $\sigma$, $\tanh$, multiplication gates, and addition to update the cell state $C_t$ and produce the hidden state $h_t$.

Labels shown: LSTM, $C_{t-1}$, $C_t$, $h_{t-1}$, $h_t$, $x_t$, $f_t$, $i_t$, $\tilde{C}_t$, $o_t$, $\sigma$, $\tanh$

### GRU

A GRU cell with fewer gates than the LSTM. It uses the previous hidden state $h_{t-1}$ and input $x_t$, with:

- reset gate $r_t$
- update gate $z_t$
- candidate hidden state $\tilde{h}_t$

The update combines $(1 - z_t)$ and $z_t$ pathways using multiplication and addition to produce $h_t$.

Labels shown: GRU, $h_{t-1}$, $h_t$, $x_t$, $r_t$, $z_t$, $\tilde{h}_t$, $\sigma$, $\tanh$, $1-$

# GRU vs LSTM

- Not exactly the same API
- LSTM returns 2 states:
  - Hidden state $h(t)$
  - Cell state $c(t)$ (usually ignored)
  - Also means you need 2 initial states: $c_0$ and $h_0$

## Diagram/Figure

The figure compares the inputs and outputs of a GRU cell and an LSTM cell.

- **GRU**:
  - Inputs: $x(t)$ and $h(t-1)$
  - Output: $h(t)$
  - The GRU takes the current word and previous hidden state, and returns one hidden state.

- **LSTM**:
  - Inputs: $x(t)$, $h(t-1)$, and $c(t-1)$
  - Outputs: $h(t)$ and $c(t)$
  - The LSTM takes the current word, previous hidden state, and previous cell state, and returns both a hidden state and a cell state.

Red annotations between the diagrams indicate:

- Current word
- Short-term memory
- Long-term memory

# LSTM Equations

\[
f_t = \sigma(W_{xf}^{T}x_t + W_{hf}^{T}h_{t-1} + b_f)
\]

Forget gate

\[
i_t = \sigma(W_{xi}^{T}x_t + W_{hi}^{T}h_{t-1} + b_i)
\]

Input/update gate

\[
o_t = \sigma(W_{xo}^{T}x_t + W_{ho}^{T}h_{t-1} + b_o)
\]

Output gate

\[
c_t = f_t \odot c_{t-1} + i_t \odot f_c(W_{xc}^{T}x_t + W_{hc}^{T}h_{t-1} + b_c)
\]

tanh

\[
h_t = o_t \odot f_h(c_t)
\]

tanh

“Simple RNN”

Diagram/figure description: Gray arrows label the first three equations as the Forget gate, Input/update gate, and Output gate. Another gray arrow labeled “Simple RNN” points to the candidate update term \(f_c(W_{xc}^{T}x_t + W_{hc}^{T}h_{t-1} + b_c)\), indicating the simple recurrent computation used inside the LSTM cell update. Red “tanh” labels indicate that \(f_c\) and \(f_h\) are tanh nonlinearities.

# Why Output Gate?

- 為何不直接將\(c_t\)的值輸出作為\(h_t\)?
- 長期記憶通常包含豐富且雜亂的資訊，直接輸出的話下一層會被迫接收大量當下根本不需要的雜訊
- Ex: “<span style="color:red">Alice</span> 是一個非常優秀的工程師，我昨天在會議上遇到<span style="color:red">她</span>” (translation task)
  - 當模型讀到Alice時，\(c_t\)會記住兩個特徵：女性、單數
  - 當模型讀到“是一個非常優秀的工程師 …”時，後面的預測層根本不需要知道 Alice 是女性這件事
  - 這時，output gate會關閉對於性別特徵的輸出，不讓它干擾當下的語意判斷
  - 直到最後讀到”遇到...”，準備要預測代名詞時，output gate才會打開，把\(c_t\)裡的”女性”特徵釋出到\(h_t\)，讓模型能夠預測出“her。

# LSTM is Simple

\[
f(t) = \text{Neuron (binary classifier)}
\]

\[
i(t) = \text{Neuron (binary classifier)}
\]

\[
o(t) = \text{Neuron (binary classifier)}
\]

\[
c(t) = f(t) * c(t-1) + i(t) * \text{SimpleRNN}
\]

\[
h(t) = o(t) * \tanh(c(t))
\]