# Probabilistic Models

# Introduction to N-Gram Models

- An **N-Gram model** predicts words based on the previous N words.
- Used in speech recognition, autocomplete, translation, and spell checking.
- <span style="color:red">Larger N = more context, but higher complexity.</span>
- Formula:
  - Unigram (n = 1): \(P(w_n)\) &nbsp;&nbsp;&nbsp; #只看單字在語料庫中的出現頻率
  - Bigram (n = 2): \(P(w_n|w_{n-1})\)
  - Trigram (n = 3): \(P(w_n|w_{n-1}, w_{n-2})\)

- Example: If past sentences include:
  - “I love NLP” (40%)
  - “I love AI” (30%)
  - “I love programming” (30%)
  - **Then \(P(\text{NLP}|\text{I love}) = 0.4\)**

# Where Are N-Gram Models Used?

- Speech Recognition → Predicts missing words.
- Autocomplete & Spell Checking → Suggests next words.
- Machine Translation → Improves word prediction accuracy.
- Text Generation → Creates realistic sentences.

# When Calculating the Probability of a Sequence…

**Sequence Definition :** $\{x_1, x_2, \ldots, x_T\}$

**Joint Probability (Goal) :** $p(x_1, x_2, \ldots, x_T)$

**The Chain Rule of Probability :**

$$
p(x_1, x_2, \ldots, x_T) = p(x_1) \cdot p(x_2 \mid x_1) \cdot p(x_3 \mid x_1, x_2) \cdot \ldots \cdot p(x_T \mid x_{T-1}, \ldots, x_1)
$$

or using product notation :

$$
p(x_1, x_2, \ldots, x_T) = p(x_1) \prod_{t=2}^{T} p(x_t \mid x_{t-1}, x_{t-2}, \ldots, x_1)
$$

**Key Computational Problem :**

$$
p(x_t \mid x_{t-1}, x_{t-2}, \ldots, x_1)
$$

# When Calculating the Probability of a Sequence…

**Sequence Definition :** $\{x_1, x_2, \ldots, x_T\}$

**Joint Probability (Goal) :** $p(x_1, x_2, \ldots, x_T)$

**The Chain Rule of Probability :**

$$
p(x_1, x_2, \ldots, x_T) = p(x_1) \cdot p(x_2 \mid x_1) \cdot p(x_3 \mid x_1, x_2) \cdot \ldots \cdot p(x_T \mid x_{T-1}, \ldots, x_1)
$$

or using product notation :

$$
p(x_1, x_2, \ldots, x_T) = p(x_1) \prod_{t=2}^{T} p(x_t \mid x_{t-1}, x_{t-2}, \ldots, x_1)
$$

**Key Computational Problem :**

$$
p(x_t \mid x_{t-1}, x_{t-2}, \ldots, x_1)
$$

Calculating this probability can be a  
nightmare when T becomes large  
due to data sparsity

**Diagram/Figure Description:** A gray arrow points from the red annotation “Calculating this probability can be a nightmare when T becomes large due to data sparsity” toward the key computational problem formula $p(x_t \mid x_{t-1}, x_{t-2}, \ldots, x_1)$, indicating that estimating this conditional probability becomes difficult for long histories because of data sparsity.

# The Markov Property

- The Markov property is a very restrictive assumption on the dependency structure of the <span style="color:red">joint probability</span>
- The probability of transitioning to the next state depends only on the current state, not past states

**Diagram:** A linear chain of states with arrows showing transitions only from one state to the next:  
\(X_{t-2} \rightarrow X_{t-1} \rightarrow X_t \rightarrow X_{t+1} \rightarrow X_{t+2}\).  
This conveys that each state depends directly only on the immediately preceding state.

- This implies that the joint probability takes the form:

\[
p(x_1, \ldots, x_T) = p(x_1)\prod_{t=2}^{T} p(x_t \mid x_{t-1})
\]

# The Markov Property

$$
p(x_t \mid x_{t-1}, x_{t-2}, \cdots) = p(x_t \mid x_{t-1})
$$

**Figure/annotation:** A green callout labeled “What the Markov property says” points to the equation, indicating that the probability of \(x_t\) conditioned on the entire past is equal to the probability of \(x_t\) conditioned only on \(x_{t-1}\).

$$
x_t \text{ is independent of } x_{t-2}, x_{t-3}, \cdots
$$

