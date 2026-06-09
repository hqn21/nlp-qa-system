# Vector-Based Models

# Vector Models & Text Preprocessing

- We want to study how Machine Learning is applied to language
- However, ML works on <span style="color: #3b73ff;">numbers</span>, and language is made of text
- How to convert language to numbers, so that ML can be applied?
- **Text Preprocessing!**

# Basic Definitions

- Sentence: a sequence of words
- Ex: In English, a sentence typically begins with a capital letter and ends with punctuation (e.g. period, question mark)

Sentence: I love dogs.

# Tokens

- We may also consider a sentence to be a sequence of tokens
- Tokens can be words, but can also be punctuation, or sub-unit of words
- Note: it is common to use “tokens” in replace of “words”

Sentence: I love dogs.  
Tokens: [I, love, dogs, .]

# Letters and Characters

- English is made up of 26 lettes (A-Z)
- A more general term: “character”
- Characters can represent punctuation and whitespace too (e.g. “\n”)
- In C++, Java, and others, the “character” is a fundamental data type
- Sometimes, NLP models will be build on words, but other times, they will be in terms of characters

```cpp
#include<iostream>
using namespace std;
int main()
{
    char name[200][20];
    cin >> name[0] >> name[1] << na
    cout << name[0] << '\t' << name[1];
    return 0;
}
```

Figure: A screenshot of C++ code illustrating the use of `char` as a fundamental data type, including a two-dimensional character array `char name[200][20];`, input into `name[0]` and `name[1]`, and output of those character arrays separated by a tab.

# Vocabulary

- Vocabulary: the set of “all” words
- In most cases, vocabulary won’t contain every possible word, but rather, just a “reasonable” subset of words
- How many to keep? 1000s? 10k’s? 100k’s? 1M’s?
- Depends on your application!
- Unless you are using a pretrained model (has been decided)

[Figure: A word cloud related to vocabulary, with prominent words including “vocabulary,” “words,” “English,” “word,” and other smaller related terms, illustrating a collection of words in a vocabulary.]

# Corpus

- “A large collection of writings of a specific kind or on a specific subject”
- Here, it will simply refer to our ML <span style="color:red">dataset</span>

**Diagram/Figure:** A progression from smaller to larger text units: Token → Sentence → Paragraph → Document → Corpus. The figure illustrates that tokens combine to form sentences, sentences combine to form paragraphs, paragraphs form documents, and multiple documents make up a corpus. Labels shown: Token, Sentence, Paragraph, Document, Corpus.

# N-Gram

- Refers to N consecutive items (e.g. words, subwords, characters)
- Single item: unigram
- Two items: bigram
- Three items: trigram

| Text | N-gram |
|---|---|
| Data | 1-gram |
| Great information | 2-gram |
| I am fine | 3-gram |
| Nice to meet you | 4-gram |

# What is a Vector?

- Vectors are how we will represent text numerically
- An array of scalars (e.g. \((3, 4)\))
- Vectors can have 100s or 1000s of dimensions
- They are also the foundation of many ML techniques

**Figure:** A 2D coordinate plane with x- and y-axes labeled from approximately -6 to 6. A red arrow starts at the origin \((0, 0)\) and points up and to the right toward approximately \((3, 4)\), illustrating a vector as a directed quantity with components along the x and y dimensions.

# Why are Vectors Useful?

- To imagine why vectors are useful, think about  what you would do if you did not use vectors
- Task: *write a computer program that takes an email as input, and output whether or not the email is spam*
- What would you do?
  - Keywords
- If the email contains “Nigerian Prince”, “insurance”, “credit”, “make money”, etc. mark it as spam

# Why are Vectors Useful?

- What if you are interested in courses about computing credit score? You cannot filter on the word “credit”
- What if you taking a course on NLP, and the instructor uses the “Nigerian Prince” example? You cannot filter this phrase either
- What conditions makes an email safe? (NCHU?) Spammer can still send fake emails pretending to be from NCHU
- Overall problems: <span style="color: #4285F4;">what to do if rules conflict?</span>
- That’s why we need ML (data-driven automated decision-making)

# Spam Detection with Vectors

- Supose there is a way to map text into vectors, such that the vector for each class fall into their own clusters
- Then we can simply draw a line between the 2 clusters

**Figure:** A 2D scatter plot shows two distinct clusters of points: a red cluster in the upper-left/center region and a blue cluster in the lower-right region. A diagonal gray line separates the two clusters, illustrating a decision boundary between the two classes.

# Spam Detection with Vectors

- Supose there is a way to map text into vectors, such that the vector for each class fall into their own clusters
- Then we can simply draw a line between the 2 clusters

- Suppose we have a new email whose spam status is unknown
- The question now is simple: which side of the line is it on?

**Figure/diagram description:** A 2D scatter plot shows two clusters of vectors: red points clustered in the upper-left region and blue points clustered in the lower-right region. A diagonal gray line separates the two clusters, representing a decision boundary between the two classes. A gray arrow from the callout box points to a teal circular point near the lower-right side of the plot, representing a new email with unknown spam status; the classification question is determined by which side of the separating line this point lies on.

# Organizing Documents

- Suppose a company has a large collection of document that needs to be organize, but there are way too many to read one-by-one
- We can automate this using **Clustering**
- But only if we convert the documents to vectors first

**Figure:** A scatter plot showing documents represented as points in vector space, grouped into five visually distinct clusters. The legend labels the clusters as Cluster 0, Cluster 1, Cluster 2, Cluster 3, and Cluster 4. Each cluster is shown in a different color, illustrating how clustering organizes similar document vectors into separate groups.

