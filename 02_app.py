import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from rag_engine import RAGEngine
from routes import register_routes  # Import the function that registers your endpoints

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize RAG Engine
try:
    rag_engine = RAGEngine()
except ValueError as e:
    print(f"Error initializing RAG Engine: {e}")
    rag_engine = None

# Register API routes and pass the rag_engine instance
register_routes(app, rag_engine)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