**Figure/annotation:** A green callout labeled “What the Markov property also says” points to the independence statement, indicating that \(x_t\) is independent of earlier states beyond \(x_{t-1}\).

# Why is the Markov Property Useful?

- Consider a Markov model of the English language
- Suppose we choose 2000 of the most common words
- Suppose we want to get the probability distribution for the 10th word in a sentence given the previous nine words
- Our model is \(p(x_{10} \mid x_9, x_8, \ldots, x_1)\)
- Each “x” has 2000 possible values (words)
- How many probabilities to estimate? \(2000 \times 2000 \times 2000 \ldots = 2000^{10}\)
- Q: Do we have a sufficient amount of data?

# The Markov “Assumption”

- We assume the Markov property holds, even when it does not

  **Figure:** Two boxed example sentences are shown:

  > "I like green eggs and ham."

  > "I like to code in C++ and Python."

  Light gray curved arrows connect earlier words in each sentence toward the final word, illustrating dependencies across multiple previous words. The figure conveys that although a Markov model may assume the next word depends only on the immediately preceding word, the words “ham” and “Python” are influenced by broader sentence context, not just by “and”.

- Do “ham” and “Python” only depend on “and”? No!
- “All models are wrong, but some are useful” - George Box

# The Markov Model

- In this section, we’ll consider sequences of **categorical symbols**, which we’ll refer to as “states”
- Example, weather: {sunny, rainy, cloudy}
- Example, POS tags: {noun, verb, adjective}

**Figure:** A Markov model over three weather states: Sunny, Cloudy, and Rainy. Directed arrows indicate transition probabilities between states:
- Sunny → Sunny: 0.8
- Sunny → Cloudy: 0.15
- Sunny → Rainy: 0.05
- Cloudy → Cloudy: 0.5
- Cloudy → Sunny: 0.2
- Cloudy → Rainy: 0.3
- Rainy → Rainy: 0.6
- Rainy → Sunny: 0.2
- Rainy → Cloudy: 0.2

# Notation

- We’ll use **s** for “state”

$$
s(t) = s_t = state\ at\ time\ t
$$

- Time will also be discrete (t = 1, 2, ...) (e.g., no such thing as t = 1.5)
- We’ll number the states from 1, 2, ..., M
- M = total number of possible states (e.g., M = 3 for sunny/rainy/cloudy)
- We use i or j to index the state space

$$
p(s_t = i)\ means:\ probability\ that\ state\ at\ time\ t\ is\ 'i'
$$

# State Distribution

- We have \(p(s_t = 1), p(s_t = 2), \ldots, p(s_t = M)\)
- This is M probability values - together they form a **distribution**
- Ex: “What is the probability that it will be rainy on Sunday?”

Ans: \(p(s_{\text{sunday}} = \text{rainy})\)

\[
p(s_t) = \textit{state distribution (length M vector)}
\]

# State Transitions

\[
p(s_t = j \mid s_{t-1} = i)
\]

- “Probability that state at time t is j, given that the state at time t-1 was i”
- How many of these probability values exist? (for all i and j)
- Since both i and j can take any value from 1…M, there are \(M^2\) values

# State Transition Matrix

\[
A_{ij} = p(s_t = j \mid s_{t-1} = i), \ \forall i = 1...M ,j = 1...M
\]

- A is an MxM matrix
- Convention: first index (row) = previous state, second index (column) = next state

# State Transition Matrix

But where is t?

\[
A_{ij} = p(s_t = j \mid s_{t-1} = i), \ \forall i = 1 \ldots M, j = 1 \ldots M
\]

- In general, we could have \(A_{ij}(t)\)
- When A doesn’t depend on t: **time-homogeneous Markov process**
- Note: Natural language is NOT strictly time-homogeneous, but here we drop t to prevent parameter explosion and solve the data sparsity issue

# Initial State

**Diagram:** A sentence box contains “The quick brown fox jumps over the lazy dog.” A red rectangle highlights the first word, “The.” A speech bubble pointing to the highlighted first word asks, “What's the probability of the first word?”

- To quantify the probability of the first state in a sequence, we use the **initial state distribution**

\[
\pi_i = p(s_1 = i) \quad (for\ i = 1...M)
\]

# Recap

\[
A_{ij} = p(s_t = j \mid s_{t-1} = i)
\]

\[
\pi_i = p(s_1 = i)
\]