# Is it Possible?

- In reality, our vectors will not be so nicely separated

## Figure

A scatter plot with red and blue points distributed throughout the same 2D space, showing that the two groups are not cleanly separated. The x-axis ranges from 0.0 to 1.0, and the y-axis ranges from 0.0 to 1.0. A callout points to the mixed scatter plot and states:

> What we do **not** want.
>
> Our objective will be to  
> convert text into vectors  
> *intelligently*.

# Bag of Words

- Text is <span style="color: blue;">sequential</span>, the specific sequence of words gives the text meaning
- If we <span style="color: blue;">randomized</span> the words in a sentence, we would change its meaning, or more likely, make it incomprehensible
- Despite this, many NLP approaches do not consider word order
- We will call this “bag of words” representations

**Figure:** A paper bag labeled “WORDS,” representing the “bag of words” concept where words are treated as an unordered collection.

# Order Matters: Example

**Figure:** The slide contrasts two phrases where word order changes meaning:

- **Dog Toy**: A blue chew toy intended for a dog, shown with a dog.
- **Toy Dog**: A stuffed/plush dog toy.

# Where is Bag of Words Used?

- Vector models and classic ML models use bag of words
- Probabalistic models and deep learning do not
- This is just a rough categorization: we can still find probabilistic and neural
  models that also use bag of words

**Diagram/Figure:** A hand-drawn diagram shows a **Document** containing ordered text: “LDA is a great tool for summarizing text!” with the note “Ordered Text.” An arrow points from the document to a tied bag labeled **Bag of Words**, containing the same words in unordered positions, with the note “Unordered Text.” The relationship conveyed is that a document’s ordered sequence of words is transformed into a bag of words representation where word order is ignored.

# Count Vectorizer

- This method is simply called counting
- It is a “bag of words” approach
- Consider a simple classification task: discriminate between documents about biology and documents about physics

# Data Format

- Excel spreadsheet / CSV / Pandas dataframe (pre-requisite)

| Text (Inputs) | Labels (Targets) |
|---|---|
| Ad sales boost Time Warner profit\n\nQuarterly... | business |
| Dollar gains on Greenspan speech\n\nThe dollar... | politics |
| Yukos unit buyer faces loan claim\n\nThe owner... | entertainment |
| High fuel prices hit BA's profits\n\nBritish A... | finance |
| Pernod takeover talk lifts Domecq\n\nShares in... | business |

# Data Format

- Excel spreadsheet / CSV / Pandas dataframe

> Our first goal is to convert the inputs  
> to numerical values (vectors) for ML  
> models

| Text (Inputs) | Labels (Targets) |
|---|---|
| Ad sales boost Time Warner profit\n\nQuarterly... | business |
| Dollar gains on Greenspan speech\n\nThe dollar... | politics |
| Yukos unit buyer faces loan claim\n\nThe owner... | entertainment |
| High fuel prices hit BA's profits\n\nBritish A... | finance |
| Pernod takeover talk lifts Domecq\n\nShares in... | business |

*Figure/diagram description: A red rectangular outline highlights the “Text (Inputs)” column of the table, indicating these text inputs are the data to be converted into numerical values (vectors) for ML models. The adjacent “Labels (Targets)” column provides the corresponding target categories for each input row.*

# Determining Vocabulary Size

- Let $V$ = number of unique words in training corpus
- Each document will be converted into a vector of size $V$
- The vector components will contain the counts for each word

| 0 | 0 | 25 | ... | 0 | 3 |
|---|---|---:|---|---|---:|
| "a" | "aa" | "and" | ... | "zoo" | "zygote" |

> This means "and" appears in the document 25 times

> An example vector

The diagram shows an example vector where each numeric component in the top row corresponds to the vocabulary word beneath it. The component for `"and"` has value `25`, meaning `"and"` appears in the document 25 times. The component for `"zygote"` has value `3`, while `"a"`, `"aa"`, and `"zoo"` have value `0`. The `...` indicates omitted intermediate vocabulary entries and their corresponding counts.

# A Simple Example

- $V$ (vocabulary size) = 6

| Original Documents |
|---|
| I like eggs |
| I hate cats |
| I like eggs and I like cats |

→

| and | cats | eggs | hate | I | like |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 0 | 2 | 2 |

Each row is a vector of size 6

Diagram/figure meaning: The original documents table is transformed by the arrow into a document-term count matrix. The columns are the vocabulary terms `and`, `cats`, `eggs`, `hate`, `I`, and `like`; each document becomes one row, where each number is the count of that vocabulary term in the corresponding original document.

# How Does Counting Help?

- Given a new document, count up # Mitochondria, # Gravity, plot it on this graph, and determine which side of the line the vector falls on!

## Diagram/Figure

A scatter plot with the x-axis labeled **Gravity** and the y-axis labeled **Mitochondria**. A thick diagonal line runs from the bottom-left corner to the top-right corner, acting as a decision boundary.

- A red cluster of points in the upper-left region is labeled **Biology**.
- A blue cluster of points in the lower-right region is labeled **Physics**.
- A light blue point representing a new document appears above the diagonal line, between the two clusters.
- An arrow from the bullet text points to this light blue point, indicating that the new document is plotted by counting **# Mitochondria** and **# Gravity**, then classified based on which side of the diagonal line it falls on.

