# 加選規則

- 加選優先序：
  - 資工系博士
  - 資工系碩二
  - 資工系碩一
  - 資工系大四
  - 外系研究生
  - 外系大四生
- 有希望加選的同學請於 2/26 (四) 12:00 前寄信至 :rogerwu212@gmail.com
- 助教會再回覆同學是否可以加選

# Natural Language Processing

# Teacher, I have questions

Lecturer:

- Office: science building (理學大樓) 812 room
- Email: albert.yang@nchu.edu.tw

TA:

- 實驗室: science building (理學大樓) 902 room
- Email: rogerwu212@gmail.com

**Making an appointment through email in advance is highly recommended!!**

# Grading policy

- 期中考 (20%)
- 期末考 (20%)
- 課堂練習 (20%)
- 期末專題 (30%)
- 出席 (10%)

# Couple of Notes

- Late assignment submissions
  - Submission time will be the basis for grading
  - The maximum score for late submissions is 80 points
  - Do not withdraw the submission at will
- Makeup exam
  - Leave must be completed at least three hours before the class, based on the records in the leave system
  - Must provide valid documents
  - Midterm exam: grades will be combined with the final exam.

# What is Natural Language Processing (NLP)

## Diagram

A large rounded rectangle labeled **Machine Learning** contains three subareas:

- **Natural Language Processing**  
  **(Text and Speech)**

- **Computer Vision**  
  **(Image, Video, …)**

- **Other**  
  **Tabular Data**  
  **Time Series**  
  **RL**  
  **Game Theory**

The diagram conveys that Natural Language Processing is a subfield within Machine Learning, alongside Computer Vision and other machine learning application areas such as tabular data, time series, reinforcement learning, and game theory.

# What is Natural Language Processing (NLP)

**Prompt:** What is NLP?

**ChatGPT:** NLP stands for **Natural Language Processing**. It is a branch of artificial intelligence (AI) that focuses on enabling computers to understand, interpret, and generate human language. NLP combines **linguistics**, **machine learning**, and **computer science** to process and analyze large amounts of natural language data.

# How is NLP Used?

- Spam Detection

**Figure:** An email interface showing the folder **“Spam (372)”** selected with a cursor pointing at it, illustrating email spam detection.

**Figure:** A smartphone text message from **+1 (215) 490-9762** containing a suspicious promotional message: **“Win a free iPad from Apple! Go to the following link to enter. iPad.apples.com/ youreanidiot”**, illustrating SMS spam detection.

# How is NLP Used?

- Spam Detection
- Predictive Text

## Figures

- Top-right figure: A smartphone keyboard interface showing predictive text. The message field contains: “I just wanted to”. The suggestion bar shows: “let”, “say”, “check”. The keyboard is labeled “SwiftKey”, with “143/1” shown near the send icon.
- Bottom-right figure: An email compose window demonstrating predictive writing/autocomplete. Visible text includes:
  - “Jacqueline Bruzek ×”
  - “Taco Tuesday”
  - “Hey Jacqueline,”
  - “Haven't seen you in a while and I hope you’re doing well.”

# How is NLP Used?

- Spam Detection
- Predictive Text
- Speech Recognition

**Figure:** A collage of speech-assistant devices and smartphone voice assistants illustrating speech recognition as an NLP application. It shows smart speakers and phones responding to spoken commands, including visible phone text: “Okay, I created a reminder for you. Move to Reminder” and “Go ahead, I’m listening...”.

# How is NLP Used?

- Spam Detection
- Predictive Text
- Speech Recognition
- Sentiment Analysis

**Figure:** A financial market chart with stock/price data in the background shows a green upward-trending arrow and a red downward-trending line, conveying contrasting positive and negative trends over time.

## SENTIMENT ANALYSIS

**Figure:** The sentiment analysis diagram categorizes hotel review text into three sentiment classes: POSITIVE, NEUTRAL, and NEGATIVE. Each class is represented by a facial expression icon and an example review.

### POSITIVE

"Great service for an affordable  
price.  
We will definitely be booking again."

### NEUTRAL

"Just booked two nights  
at this hotel."

### NEGATIVE

"Horrible services. The room  
was dirty and unpleasant.  
Not worth the money."

# Modern Advancement

- Language Translation

![A smartphone camera view translating a stop sign from English to Tamil. The physical sign in the background reads “STOP”; on the phone screen, the interface shows “English → Tamil” and overlays the stop sign with Tamil text “நிறுத்த”. The figure conveys real-time visual language translation using a mobile device, mapping English text in the environment to Tamil on-screen.]()

# Modern Advancement

- Language Translation
- Text Generation

**Figure:** GitHub Copilot promotional image conveying AI-assisted pair programming/code generation.

Text shown in figure:

- GitHub Copilot
- Technical preview
- Your AI pair programmer
- fetch_pic.js
- push_to_git.py
- Copilot

**Figure:** ChatGPT conversation screenshot conveying text generation through a user question and an AI-generated response.

**A** What is ChatGPT?

ChatGPT is an AI-powered chatbot developed by OpenAI. It is based on the GPT (Generative Pre-trained Transformer) architecture, specifically GPT-3.5. ChatGPT is designed to engage in text-based conversations with users, providing responses that are coherent, contextually relevant, and generated in a human-like manner.

The underlying technology behind ChatGPT is deep learning, specifically employing a transformer model. This architecture allows the model to process and understand the structure, context, and meaning of text input, enabling it to generate appropriate and informative responses.