- Given A and \(\pi\), and a sequence {s1, s2, …, st}, what is a probability of seeing that sequence?
- How do we find A and \(\pi\) given a dataset?

# Probability of a Sequence

\[
p(s_{1\ldots T}) = p(s_1)p(s_2|s_1)p(s_3|s_1,s_2)\cdots
\]

\[
p(s_{1\ldots T}) = p(s_1)\prod_{t=2}^{T} p(s_t|s_{t-1})
\]

Markov Property

\[
p(s_{1\ldots T}) = \pi_{s_1}\prod_{t=2}^{T} A_{s_{t-1},s_t}
\]

Start thinking about how you'd implement this in Python code

**Diagram/figure description:** A green callout labeled “Markov Property” points to the second equation, indicating that the probability of each state depends only on the immediately previous state. A larger green callout at the bottom right says “Start thinking about how you'd implement this in Python code,” prompting consideration of implementing the sequence probability using the initial distribution \(\pi\) and transition matrix \(A\).

# Training a Markov Model

- Suppose we flip a coin a bunch of times - how do we estimate p(heads)?

$$
p(heads) \approx \frac{count(H)}{total\ tosses}
$$

- That’s just the binary case. What if we have M>2?

$$
p("cat") \approx \frac{count("cat")}{total\ word\ count}
$$

# Estimating A and \(\pi\) (Training)

> Note: the ‘hat’  
> means ‘estimate’

\[
\hat{\pi}_i = \frac{count(s_1 = i)}{N}
\]

> N = number of  
> sequences in dataset

\[
\hat{A}_{ij} = \frac{count(i \to j)}{count(i)}
\]

> Example:  
> count(“the cat”) / count(“the”)

# Probability of a Sequence

$$
p(s_{1...T}) = \pi_{s_1} \prod_{t=2}^{T} A_{s_{t-1}, s_t}
$$

- Only involves multiplication
- What if one of the value is 0? Transition never appears in training set
- The result becomes 0!

# Add-One Smoothing

- Give a small probability to every possible transition
- Add a “fake count” of 1 for each (i, j) transition

\[
\hat{A}_{ij} = \frac{count(i \to j) + 1}{count(i) + M}
\]

> Adding M to the denominator ensures  
> that each row of A sums to 1

# Add-One Smoothing

- We can do this for the initial state distribution too

$$
\hat{\pi}_i = \frac{count(s_1 = i) + 1}{N + M}
$$

# Add-Epsilon Smoothing

- We can make it more smooth \((\varepsilon > 1)\) or less smooth \((\varepsilon < 1)\)

\[
\hat{A}_{ij} = \frac{count(i \to j) + \varepsilon}{count(i) + \varepsilon M}
\]

\[
\hat{\pi}_{i} = \frac{count(s_1 = i) + \varepsilon}{N + \varepsilon M}
\]

# Computing the Probability of a Sequence

\[
p(s_{1...T}) = \pi_{s_1}\prod_{t=2}^{T} A_{s_{t-1},s_t}
\]

- This involves <span style="color: blue;">multiplying</span> many small numbers together
- Common to use 20k - 50k vocabulary size in English
- As you multiply small numbers together, they approach 0!
- Computers don’t have infinite precision; eventually it just rounds to 0
- Problematic: what if we want to compare 2 sequences?

# Working with Log Probabilities

- Solution: compute log probabilities instead
- We don’t need the actual probability value, since what we usually want to do is compare (e.g., is one sequence more likely than another?)

**Figure:** A graph comparing logarithmic functions. The x-axis is labeled \(x\) and the y-axis is labeled \(y\). A dashed vertical line marks \(x = 0\). Three curves are shown: \(\log_2(x)\) is the highest curve, \(\ln(x)\) is in the middle, and \(\log(x)\) is the lowest curve. All three curves increase as \(x\) increases, approach negative infinity as \(x\) approaches 0 from the right, and pass through approximately \((1, 0)\).

# Working with Log Probabilities

$$
\log p(s_{1...T}) = \log \pi_{s_1} + \sum_{t=2}^{T} \log A_{s_{t-1}, s_t}
$$

- Since log(AB) = log(A) + log(B)
- Note: do not compute the product and then take the log (to avoid log(0))

# Build a Text Classifier Using Markov Models

## Diagram

- `Poem` → `Classifier` → `Is the poem by Edgar Allan Poe or Robert Frost?`
- `Email` → `Classifier` → `Spam or not spam`