# CountVectorizer in Code (Scikit-Learn)

```python
vectorizer = CountVectorizer()

vectorizer.fit(list_of_documents_train)

Xtrain = vectorizer.transform(list_of_documents_train)

# all in one step

Xtrain = vectorizer.fit_transform(list_of_documents_train)

Xtest = vectorizer.transform(list_of_documents_test)
```

# Normalization

- What if our corpus has very long and very short documents?
- Count vectors will have size disparities (more words = higher counts)

> Method 1: Make the L2-norm 1

$$
\hat{x} = \frac{x}{\lVert x \rVert_2}, \ where \ \lVert x \rVert_2 = \sqrt{\sum_{i=1}^{V} x_i^2}
$$

**Diagram/Figure description:** A callout labeled “Method 1: Make the L2-norm 1” points to the normalization formula, showing that the vector \(x\) is divided by its L2 norm so that the resulting vector \(\hat{x}\) has L2-norm 1.

> Method 2: Divide by the sum (can think  
> of each element as a probability)

$$
\hat{x} = \frac{x}{\sum_{i=1}^{V} x_i}
$$

**Diagram/Figure description:** A callout labeled “Method 2: Divide by the sum (can think of each element as a probability)” points to the formula showing that the vector \(x\) is divided by the sum of its elements, producing normalized values interpretable as probabilities.

# Before Normalization  
## (Length Varies)

**Diagram description:** A 2D coordinate plot with x-axis labeled **Word 1 Count** and y-axis labeled **Word 2 Count**. Two document vectors start at the origin. The blue **Doc A Vector (Short Text)** points to \((3, 4)\) and has \(L_2\)-norm \(= 5\). The red **Doc B Vector (Long Text)** points to \((10, 20)\) and has \(L_2\)-norm \(= 22.36\). The diagram conveys that before normalization, document vectors can have different lengths depending on document length.

- **Word 2 Count**
  - 20
  - 15
  - 10
  - 5
- **Word 1 Count**
  - 5
  - 10
- \(L_2\)-norm \(= 22.36\)
- \(L_2\)-norm \(= 5\)
- \((3, 4)\)
- \((10, 20)\)
- **Doc A Vector**  
  **(Short Text)**
- **Doc B Vector**  
  **(Long Text)**

# Normalization Process:

**Diagram description:** A right-pointing arrow connects the “Before Normalization” plot to the “After Normalization” plot. The arrow indicates that each vector is divided by its own \(L_2\)-norm length.

Divide by its own  
\(L_2\)-norm length

# After Normalization  
## (Make L2-norm 1)

**Diagram description:** A 2D coordinate plot with a unit circle centered at the origin. Both document vectors start at the origin and end on the unit circle, showing that after normalization all vectors have length 1. The red vector is labeled \((0.45, 0.89)\), corresponding to the normalized version of \((10, 20)\). The blue vector is labeled \((0.6, 0.8)\), corresponding to the normalized version of \((3, 4)\). Both vectors are labeled \(L_2\)-norm \(= 1\), conveying that normalization preserves direction while making lengths uniform.

- \((0.45, 0.89)\)
- \((0.6, 0.8)\)
- \(L_2\)-norm \(= 1\)
- \(L_2\)-norm \(= 1\)

**Result:** All document vectors now have a  
uniform length of 1, enabling fair comparison  
(e.g., cosine similarity) regardless of  
original document length.

# Tokenization

- Tokenization: splitting strings into tokens
- Basic approach: s.split() → ["I", "like", "cats"]
- Better approach: Use NLP libraries (SpaCy, NLTK)

| Method | Output |
|---|---|
| s.split() | ["I", "like", "cats."] |
| NLTK word\_tokenize() | ["I", "like", "cats", "."] |
| SpaCy Tokenizer | ["I", "like", "cats", "."] |

# Tokenization: Words-Based VS. Character-Based

<span style="color:red">Cons</span> of word-based tokenization:

- Up to 1 million words (hence, 1 million dimensions)
- Must have # outputs equal to vocabulary size (1 million dimension probability distribution)
- This corresponds to a very large weight matrix

<span style="color:green">Pros</span> of word-based tokenization:

- Words have meaning / contain lots of information

# Tokenization: Words-Based VS. Character-Based

<span style="color:red">Cons</span> of charater-based tokenization:

- Characters do not contain lots of information

<span style="color:green">Pros</span> of character-based tokenization:

- In English, there are only 26 letters, + some characters for white space and punctuation
- Thus, the “vocabulary” size is small, easy to represent in a computer

# Subword-Based Tokenization

- A middle ground between word-based and character-based
- Ex: “walking” → “walk” + “ing”
- “Walk” is closely related to “walking” - we’d like them to have some shared representation in our model (via the token “walk”)
- “ing” is a meaningful token - it has the same meaning whether it’s applied to “walking”, “eating”, etc.

# Subword-Based Tokenization

- What if we didn’t split “walking” into “walk” + “ing”?
- Each vector component (count) is separate, so “walk” is no closer to “walking” than it is to “tree”
- We can only hope our model learn the similarity through the data
- Do we want our model to learn “walk”, “walks”, “walking”, “walked”, etc. independently? Or should we connect them via a shared representation?

# In Scikit-Learn

## Word-based tokenization

```text
CountVectorizer(analyzer="word")
```

## Character-based tokenization

```text
CountVectorizer(analyzer="char")
```

# Punctuation

