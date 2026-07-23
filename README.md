# REPO_Mind
An AI-powered RAG chatbot to analyze and query any GitHub repository in seconds using LangChain, Groq LLaMA 3.3, and ChromaDB.

Markdown# 🧠 RepoMind.ai

**Understand any codebase in seconds with AI-powered RAG (Retrieval-Augmented Generation)**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.2+-orange.svg)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3-purple.svg)
![ChromaDB](https://img.shields.io/badge/Vector_DB-ChromaDB-red.svg)

RepoMind is an enterprise-grade AI-powered chatbot that helps developers understand codebases quickly. Simply paste a GitHub repository URL, and start asking questions about the code!

## ✨ Features

- 🔍 **Smart Code Search** - Semantic search across entire repositories using advanced RAG and language-aware chunking.
- 🚀 **Fast Indexing** - Local HuggingFace embeddings (`all-MiniLM-L6-v2`) with no API rate limits.
- 💬 **Natural Language Q&A** - Ask questions about code in plain English.
- ⚡ **Blazing Fast Responses** - Powered by Groq's ultra-fast `llama-3.3-70b-versatile` LLM inference.
- 🎨 **Modern UI** - Beautiful glassmorphism design with TailwindCSS.

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | HTML, TailwindCSS, JavaScript |
| **Backend** | Flask (Python) |
| **Embeddings** | HuggingFace `all-MiniLM-L6-v2` (Local, Free) |
| **LLM** | Groq `llama-3.3-70b-versatile` |
| **Vector Store** | ChromaDB |
| **Framework** | LangChain |

## 📋 Prerequisites

- Python 3.10+
- Git
- [Groq API Key](https://console.groq.com/keys) (Free)

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone [https://github.com/YOUR_USERNAME/RepoMind.git](https://github.com/YOUR_USERNAME/RepoMind.git)
cd RepoMind
2. Create a virtual environmentBashpython -m venv venv

# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
3. Install dependenciesBashpip install -r requirements.txt
4. Set up environment variablesCreate a .env file in the project root:Code snippetGROQ_API_KEY="your-groq-api-key-here"
Get your free Groq API key from: https://console.groq.com/keys5. Run the applicationBashpython app.py
6. Open in browserNavigate to http://localhost:5000 and start exploring codebases!📖 How It Works┌─────────────────────────────────────────────────────────────┐
│  1. CONNECT                                                 │
│     Paste a GitHub repository URL                           │
└─────────────────────────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────┐
│  2. INDEX                                                   │
│     • Clone repository                                      │
│     • Recursive language-aware code splitting               │
│     • Generate embeddings (local HuggingFace)               │
│     • Store in ChromaDB vector database                     │
└─────────────────────────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────┐
│  3. QUERY                                                   │
│     • Ask questions in natural language                     │
│     • Retrieve relevant code snippets via similarity search │
│     • Generate answers using Groq LLaMA 3.3                 │
└─────────────────────────────────────────────────────────────┘
📁 Project StructurePlaintextRepoMind/
├── app.py              # Flask backend server
├── rag_engine.py       # RAG pipeline (embedding, retrieval, generation)
├── templates/
│   └── index.html      # Frontend UI
├── static/
│   ├── styles.css      # Custom CSS styles
│   └── script.js       # Frontend JavaScript logic
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (not committed)
└── chroma_db/          # Vector database storage (auto-generated)
🔧 ConfigurationEnvironment VariableDescriptionRequiredGROQ_API_KEYYour Groq API key for LLM✅ Yes📝 Supported File TypesThe RAG engine indexes the following file types:Programming: .py, .js, .ts, .jsx, .tsx, .java, .c, .cpp, .go, .rs, .rb, .php, .swift, .ktWeb: .html, .css, .scss, .vue, .svelteConfig: .json, .yaml, .yml, .toml, .xmlDocs: .md, .txt, .rstScripts: .sql, .sh, .bash, .ps1🗺️ Roadmap & Future Enhancements[ ] Hybrid Search (Ensemble Retriever): Combine semantic vector search with BM25 lexical keyword matching.[ ] Streaming Responses: Implement Server-Sent Events (SSE) for real-time token streaming.[ ] Dependency Mapping: Parse dependency manifests for macro-level architectural overviews.🤝 ContributingContributions are welcome! Please feel free to submit a Pull Request.📄 LicenseThis project is licensed under the MIT License - see the LICENSE file for details.🙏 AcknowledgmentsLangChain for the RAG frameworkGroq for lightning-fast LLM inferenceHuggingFace for free embedding modelsChromaDB for vector storageMade with ❤️ by developers, for developers.