The diagram shows two examples of text classification: a poem is input into a classifier to determine whether it was written by Edgar Allan Poe or Robert Frost, and an email is input into a classifier to determine whether it is spam or not spam.

# Supervised or Unsupervised?

- Text classification is an example of supervised learning, but Markov models are unsupervised (training data is just text; no labels)
- Answer: We must apply Bayes’ rule (and build a **Bayes classifier**)

$$
p(y \mid x) = \frac{p(x \mid y)p(y)}{p(x)}
$$

# Bayes Classifier

## Diagram

- Poems by Robert Frost → Markov Model $(A_0, \pi_0)$
- Poems by Edgar Allan Poe → Markov Model $(A_1, \pi_1)$

The diagram shows two separate poetry corpora used to train two separate Markov Models: poems by Robert Frost are associated with Markov Model $(A_0, \pi_0)$, and poems by Edgar Allan Poe are associated with Markov Model $(A_1, \pi_1)$.

# Bayes Classifier

## Diagram

- Poems by Robert Frost → Markov Model \((A_0, \pi_0)\)
- Poems by Edgar Allan Poe → Markov Model \((A_1, \pi_1)\)

A vertical dotted line separates training the Markov models from classifying a new text.

- New unknown text → Markov Model \((A_0, \pi_0)\) → \(p(x \mid \text{author} = \text{Frost})\)
- New unknown text → Markov Model \((A_1, \pi_1)\) → \(p(x \mid \text{author} = \text{Poe})\)

# Maximum A Posteriori (MAP)

- We have p(poem | author), but we want p (author | poem) (a probability distribution)
- Then we can apply the following decision rule:

$$
k^* = \arg\max_k p(class = k \mid x)
$$

**Callout:**  
If it's not obvious,  
"poem" = x, and  
"author" = class

**Figure meaning:** The callout maps the example terms to the variables in the decision rule: "poem" corresponds to \(x\), and "author" corresponds to class.

# Apply Bayse Rule (In this example)

\[
p(author \mid poem) = \frac{p(poem \mid author)\,p(author)}{p(poem)}
\]

# How to Find the Probability Distribution

Posterior

Liklihood

Prior

$$
p(author \mid poem)=\frac{p(poem \mid author)\,p(author)}{p(poem)}
$$

The figure shows Bayes’ rule for calculating the posterior probability \(p(author \mid poem)\). The label “Posterior” corresponds to the left-hand side \(p(author \mid poem)\), “Liklihood” corresponds to \(p(poem \mid author)\), and “Prior” corresponds to \(p(author)\).

# Simplifying the Decision Rule

$$
k^* = \arg \max_k \frac{p(poem \mid author = k)\ p(author = k)}{p(poem)}
$$

$$
k^* = \arg \max_k p(poem \mid author = k)\ p(author = k)
$$

$$
k^* = \arg \max_k \log p(poem \mid author = k) + \log p(author = k)
$$

# Simplifying the Decision Rule

\[
k^* = \arg\max_k \frac{p(poem \mid author = k)\ p(author = k)}{p(poem)}
\]

\[
k^* = \arg\max_k p(poem \mid author = k)\ p(author = k)
\]

\[
k^* = \arg\max_k \log p(poem \mid author = k) + \log p(author = k)
\]

**Figure/callout:** A callout box to the right of the first equation states: “p(poem) can be ignored”. It indicates that \(p(poem)\), the denominator in the first expression, is independent of \(k\) and is omitted in the simplified decision rule.

# Simplifying the Decision Rule

\[
k^* = \arg\max_{k} \frac{p(poem \mid author = k)\,p(author = k)}{p(poem)}
\]

\[
k^* = \arg\max_{k} p(poem \mid author = k)\,p(author = k)
\]

\[
k^* = \arg\max_{k} \log p(poem \mid author = k) + \log p(author = k)
\]

**Apply log function**

**Diagram/Figure description:** A rounded rectangle labeled “Apply log function” appears to the right of the equations, indicating the transformation from the product of probabilities in the second decision rule to the sum of log probabilities in the third decision rule.

# Simplifying the Decision Rule

\[
k^* = \operatorname*{arg\,max}_{k} \frac{p(poem \mid author = k)\,p(author = k)}{p(poem)}
\]