- Punctuation may be important for downstream NLP tasks
- Ex: “I hate cats.” vs. “I hate cats?”
- Tokenizing punctuation: “I hate cats?” → [“I”, “hate”, “cats”, “?”]
- Should you use it? Thats dependent on your experimental results
  - Sentiment analysis → Yes (affect meaning)
  - Topic modeling → No (add noise)
- Note: SKLearn CountVectorizer ignores punctuation

# Casing

- Consider sentiment analysis or spam detection
- Does “cat” have the same meaning as “Cat”?
- Simply call `string.lower()` in Python
- With SKLearn: `CountVectorizer(lowercase=True)`

# Accents

- Less common in English
- “Naive” and “Náive” are both correct
- Map the character yourself, or use

  `CountVectorizer(strip_accents=True)`

# Stopwords

- What we know so far: how to build vector using counting
- Tokenization → Count the tokens → Put them into a vector

[Figure: A red octagonal stop sign with the word “STOP” in large white letters, indicating a halt or stopping point before proceeding.]

# Why do We Need Stopwords?

- When we perform counting procedure, what happen with very common words? such as “and”, “the”, “it”, “is”, etc.
- Are these words useful?
- Any text will contain these words

**Figure:** A word cloud showing very common words appearing prominently, including “the”, “and”, “to”, “Twitter”, “PubMed”, “for”, “on”, “that”, and “Search”, illustrating that frequent stopwords can dominate text-counting results.

# Dimensionality

- High dimensionality is bad
- More dimensions → more computation
- Could it be beneficial to simply not include stopwords?

[Figure: A colorful clustered scatter/embedding visualization with many small labeled points (letters/numbers) forming several distinct groups. The figure illustrates high-dimensional data projected into a lower-dimensional space, showing clusters and relationships among points.]

# Distance Consideration

- Recall that our understanding of feature vectors involves theirs distance to each other
- If we count all the “and”s, “the”s, etc. <span style="color:red">the vectors which will be close will simply by the ones with similar numbers of these words</span>
- The might overshadow more important words, like “mitochondria” or “voltage”
- Thus, **stopwords** are the words we wish to ignore

**Figure:** A scatter plot shows multiple colored clusters of points (blue, yellow, green, and red), each grouped around a central marked point. Lines extend from or between clusters, indicating distances or decision boundaries/relationships among groups in feature-vector space.

# Stopwords in CountVectorizer

```python
CountVectorizer(stop_words=”english”)

CountVectorizer(stop_words=list_of_user_defined_words)

CountVectorizer(stop_words=None) # default
```

# NLTK Stopwords

```python
import nltk

nltk.download(‘stopwords’)

from nltk.corpus import stopwords


stopwords.words(‘english’)

stopwords.words(‘german’)
```

> 中文需使用 jieba 或 CKIP 進行  
> tokenization, 並使用自定義的停用詞表

# Stemming & Lemmatization

- With basic word tokenization, each variation of a word will have its own vector component: “walk”, “walking”, “walks”, “walked”, …
- “Walk” is no closer to “walking” than it is to “cartwheel” (unless similarity can be learned from the data)
- This also leads to high-dimensional vectors
- Practical issue: imagine we’re building a search engine, and search for “running” (what about “ran” and “run”? How to match them?)
- Solution: convert words to their root word
- 2 methods: stemming and lemmatization

# Stemming & Lemmatization

- Stemming is very **crude** - it just cut off the end of the word
- The result is not necessarily a real word
- Lemmatization is more **sophisticated** - it uses actual rules of language
- The true root word will be returned

# Stemming

- Based on single heuristics
- Ex: ends with “sses” → remove “es”
- Ex: “Bosses” → “Boss”
- Ex: “Replacement” → “Replac”
- Multiple stemming algorithms
  - Porter Stemmer
  - Lancaster Stemmer
  - Snowball Stemmer

```python
from nltk.stem import PorterStemmer

porter = PorterStemmer()

porter.stem(“walking”) # returns “walk”
```

# Lemmatization

- Think of it as a lookup table
- Stemming: “Better” → “Better”
- Lemmatization: “Better” → “Good”
- Note: “Was” is the past-tense of “Is”, both are derivatives of “Be”
- Stemming: “Was” → “Wa”
- Lemmatization: “Was” / “Is” → “Be”
- Stemming: “Mice” → “Mice”
- Lemmatization: “Mice” → “Mouse”

# How to Use Lemmatization

- Appear in NLTK, spaCy, and others

```python
from nltk.stem import WordNetLemmatizer

from nltk.corpus import wordnet
nltk.download("wordnet") # only need to do once

lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("mice") # returns 'mouse'

lemmatizer.lemmatize("going") # returns 'going'
lemmatizer.lemmatize("going", pos=wordnet.VERB) # returns 'go'
```

**Figure/annotation:** A red rectangle highlights `pos=wordnet.VERB`, showing that specifying the part of speech as a verb changes the lemmatization of `"going"` from returning `'going'` to returning `'go'`.

# Why Does the Part-of-Speech Matter?

“Donal Trump has a devoted following”

**Noun**

“The cat was following the bird as it flew by”

**Verb**

**Figure description:** The word “following” is highlighted in both sentences. In “Donal Trump has a devoted following,” “following” is labeled **Noun**. In “The cat was following the bird as it flew by,” “following” is labeled **Verb**. The slide illustrates that the same word can have different parts of speech depending on context.

## Parts of Speech