# How NLP Works?

## NLP Process Flowchart

**Diagram description:** The flowchart shows **NLP** branching into two main areas: **NLU** and **NLG**. **NLU** further branches into **Sentiment Analysis** and **Entity Recognition**. **NLG** further branches into **AI Writing Tools** and **Text Summarization**.

```text
NLP
├── NLU
│   ├── Sentiment Analysis
│   └── Entity Recognition
└── NLG
    ├── AI Writing Tools
    └── Text Summarization
```

# NLP Methods

- Vector-Based Models and Text Processing
- Probability Models
- Machine Learning Models
- Deep Learning Models
- Large Language Models

# Vector-Based Models and Text Processing

- TF-IDF, Word Embedding Models
- Applications: similarity search, document retrieval, summarization

## Diagram/Figure Descriptions

### Left figure

A 2D vector-space diagram with arrows showing word-embedding relationships and analogies. The diagram includes the following words and linked relationships:

- `dog`, `dogs`
- `cat`, `cats`
- `Paris`, `France`
- `London`, `England`
- `Rome`, `Italy`
- `king`, `queen`
- `man`, `woman`
- `father`, `mother`
- `son`, `daughter`
- `boy`, `girl`
- `he`, `himself`
- `she`, `herself`
- `slow`, `slower`, `slowest`
- `fast`, `faster`, `fastest`
- `long`, `longer`, `longest`

The arrows convey consistent vector offsets for semantic and grammatical relationships such as singular/plural, capital/country, gender, family roles, pronoun/reflexive forms, and adjective comparative/superlative forms.

### Right figure

A node-link graph of entities connected by labeled relationships. The central node is `Bob_Dylan`, connected to related entities and concepts. Blue nodes represent entities; gray lines represent labeled relationships.

Connections shown include:

| Connected nodes | Relationship label |
|---|---|
| `The_Freewheelin'_Bob_Dylan` — `Randy_Newman_(album)` | `comprise` |
| `Antônio_Carlos_Jobim` — `Randy_Newman_(album)` | `comprise` |
| `Folk_music` — `Randy_Newman_(album)` | `genre` |
| `Randy_Newman_(album)` — `Bob_Dylan` | `comprise` |
| `Kars_Province` — `Bob_Dylan` | `write` |
| `Country_music` — `Bob_Dylan` | `explore` |
| `Duluth,_Minnesota` — `Bob_Dylan` | `until` |
| `Bob_Dylan` — `John_Wesley_Harding_(album)` | `explore` |
| `Bob_Dylan` — `Anterior_chamber_of_eyeball` | `adopt` |
| `Bob_Dylan` — `Controversy` | `draw + record` |
| `Bob_Dylan` — `Empire_State_Building` | `adopt` |
| `Controversy` — `Anterior_chamber_of_eyeball` | `adopt` |
| `Controversy` — `Analog_synthesizer` | `record` |
| `Empire_State_Building` — `Controversy` | `adopt` |
| `Empire_State_Building` — `Analog_synthesizer` | `record` |

# Probability Models

- Markov Models, N-gram Models, Hidden Markov Models (HMM), Naïve Bayes
- Applications: Spell correction, auto-completion, speech recognition
- Prerequisites for Transformers (BERT and GPT-3)

**Figure/diagram:** The phrase “the students opened their ______” branches via arrows to possible next words: “books” with probability 0.2, “laptops” with probability 0.1, “exams” with probability 0.1, and “minds” with probability 0.6.

# Machine Learning Models

- Training is essential for ML models

|  |  |
|---|---|
| **Spam Detection**<br>Uses: email filtering, SMS spam detection,<br>phishing detection<br>Method: Naive Bayes, SVM, Random Forest | **Sentiment Analysis**<br>Uses: reputation management, stock market,<br>customer feedback<br>Method: Logistic Regression, SVM, BERT,<br>Random Forest |
| **Latent Semantic Indexing**<br>Uses: information retrieval, document<br>clustering, search engines<br>Method: PCA / SVD | **Topic Modeling**<br>Uses: legal document classification, news<br>categorization, recommendation systems<br>Method: Latent Dirichlet Allocation |

# Deep Learning Models

- RNN, LSTM / GRU, Transformer (BERT, GPT-3)
- Can do any tasks we previously discussed

# Can ChatGPT Solve Every NLP Task?

- Specialized tasks require domain-specific models
  - ChatGPT lacks expertise in medical, legal, and financial fields.
  - BioBERT, FinBERT outperform general AI in these areas.

- Privacy & security risks
  - Public cloud-based AI models pose data privacy concerns.
  - Local NLP models (e.g., Llama, Mistral) ensure data control.

- Resource & cost constraints
  - Running ChatGPT is expensive & resource-intensive.
  - Task-specific NLP models are faster, cheaper, and more efficient.

# Syllabus (May Change in the Future)

## Classic NLP Methods:

- Vector Models and Text  
  Processing
- Probabilistic Models
- Machine Learning Models
- Deep Learning Models
- Large Language Models

## NLP Tasks

- Sentiment analysis
- Summarization
- Text Q&A
- Text-to-SQL
- …

## Advanced Topics:

- RAG
- AI Agent

# Schedule

2026/4/1: no class

2026/4/8: holiday

2026/4/22: midterm exam

2026/6/3: final exam