\[
k^* = \operatorname*{arg\,max}_{k} p(poem \mid author = k)\,p(author = k)
\]

\[
k^* = \operatorname*{arg\,max}_{k} \log p(poem \mid author = k) + \log p(author = k)
\]

**Diagram/Figure:** A rounded rectangle labeled “Can be computed by Markov model” sits below the third equation. An upward arrow points from the rectangle to the \(\log p(poem \mid author = k)\) term, indicating that this term can be computed by a Markov model.

# Maximum Likelihood

- We can simply take the argmax of the likelihood if the <span style="color:red">prior is uniform</span> (i.e. we have no reason to believe, given no other info, that one author is more likely than another)

\[
k^* = \operatorname*{arg\,max}_{k} \log p(\mathit{poem}\mid \mathit{author}=k)
\]

**Diagram/Figure:** A rounded gray callout beneath the formula reads: “If p(author) is uniform”. It indicates that the maximum likelihood rule above applies when the prior probability over authors is uniform.

# Recap

- We train a separate Markov model for each class
- Each model gives us \(p(x \mid \text{class} = k)\) for all k
- General form of decision (MAP): \(k^* = \arg\max_k p(\text{class} = k \mid x)\)
- Posterior can be simplified since we don’t need its actual value
- Simplified MAP: \(k^* = \arg\max_k \log p(x \mid \text{class} = k) + \log p(\text{class} = k)\)
- Maximum likelihood: \(k^* = \arg\max_k \log p(x \mid \text{class} = k)\)

# Text Classifier Exercise Prompt

- You’ll be given poems by 2 authors: Edgar Allan Poe and Robert Frost
- Build a classifier that can distinguish between the 2 authors
- Compute train and test accuracy
- Check for class imbalance, compute F1-score if imbalanced

# Using Markov Models to Generate Text

- Classifying text: supervised learning (we have labels)
- Generating text: unsupervised learning (no labels)

**Diagram description:** A sequence of words, **THE → CAT → SAT → ON → THE**, is fed into a **MARKOV MODEL**. The model predicts possible next words with probabilities: **MAT (60%)**, **ROOF (30%)**, and **FLOOR (10%)**. The selected output is shown as **PREDICTED WORD: MAT**.

# Problem with Markov Assumption

- Recall: the next word only on a single preceding word

## Figure

The diagram shows examples where relying only on a single preceding word can combine incompatible sentence contexts, producing incoherent sentences.

- Green example sentences:
  - I made **myself** a peanut butter sandwich.
  - I'll go and see her **myself**.
- Pink resulting sentence:
  - I'll go and see her **myself** a peanut butter sandwich.

- Green example sentences:
  - I made myself a **peanut** butter sandwich.
  - The **peanut** is not a nut.
- Pink resulting sentence:
  - I made myself a **peanut** is not a nut.

# Extending the Markov Model

- Instead of depending only on one past state, depend on two

$First\ Order\ Markov:\ \ p(s_t \mid s_{t-1}, s_{t-2}, \cdots) = p(s_t \mid s_{t-1})$

$Second\ Order\ Markov:\ \ p(s_t \mid s_{t-1}, s_{t-2}, \cdots) = p(s_t \mid s_{t-1}, s_{t-2})$

# 2nd-Order Markov Model Implementation

\[
A_{ijk} = p(s_t = k \mid s_{t-1} = j, s_{t-2} = i)
\]

- This is a 3-D array
- Its shape is MxMxM = M³
- 3rd-order: M⁴, 4th-order: M⁵, etc. This grows exponentially!

**Diagram/Figure:** The figure shows arrays increasing in dimensionality: a 1-D row along the X axis, a 2-D grid along X and Y, and a 3-D cube along X, Y, and Z. It conveys that higher-order Markov models require higher-dimensional arrays, with storage growing rapidly as dimensions are added.

# The Full Model

$$
\pi_i = p(s_1 = i)
$$

$$
A^{(1)}_{ij} = p(s_2 = j \mid s_1 = i)
$$

$$
A^{(2)}_{ijk} = p(s_t = k \mid s_{t-1} = j,\ s_{t-2} = i)
$$

Diagram description: The sentence `"The quick brown fox jumps over the lazy dog."` is shown inside a large black rectangle. Overlapping colored boxes illustrate the model components: a red box highlights the initial state/window corresponding to $\pi_i$, an orange box highlights a first-order transition/window corresponding to $A^{(1)}_{ij}$, and multiple cyan boxes highlight overlapping second-order transition/windows corresponding to $A^{(2)}_{ijk}$ across consecutive words.

