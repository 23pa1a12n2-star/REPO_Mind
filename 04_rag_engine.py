import os
import shutil
import git
from typing import List, Optional
from langchain_groq import ChatGroq
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings

class RAGEngine:
    def __init__(self, persist_directory: str = "./chroma_db"):
        self.persist_directory = persist_directory
        # Ensure Groq API key is set
        if not os.getenv("GROQ_API_KEY"):
            raise ValueError("GROQ_API_KEY environment variable is not set")
        
        # Use FREE local HuggingFace embeddings - NO API RATE LIMITS!
        print("Loading local embedding model (first time may take a minute to download)...")
        self.embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
        print("Embedding model loaded successfully!")
        
        # Use Groq for fast, free LLM inference
        self.llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
        self.vector_store = None
        self._load_existing_db()

    def _load_existing_db(self):
        if os.path.exists(self.persist_directory):
            self.vector_store = Chroma(
                persist_directory=self.persist_directory, 
                embedding_function=self.embeddings
            )

    def ingest_repo(self, repo_url: str) -> dict:
        """
        Clones and indexes the repository.
        Returns a summary of the indexing process.
        """
        import time
        import stat
        import tempfile

        # Use system temp directory to avoid Flask auto-reload
        temp_dir = os.path.join(tempfile.gettempdir(), "repomind_temp_repo")

        # Helper to handle Windows read-only files during deletion
        def on_rm_error(func, path, exc_info):
            os.chmod(path, stat.S_IWRITE)
            func(path)
        
        # 1. Clean up previous temp repo if exists
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, onerror=on_rm_error)
            
        try:
            # 2. Clone repository
            print(f"Cloning {repo_url}...")
            git.Repo.clone_from(repo_url, temp_dir)
            
            # 3. Load documents (filtering for text/code files only)
            # Define supported code/text file extensions
            supported_extensions = [
                "*.py", "*.js", "*.ts", "*.jsx", "*.tsx",  # Python, JavaScript, TypeScript
                "*.java", "*.c", "*.cpp", "*.h", "*.hpp", "*.cs",  # Java, C/C++, C#
                "*.go", "*.rs", "*.rb", "*.php", "*.swift", "*.kt",  # Go, Rust, Ruby, PHP, Swift, Kotlin
                "*.html", "*.css", "*.scss", "*.sass", "*.less",  # Web
                "*.json", "*.yaml", "*.yml", "*.toml", "*.xml",  # Config
                "*.md", "*.txt", "*.rst", "*.ini", "*.cfg",  # Docs/Config
                "*.sql", "*.sh", "*.bash", "*.zsh", "*.ps1",  # Scripts
                "*.vue", "*.svelte", "*.astro",  # Frontend frameworks
                "*.env.example", "Dockerfile", "Makefile",  # Dev files
            ]
            
            all_docs = []
            for ext in supported_extensions:
                try:
                    loader = DirectoryLoader(
                        temp_dir, 
                        glob=f"**/{ext}",
                        loader_cls=TextLoader,
                        loader_kwargs={"autodetect_encoding": True, "encoding": "utf-8"},
                        show_progress=False,
                        use_multithreading=True,
                        silent_errors=True,
                        exclude=["**/.git/**", "**/node_modules/**", "**/__pycache__/**", "**/venv/**"]
                    )
                    docs = loader.load()
                    all_docs.extend(docs)
                except Exception as e:
                    print(f"Warning: Could not load {ext} files: {e}")
                    continue
            
            docs = all_docs
            print(f"Loaded {len(docs)} documents.")

            if not docs:
                return {"status": "warning", "message": "No text documents found in repository."}

            # 4. Split text
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                add_start_index=True
            )
            splits = text_splitter.split_documents(docs)
            print(f"Created {len(splits)} chunks.")

            # 5. Create/Update VectorStore (local embeddings - no rate limits!)
            print("Creating vector embeddings (local - no API limits)...")
            
            if self.vector_store is None:
                self.vector_store = Chroma.from_documents(
                    documents=splits, 
                    embedding=self.embeddings,
                    persist_directory=self.persist_directory
                )
            else:
                self.vector_store.add_documents(splits)
            
            print("Indexing complete!") 
            
            return {
                "status": "success", 
                "files_processed": len(docs),
                "chunks_created": len(splits)
            }
            
        except Exception as e:
            print(f"Error indexing repo: {e}")
            # Identify specific errors for better user feedback
            if "429" in str(e):
                return {"status": "error", "message": "Rate limit exceeded. Please try a smaller repo or wait a moment."}
            return {"status": "error", "message": str(e)}
            
        finally:
            # Cleanup: remove the cloned repo to save space
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir, onerror=on_rm_error)

    def query(self, question: str) -> str:
        """
        Queries the vector store and generates an answer.
        """
        if not self.vector_store:
            return "Repository has not been indexed yet. Please upload a repo first."
        
        # Retrieve relevant docs
        retriever = self.vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})
        retrieved_docs = retriever.invoke(question)
        
        # Format context
        context = "\n\n".join([d.page_content for d in retrieved_docs])
        
        # Generate Answer
        # We construct a simple prompt here. In a larger app, use LangChain Chains.
        prompt = f"""You are a helpful coding assistant. Use the following pieces of context to answer the user's question about the codebase.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        
        Context:
        {context}
        
        Question: {question}
        
        Answer:"""
        
        response = self.llm.invoke(prompt)
        return response.content