| Part of Speech | Definition |
|---|---|
| Nouns | A noun is the name of a person, place, thing, or idea. |
| Pronouns | A pronoun takes the place of a noun in a sentence. |
| Verbs | A verb tells what action someone or something is doing or expresses a state of being. |
| Adjectives | An adjective describes a noun or a pronoun. It tells what kind, how many, or which one. |
| Articles | The words a, an, and the are special adjectives called articles. An article is used before a noun. |
| Adverbs | An adverb describes a verb, adjective, or adverb. It tells how, when, where, or to what extent. |
| Prepositions | A preposition describes a relationship between a noun or pronoun and another word in the sentence. |
| Conjunctions | A conjunction joins words or phrases in a sentence. |
| Interjections | An interjection is a word or phrase that expresses strong feeling or emotion. |

# Why Stemming & Lemmatization Still Matter in NLP?

- **Misconception:** Are These Techniques Outdated?
  - Some believe that NLP today is all about “throwing everything at deep learning”—but this approach is <span style="color:red">inefficient and lacks interpretability</span>.

- **Reality:** Stemming & Lemmatization Are Still Essential!
  - These techniques remain crucial preprocessing steps in various NLP applications, such as:
  - Search Engines / Document Retrieval (Google, Bing)
  - Online Advertising (Google Ads, Meta Ads)
  - Social Media Tagging (Twitter, Instagram)

- **Why?**
  - They <span style="color:red">reduce word variations</span>, improve <span style="color:red">text normalization</span>, and enhance <span style="color:red">computational efficiency</span>—helping both traditional NLP models and modern AI systems.

# Vector Similarity

**Diagram:** Two vector inputs, \(a = [0.5, 0.3, \ldots]\) and \(b = [-0.1, 0.2, \ldots]\), both feed into a **Similarity Function** \(s(a, b)\), which outputs a similarity **score = 0.12345**.

- How is it useful? Given some document, find the “most similar” document
- E.g. Researchers looking for papers on a subject
- If we have word vectors: we may find “king” and “queen” are similar
- “Car”, “vehicle”, “automobile” → similar
- “Car”, “giraff” → dismilar

# Euclidean Distance

- In a Euclidean space, we can calculate the straight-line distance between two document vectors.
- While distance can measure similarity, it is sensitive to <span style="color:red">document length</span>.
- For best results, this is often used with normalized vectors.

## Figure: Euclidean Distance

A 2D plot titled **Euclidean Distance** with x-axis labeled \(x\) and y-axis labeled \(y\). Two vectors originate at \((0,0)\):

- A red vector \(\vec{v}_1\) points to \((3,1)\).
- A blue vector \(\vec{v}_2\) points to \((1,2)\).
- A gray line connects the endpoints \((1,2)\) and \((3,1)\), representing the Euclidean distance between the two vectors.
- The distance is annotated as:

\[
\sqrt{5} = \sqrt{(1 - 3)^2 + (2 - 1)^2}
\]

\[
\lVert x - y \rVert_2 = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2 + \ldots + (x_D - y_D)^2}
\]

# Cosine Similarity

## Diagram

- Two nearly parallel arrows point upward to the right, indicating vectors with a very small angle between them.
- A green callout above the arrows reads: **Angle ≈ 0**

## Graph

- A plot of $\cos(\theta)$ versus $\theta$.
- Vertical axis labeled: $\cos(\theta)$
- Horizontal axis labeled: $\theta$
- Vertical axis markings: `1`, `0.5`, `0`, `-1`
- Horizontal axis markings: `60°`, `90`, `180`, `270`, `360`
- The cosine curve starts near `1` at $\theta = 0$, decreases through `0` near `90`, reaches `-1` near `180`, rises through `0` near `270`, and returns to `1` near `360`.
- A dashed red guide indicates that at `60°`, $\cos(\theta) = 0.5$.

# Cosine Similarity

## Diagram descriptions

- Left diagram: A diagonal line with arrowheads at both ends, indicating two vectors pointing in opposite directions along the same line. A green callout reads: **Angle ≈ 180°**.
- Right diagram: A plot of $\cos(\theta)$ versus $\theta$. The vertical axis is labeled $\cos(\theta)$ with tick labels `1`, `0.5`, `0`, `-1`; the horizontal axis is labeled $\theta$ with tick labels `60°`, `90`, `180`, `270`, `360`. A red dashed guide marks $\theta = 60°$ and $\cos(\theta) = 0.5$. The cosine curve begins at `1`, crosses `0` near `90`, reaches `-1` near `180`, crosses `0` near `270`, and returns to `1` near `360`.

# Cosine Distance

\[
Cosine\ Distance = 1 - Cosine\ Similarity
\]

**Diagram description:** Two examples illustrate cosine distance. On the left, two arrows point in the same direction, indicating cosine similarity \(= 1\), so distance \(= 0\). On the right, two arrows point in opposite directions, indicating cosine similarity \(= -1\), so distance \(= 2\).

\[
\begin{aligned}
dist &= 1 - sim \\
dist &= 1 - 1 \\
dist &= 0
\end{aligned}
\]

\[
\begin{aligned}
dist &= 1 - sim \\
dist &= 1 - (-1) \\
dist &= 2
\end{aligned}
\]

# Which One Should We Use?

**Figure/diagram:** A two-dimensional coordinate axis diagram labeled for “Mitochondria.” The vertical axis points upward and is labeled **y**. The horizontal axis points to the right and is labeled **x**, with **Voltage** written to the right of the x-axis arrow.

# Which One Should We Use?

## Diagram/Figure

