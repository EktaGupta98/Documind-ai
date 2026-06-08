# 📚 DocuMind AI

An Intelligent Multi-Document Retrieval-Augmented Generation (RAG) Assistant that allows users to upload documents, perform hybrid search, and chat with their data using Large Language Models.

---
### Live demo
https://av4lkchad4usgangejfuaw.streamlit.app/

## 🚀 Features

### 📂 Runtime Document Upload
- Upload documents directly from the Streamlit interface.
- No need to manually place files inside project folders.

### 📄 Multi-Format Support
Supports:

- PDF
- DOCX
- TXT
- CSV
- XLSX
- JSON

### ✂️ Intelligent Document Chunking
- Recursive Character Text Splitter
- Chunk Size: 1000
- Chunk Overlap: 200

### 🔎 Hybrid Search
Combines:

- Semantic Search (FAISS)
- Keyword Search (BM25)

This improves retrieval quality by capturing both semantic meaning and exact keyword matches.

### 🧠 Embedding Generation
Uses:

- sentence-transformers/all-MiniLM-L6-v2

for efficient and lightweight document embeddings.

### ⚡ Fast Vector Retrieval
- FAISS Vector Database
- Local vector storage
- Low-latency semantic retrieval

### 🤖 LLM Powered Answers
Uses:

- Groq API
- Llama 3.1 8B Instant

for fast and context-aware response generation.

### 📌 Source Citations
Every answer includes:

- Source Document Name
- Page Number (if available)

This improves transparency and reduces hallucinations.

### 📊 Retrieval Quality Score
Displays:

- High
- Medium
- Low

based on retrieval similarity scores.

### 💬 Conversational Interface
- Chat-style UI
- Maintains conversation history
- Built using Streamlit

---

# 🏗️ System Architecture

```text
User Uploads Documents
          │
          ▼
Document Loader
(PDF/DOCX/TXT/CSV/XLSX/JSON)
          │
          ▼
Document Chunking
          │
          ▼
MiniLM Embeddings
          │
          ▼
FAISS Vector Store
          │
          ▼
Hybrid Retrieval
(FAISS + BM25)
          │
          ▼
Context Construction
          │
          ▼
Groq LLM
(Llama 3.1 8B)
          │
          ▼
Answer + Sources + Retrieval Quality
```

---

# 🛠️ Tech Stack

## Frontend

- Streamlit

## Backend

- Python

## LLM

- Groq
- Llama 3.1 8B Instant

## Vector Database

- FAISS

## Embeddings

- Sentence Transformers
- MiniLM-L6-v2

## Retrieval

- Hybrid Search
  - FAISS
  - BM25

## Libraries

- LangChain
- LangChain Community
- LangChain HuggingFace
- LangChain Groq
- Rank BM25
- PyPDF
- Docx2txt
- OpenPyXL
- Unstructured

---

# 📁 Project Structure

```text
DocuMind-AI
│
├── app.py
│
├── data/
│
├── vector_store/
│
├── src/
│   ├── __init__.py
│   ├── document_loader.py
│   ├── create_vectorstore.py
│   ├── hybrid_search.py
│   └── rag_chain.py
│
├── requirements.txt
├── .env
├── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/documind-ai.git

cd documind-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Run the application:

```bash
streamlit run app.py
```

---

# 📖 Usage

### Step 1

Upload one or more documents.

### Step 2

Click:

```text
Process Documents
```

### Step 3

Ask questions about the uploaded documents.

Example:

```text
What is the architecture proposed in the paper?

Summarize the research gap.

What classifier achieved the best accuracy?
```

---

# 🎯 Key Highlights

- Runtime Document Upload
- Hybrid Retrieval (FAISS + BM25)
- Source Citations
- Retrieval Quality Scoring
- Multi-Document Question Answering
- Production-Inspired RAG Pipeline
- Streamlit Interactive UI

---

# 🔮 Future Enhancements

- Metadata Filtering
- Multi-User Support
- Cloud Vector Databases (Pinecone/Qdrant)
- OCR Support for Scanned PDFs
- Document Summarization
- Chat Memory
- Authentication and User Management

---

# 👩‍💻 Author

**Ekta Gupta**

B.Tech - Computer Science & Artificial Intelligence (CSAI)

Netaji Subhas University of Technology (NSUT)

---