# Storing Word Probabilities in Dictionaries

- We will not use add-one smoothing, so many words will have zero probability (and they will simply not appear in the dictionary)
- Thus, although there will be V words in the vocabulary, the dictionary will not store V items

```text
pi = {
    "the": 0.2,
    "a": 0.3,
    "is": 0.1,
    ...
}
```

**Figure:** A dictionary named `pi` maps words to their probabilities. Only words with nonzero probabilities are stored as key-value pairs, such as `"the": 0.2`, `"a": 0.3`, and `"is": 0.1`; omitted words are implied to have zero probability.

# Why Use Dictionaries?

- Sparsity!
- We use add-one smoothing since many possible transition don’t appear in the training corpus
- This gets worse as the model order gets larger
- i.e. Transition array will be <span style="color:red">mostly zeros</span> (out of $V \times V \times V$ total elements)
  - It’s more efficient to store only the transition which were seen!

# First Order Transitions

- Recall: used only to model the 2nd word in each line

```text
A1 = {
    "the": {
            "cat": 0.05,
            "dog": 0.03,
            "mouse": 0.01,
            ...
        },
    "a": { ... },
    ...
}
```

Figure description: The figure shows `A1` as a first order transition mapping from an initial word such as `"the"` or `"a"` to possible second words and their probabilities. For `"the"`, example next-word probabilities include `"cat": 0.05`, `"dog": 0.03`, and `"mouse": 0.01`.

# First Order Transitions

- Recall: used only to model the 2nd word in each line

```text
A1 = {
    "the": {
            "cat": 0.05,
            "dog": 0.03,
            "mouse": 0.01,
            ...
        },
    "a": { ... },
    ...
}
```

[Diagram/Figure: A boxed code-like dictionary labeled `A1` stores first-order transition probabilities. The key `"the"` maps to a nested dictionary of possible next words and probabilities, including `"cat": 0.05`, `"dog": 0.03`, and `"mouse": 0.01`. A red arrow points from the `"cat": 0.05` entry to a callout showing \(p(\text{cat} \mid \text{the}) = 0.05\), indicating that the probability of `"cat"` following `"the"` is 0.05. Another callout asks: “Exercise: how would you store second-order transitions?”]

# Sampling from a Probability Dictionary

- How do we sample words from a dictionary with probabilities stored as dictionary values (with words as keys)?

```python
probs = {
    "the": 0.2,
    "a": 0.3,
    "is": 0.1,
    ...
}
```

The figure shows a probability dictionary named `probs`, where each word is a key and its associated probability is the value.

# Example

> Start by drawing a number \(x \sim U(0, 1)\)

## Diagram

A horizontal number line from 0 to 1 is divided into three adjacent ranges:

| Range of \(x\) | Outcome |
|---|---|
| \(0 < x < 0.2\) | “a” |
| \(0.2 < x < 0.7\) | “b” |
| \(0.7 < x < 1\) | “c” |

The first segment from 0 to 0.2 is labeled **a**, the second segment from 0.2 to 0.7 is labeled **b**, and the third segment from 0.7 to 1 is labeled **c**. Arrows point from the rule boxes to their corresponding intervals.

> If \(0 < x < 0.2\), then “a”

> If \(0.2 < x < 0.7\), then “b”

> If \(0.7 < x < 1\), then “c”

- The <span style="color:red">area</span> covered by each of these ranges is exactly  
  the assigned probabilities (0.2, 0.5, 0.3)

- Notice: we must calculate the <span style="color:red">cumulative sum</span>  
  0 + 0.2: first boundary  
  0.2 + 0.5 = 0.7: second boundary  
  0.7 + 0.3 = 1: third boundary

```text
probs = {
    "a": 0.2,
    "b": 0.5,
    "c": 0.3
}
```

# Pros & Cons of Markov Models

✅ Advantages:

- Simple & Efficient → Easy to implement and compute.
- Interpretable → Probabilities are clear and easy to analyze.
- Good for structured sequences → POS tagging, DNA sequence analysis.

❌ Limitations:

- Lacks long-term memory → Only considers the current state.
- Fails with ambiguous words → Struggles when context matters.
- Neural models (like Transformers) perform better → Capture long-range dependencies.