A 2D plot with a vertical **y** axis labeled **Mitochondria** and a horizontal **x** axis labeled **Voltage**.

- A red point high on the **Mitochondria** axis is annotated:  
  “Very long book. Mitochondria appears 500 times.”
- A red point lower on the **Mitochondria** axis is annotated:  
  “Short book. Mitochondria appears a few times.”
- A green point along the **Voltage** axis is annotated:  
  “Short book. Voltage appears a few times.”

The diagram conveys that term counts depend on both the word and the length of the book: a very long book can contain “Mitochondria” many times, while short books may contain either “Mitochondria” or “Voltage” only a few times.

# Which One Should We Use?

## Diagram/Figure

The diagram shows a 2D coordinate plane with:

- Vertical axis labeled **y** and **Mitochondria**
- Horizontal axis labeled **x** and **Voltage**

There are three plotted points:

- A red point high on the **Mitochondria** axis:
  - “Very long book. Mitochondria appears 500 times.”
- A red point lower on the **Mitochondria** axis:
  - “Short book. Mitochondria appears a few times.”
- A green point along the **Voltage** axis:
  - “Short book. Voltage appears a few times.”

Pink line segments connect the lower red point to the upper red point and to the green point, illustrating distances between books in term-count space.

A highlighted callout explains the main issue:

> The 2 biology books are  
> further apart, simply  
> because one had more  
> words!

# TF-IDF

- Improve the count vectorizer
- TF-IDF is popular for document retrieval and text mining
- Why we need it and how it works

# What’s Wrong with the Count Vectorizer?

- Why don’t we want to keep stopwords?
- They’re unlikely to be helpful for NLP tasks
- If you’re building a search engine:
  - Probably every document contain these words
- If you’re doing spam detection or sentiment analysis:
  - Probably every document contain these words

# Stopwords

- How do we know our list of stopwords is correct?
- They may be <span style="color:#4285F4">application-specific</span>
- “Mitochondria” might be useful to differentiate biology and physics
- But what if <span style="color:#4285F4">all</span> documents are about biology
- Can we <span style="color:#4285F4">automatically</span> determine which words are important, and which to ignore?

# The Main Idea Behind TF-IDF

- Words that we want to ignore appear in many different documents
- They won’t help us differentiate <span style="color: #4285F4;">between</span> documents
- We want to somehow <span style="color: #4285F4;">scale down</span> these word counts

# TF-IDF: Intuitive Idea

- “Term Frequency - Inverse Document Frequency”

$$
TF - IDF \approx \frac{Term\ Frequency}{Document\ Frequency}
$$

# TF-IDF Formula

\[
tfidf(t, d) = tf(t, d) \times idf(t)
\]

> The term count depends on which  
> term t we are counting, and which  
> document d we are looking at

> The document count only  
> depends on the term t. It is found  
> by summing over all documents.

**Diagram/Figure description:** The formula shows TF-IDF as the product of term frequency \(tf(t, d)\) and inverse document frequency \(idf(t)\). A callout points to \(tf(t, d)\), explaining that term count depends on both the term \(t\) and the document \(d\). Another callout points to \(idf(t)\), explaining that document count depends only on the term \(t\) and is found by summing over all documents.

# TF-IDF

- Term Frequency
  - This is what we get with the CountVectorizer (after calling “transform”)

\[
tf(t,d) = \# \text{ of times } t \text{ appears in } d
\]

- Inverse Document Frequency
  - Let N(t) be the number of documents term t appears in and N be the  
    number of documents

\[
idf(t) = \log \frac{N}{N(t)}
\]

# Why Take the Log?

- The log is a monotonic function: if \(N/N(t)\) gets larger, so too will its log
- i.e. TF-IDF goes down as t appears in more documents
- The log function squashes its argument
- Suppose \(N(t) = 1\), and \(N = 10^6\), if we didn’t take the log, TF-IDF would increase by 1 million (relative to TF)
- With logging, this goes down to 13.8 (better for ML)
- Deeper reasons: information theory

\[
idf(t) = \log \frac{N}{N(t)}
\]

# How to Use TF-IDF in Python

```python
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
Xtrain = tfidf.fit_transform(train_texts)
Xtest = tfidf.transform(test_texts)

# note: arguments exist for stopwords, tokenizer, strip
accents, etc.
```

# Term Frequency Variations

- Binary (1 if word appears, 0 otherwise)
- Normalize the count

$$
tf(t,d) = \frac{count(t,d)}{\sum_{t' \in terms(d)} count(t',d)}
$$

- Take the log

$$
tf(t,d) = \log(1 + count(t,d))
$$

# Inverse Document Frequency Variations

- Smooth IDF

  $$
  idf(t) = \log \frac{N}{N(t)+1} + 1
  $$

- IDF Max

  $$
  idf(t) = \log \frac{\max_{t' \in terms(d)} N(t')}{N(t)}
  $$

- Probabilistic IDF

  $$
  idf(t) = \log \frac{N - N(t)}{N(t)}
  $$

# Normalizing TF-IDF

- Unlike CountVectorizer, TfidfVectorizer supports it
- TfidfVectorizer(norm=’l2’) (or ‘l1’; L2 is the default)

$$
\hat{tfidf}(t,d) = \frac{tfidf(t,d)}{\|tfidf(\cdot,d)\|_p}, \ where \ p = 1 \ or \ 2
$$

# Exercise - TF-IDF Recommendation system

