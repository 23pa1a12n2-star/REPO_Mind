# 🧠 RepoMind.ai

> **Understand any GitHub codebase in seconds with AI-powered Retrieval-Augmented Generation (RAG).**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.2+-orange.svg)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3-purple.svg)
![ChromaDB](https://img.shields.io/badge/Vector_DB-ChromaDB-red.svg)

---

# 📖 Overview

**RepoMind.ai** is an AI-powered RAG (Retrieval-Augmented Generation) application that helps developers understand unfamiliar GitHub repositories through natural language conversations.

Instead of manually browsing hundreds of files, simply paste a GitHub repository URL. RepoMind automatically:

- Clones the repository
- Indexes the source code
- Generates vector embeddings
- Retrieves relevant code snippets
- Produces context-aware answers using Groq's LLaMA 3.3 model

Whether you're exploring an open-source project, reviewing a teammate's code, or onboarding to a new codebase, RepoMind significantly reduces the time required to understand complex repositories.

---

# ✨ Features

- 🔍 **Semantic Code Search**
  - Finds relevant code based on meaning instead of exact keywords.

- 🚀 **Fast Repository Indexing**
  - Automatically clones repositories and indexes supported source files.

- 🧠 **Language-Aware Code Chunking**
  - Splits code intelligently for better retrieval accuracy.

- 📚 **Local Embeddings**
  - Uses HuggingFace `all-MiniLM-L6-v2` embeddings locally.
  - No embedding API costs or rate limits.

- 💬 **Natural Language Q&A**
  - Ask questions in plain English about any repository.

- ⚡ **Ultra-Fast AI Responses**
  - Powered by Groq's blazing-fast `llama-3.3-70b-versatile`.

- 🗂️ **Persistent Vector Database**
  - Stores embeddings using ChromaDB for efficient similarity search.

- 🎨 **Modern Responsive UI**
  - Glassmorphism interface built with TailwindCSS.

---

# 🛠 Tech Stack

| Component | Technology | Purpose |
|------------|------------|---------|
| **Frontend** | HTML, TailwindCSS, JavaScript | User Interface |
| **Backend** | Flask (Python) | API & Server |
| **Embeddings** | HuggingFace `all-MiniLM-L6-v2` | Local Vector Embeddings |
| **LLM** | Groq `llama-3.3-70b-versatile` | Answer Generation |
| **Vector Database** | ChromaDB | Semantic Retrieval |
| **Framework** | LangChain | RAG Pipeline |

---

# 🏗 System Architecture

```
                GitHub Repository
                        │
                        ▼
               Clone Repository
                        │
                        ▼
         Language-Aware Code Chunking
                        │
                        ▼
      HuggingFace Embedding Generation
                        │
                        ▼
             ChromaDB Vector Store
                        │
                        ▼
              Similarity Retrieval
                        │
                        ▼
              Retrieved Code Chunks
                        │
                        ▼
          Groq LLaMA 3.3 (Generation)
                        │
                        ▼
               AI-Powered Response
```

---

# 🔄 How It Works

```
                 User enters GitHub URL
                          │
                          ▼
                Repository is cloned
                          │
                          ▼
        Source files are recursively scanned
                          │
                          ▼
        Language-aware code chunking performed
                          │
                          ▼
      Embeddings generated using HuggingFace
                          │
                          ▼
        Stored inside ChromaDB Vector Store
                          │
──────────────────────────────────────────────────
                     User asks a question
                          │
                          ▼
         Similarity search retrieves context
                          │
                          ▼
       Relevant code sent to Groq LLM
                          │
                          ▼
          Context-aware answer generated
```

---

# 📂 Project Structure

```
RepoMind/
│
├── app.py
│   ├── Flask backend
│   └── API endpoints
│
├── rag_engine.py
│   ├── Repository cloning
│   ├── Code chunking
│   ├── Embedding generation
│   ├── ChromaDB indexing
│   └── Question answering
│
├── templates/
│   └── index.html
│
├── static/
│   ├── styles.css
│   └── script.js
│
├── requirements.txt
│
├── .env
│
├── chroma_db/
│
└── README.md
```

---

# 🚀 Quick Start

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/RepoMind.git

cd RepoMind
```

---

## 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
.\venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file inside the project root.

```env
GROQ_API_KEY="your-groq-api-key"
```

Get your free API key from:

https://console.groq.com/keys

---

## 5️⃣ Run the Application

```bash
python app.py
```

---

## 6️⃣ Open the Browser

Visit

```
http://localhost:5000
```

Paste any GitHub repository URL and start asking questions.

---

# ⚙ Configuration

| Environment Variable | Description | Required |
|----------------------|-------------|----------|
| `GROQ_API_KEY` | Groq API Key | ✅ Yes |

---

# 📄 Supported File Types

### Programming Languages

- Python (`.py`)
- Java (`.java`)
- JavaScript (`.js`)
- TypeScript (`.ts`)
- React (`.jsx`, `.tsx`)
- C (`.c`)
- C++ (`.cpp`)
- Go (`.go`)
- Rust (`.rs`)
- Ruby (`.rb`)
- PHP (`.php`)
- Kotlin (`.kt`)
- Swift (`.swift`)

### Web Technologies

- HTML
- CSS
- SCSS
- Vue
- Svelte

### Configuration Files

- JSON
- YAML
- TOML
- XML

### Documentation

- Markdown
- TXT
- RST

### Scripts

- SQL
- Shell
- Bash
- PowerShell

---

# 🎯 Why RepoMind?

Understanding a new repository often takes hours of manually exploring folders, reading files, and tracing function calls.

RepoMind accelerates this process by combining semantic search with Retrieval-Augmented Generation (RAG), allowing developers to interact with an entire codebase using natural language.

---

# 🗺 Roadmap

- [ ] Hybrid Search (Vector + BM25)
- [ ] Streaming Responses (SSE)
- [ ] Repository Summarization
- [ ] Dependency Graph Visualization
- [ ] Multi-Repository Search
- [ ] Docker Deployment
- [ ] Cloud Deployment
- [ ] Conversation Memory
- [ ] Authentication & User Accounts

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve RepoMind, feel free to:

- Fork the repository
- Create a new feature branch
- Commit your changes
- Submit a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

See the **LICENSE** file for more information.

---

# Acknowledgements

- **LangChain** — RAG framework
- **Groq** — Ultra-fast LLM inference
- **HuggingFace** — Local embedding models
- **ChromaDB** — Vector database
- **Flask** — Backend framework

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

**Made with ❤️ by developers, for developers.**

</div>