- Data: movie info (keywords, genre, title, synopsis, tagline, production, …)
- Key step: how to combine movie data into a single string?
  - Recall: TfidfVectorizer expects one string per “Document”
- Transform the strings using TF-IDF
- Assume the query is always an existing movie in the database
- E.g. query = “Scream 3”, then recommend other movies based on this
- Get TF-IDF representation of Scream 3
- Compute similarity between Scream 3 and all other vectors
- Sort by similarity
- Print out the top 5 closest movies
- Try movies from other genres

# Neural Word Embeddings

- Previously, we saw how to convert whole documents into vectors
- Neural word embeddings convert <span style="color:#4285f4">single word</span> into vectors
- Thus, a document becomes a <span style="color:#4285f4">sequence</span> of vectors
- More information than “bag of words”

> Just think of “word embedding” the same as “word vector”

**Diagram/Figure:** A recurrent neural network processes a word sequence one word at a time: `"The"` → `"quick"` → `"brown"` → `"fox"`. Each word is input into an `RNN` block, which passes hidden state information forward from \(h_0\) through \(h_1\), \(h_2\), \(h_3\), and \(h_4\). Above each `RNN` block is a `Softmax` layer that outputs a probability distribution over the next word:
- \(P(W \mid \text{"The"})\)
- \(P(W \mid \text{"...quick"})\)
- \(P(W \mid \text{"...brown"})\)
- \(P(W \mid \text{"...fox"})\)

# Sequence of Vectors

- Specialized models are designed to handle sequences, including:
  - CNNs
  - RNNs
  - Transformers

- Cutting-edge applications include:
  - Language translation
  - Question answering
  - Chatbots
  - Speech-to-text and text-to-speech
  - Biological sequence analysis

**Figure/diagram:** A sequence-processing architecture is illustrated. Purple rectangular blocks along the bottom represent sequential inputs or hidden states connected over time by arrows, including a recurrent/self-loop connection on the first block and forward arrows through later blocks. Above the blocks are purple neural-network panels receiving inputs from the sequence positions, with arrows indicating information flowing upward and across time. Yellow connections between panels suggest attention or communication across sequence elements, showing that models can relate different positions in a sequence when producing outputs.

# Embedding Methods

- Word2Vec (Google) – Predicts word context using neural networks.
- GloVe (Stanford) – Uses word co-occurrence statistics for embeddings.
- BERT – Contextual embeddings with bidirectional transformer models.

# Word2Vec

- Word2Vec learns word representations based on surrounding words.
- Uses a <span style="color:red">simple neural network (embedding matrix)</span> with only one hidden layer.
- Two training methods:
  - Continuous Bag of Words (CBOW): Predicts a target word from surrounding words.
  - Skipgram: Predicts surrounding words given a target word.
- Once trained, only the <span style="color:red">embedding matrix</span> is used.

https://towardsdatascience.com/implementing-word2vec-in-pytorch-from-the-ground-up-c7fe5bf99889/

# Word2Vec Architecture (Skipgram)

## Diagram description

A Word2Vec Skipgram architecture is shown:

- A **Word** input points to a one-hot **Vocabulary** vector:
  - `0`
  - `1`
  - `0`
  - `0`
  - `.`
  - `.`
  - `.`
  - `0`
  - `0`
  - `0`

- The vocabulary vector connects to an embedding matrix labeled:

  \[
  V \times N
  \]

  **(Embedding Matrix)**

- The embedding matrix produces a **Hidden Layer** vector labeled:
  - `h1`
  - `h2`
  - `.`
  - `.`
  - `.`
  - `hn`

- The hidden layer connects to a context matrix labeled:

  \[
  N \times V
  \]

  **Context Matrix**

- The context matrix produces multiple **Prediction Vectors**, including:
  - First prediction vector:
    - `0.12`
    - `0.99`
    - `.`
    - `.`
    - `.`
    - `0.03`
    - **First context word**
  - Last prediction vector:
    - `0.95`
    - `0.11`
    - `.`
    - `.`
    - `.`
    - `0.03`
    - **Last context word**

The diagram conveys that a one-hot input word from the vocabulary is transformed by the embedding matrix into a hidden representation, which is then multiplied by the context matrix to predict surrounding context words.

# What is the Embedding Matrix?

- A $V \times N$ matrix storing word embeddings.
  - V = Vocabulary size
  - N = Embedding dimension
- Each row represents a <span style="color:red">word vector</span>.
- Words with <span style="color:red">similar meanings</span> have <span style="color:red">similar vectors</span>.

| Word | Learned Word Vector (Embedding Matrix) |
|---|---|
| king | [0.27, -0.63, 0.89, ...] |
| queen | [0.31, -0.60, 0.85, ...] |
| apple | [0.12, -0.78, 0.35, ...] |

# Pros & Cons of Word2Vec

Strengths:

- Captures semantic meaning and word relationships effectively.
- Generates dense, low-dimensional vectors (solves the curse of dimensionality).
- Highly efficient and scalable for training on massive datasets.
- Provides easily transferable pretrained embeddings for downstream NLP tasks.

Limitations:

- Cannot handle out-of-vocabulary (OOV) words.
- Ignores subword information and morphology (e.g., apple vs. apples, solved by FastText).
- Does not understand context variations and polysemy (e.g., the word "bank", solved by BERT).
- Limited by a fixed context window, missing long-distance semantic dependencies.

# GloVe

- A word embedding model developed by Stanford University.
- Uses <span style="color:red">co-occurrence statistics</span> to learn word relationships.
- Captures <span style="color:red">global word meaning</span> by analyzing entire corpora.
- Unlike Word2Vec, it does not use a neural network.

# Learning Word Embeddings with GloVe

- Step 1: Build a word <span style="color:red">co-occurrence matrix</span> from a large corpus.
- Step 2: Apply <span style="color:red">matrix factorization</span> to generate dense word vectors.

Example of Co-Occurrence:

- If "ice" appears 20 times with "cold" but only 1 time with "steam", GloVe assigns a higher similarity between "ice" and "cold".
- Context words like "winter" or "freeze" will also be closer to "ice" in vector space.
- Word relationships emerge from co-occurrence patterns.

# Matrix Factorization

Given

$$
\log(X) \approx W \cdot \tilde{W}^{T} + b_i + \tilde{b}_j
$$

| Component | Dimensions shown | Text in figure |
|---|---:|---|
| Target Matrix | V x V | $\log(X)$ |
| Center Word Vectors | d by V | $W$ |
| Context Word Vectors | V by d | $\tilde{W}^{T}$ |
| Learned Word & Context Bias Terms | V x V | $b_i + \tilde{b}_j$ |

**Diagram/figure description:** The diagram shows the log of Co-occurrence Matrix (X), labeled Target Matrix, being approximated by the product of Center Word Vectors $W$ and transposed Context Word Vectors $\tilde{W}^{T}$, plus Learned Word & Context Bias Terms $b_i + \tilde{b}_j$.

log of Co-occurrence Matrix (X)

Target Matrix

Center Word Vectors

Context Word Vectors

(transposed)

Learned Word & Context Bias Terms

# Pros & Cons of GloVe

Strengths:

- Similar to Word2Vec
- Captures <span style="color:red">both global and local</span> word relationships.

Limitations:

- Requires <span style="color:red">pre-computing a co-occurrence matrix</span> (memory-intensive).
- Cannot <span style="color:red">learn new words dynamically</span> after training.
- Does not understand <span style="color:red">context variations</span> (solved by BERT).

# What can We Do with Word Vectors?

- Can convert a document into a vector (but not sparse like counting/TFIDF)
- <span style="color:red">Embeddings are dense and low dimensional</span> (20, 50, 100, 300, … << V)

**Diagram:** A document is converted into a sequence of words, then each word is mapped to its word vector, and the vectors are averaged to produce a document vector.

Doc → `"I", "like", "cats", "and", "dogs", ...` → `vec(I)`, `vec(like)`, `vec(cats)`, `...` → `AVERAGE()`

# Word Analogies

- How do we evaluate our embedding model?
- We can do <span style="color:red">arithmetic</span> on vectors (+ and -)
- King : Man :: ??? : Woman
- Answer: Queen
- In math: $\text{King} - \text{Man} \approx \text{Queen} - \text{Woman}$
- In code: $x = \text{King} - \text{Man} + \text{Woman}$
  - Find the closest word vector to x
  - The result will be Queen

**Diagram/figure:** A 3D vector space shows labeled points Man, Woman, King, and Queen. An arrow from Man to Woman and a parallel arrow from King to Queen indicate the same directional relationship, illustrating that the vector offset from Man to Woman corresponds to the offset from King to Queen.

# Word Analogies

- France : Paris :: Italy : Rome
- Japan : Japanese :: China : Chinese
- Miami : Florida :: Dallas : Texas
- December : November :: July : June
- Man : Woman :: He : She

# Vector Models & Text Preprocessing Summary

- Connection between text (strings) and numbers, i.e., turning text into vectors
  - Counting
  - TF-IDF
  - Neural word embeddings (word2vec, GloVe)
- Text preprocessing:
  - Tokenization
  - Bag of words
  - Stopwords
  - Stemming and lemmatization

# NLP in Other Languages

- Everything in this course can be applied to any language
- Reminder: many NLP techniques are applied in bioinformatics / genomics
- Strings of DNA / RNA / etc.

![Diagram showing cartoon people with speech bubbles in different languages: English, Français, Italiani, Español, ελληνικά, Deutsch, 日本の, 中國的, русский. The figure conveys that NLP can be applied across many human languages.]()

# Steps of a Typical NLP Analysis

- Get the text (strings)
- Tokenize the text
- Stopwords, stemming / lemmatization
- Convert text into count vectors / TF-IDF
- Do ML task (recommend, detect spam, summarize, topic model)

# When Working with a New Language …

- Some questions to ask
  - What is a “word”?
  - What is a “sentence”? How does punctuation work?
  - Boundaries between sentences?
  - Boundaries between words?
  - Stopwords?
- Find a tokenizer built by others or build one yourself
- Learn the language!

# Multilingual Models

- Idea: try to make embedding consistent across languages

**Figure:** A 2D embedding space with axes, showing semantically equivalent phrases in different languages clustered near each other. Color legend: red = En, orange = Fr, blue = Zh. The phrases “cute puppy,” “chiot mignon,” and “可爱的小狗” appear close together in the upper-left region. The phrases “nice weather,” “beau temps,” and “好天气” appear close together in the lower-right region.

# Multilingual Models

- Challenge: Different languages have unique grammar, word order, and cultural nuances.
- Methods:
  - **Supervised Alignment:** Uses parallel corpora (e.g., translations) to align embeddings.
  - **Unsupervised Alignment:** Learns alignment without direct translations, relying on statistical patterns.
  - **Joint Training:** Trains embeddings on multiple languages at the same time.