import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
from rag_engine import RAGEngine

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


# =========================
# Home Page
# =========================
@app.route('/')
def home():
    return render_template("index.html")


# =========================
# Health Check
# =========================
@app.route('/health', methods=['GET'])
def health_check():
    status = "healthy" if rag_engine else "degraded (missing API key)"
    return jsonify({
        "status": status,
        "service": "RepoMind AI Backend"
    }), 200


# =========================
# Index GitHub Repository
# =========================
@app.route('/api/index-repo', methods=['POST'])
def index_repo():

    if not rag_engine:
        return jsonify({"error": "RAG Engine not initialized. Check server logs."}), 500

    data = request.json
    repo_url = data.get('repo_url')

    if not repo_url:
        return jsonify({"error": "repo_url is required"}), 400

    try:
        result = rag_engine.ingest_repo(repo_url)

        if result['status'] == 'success':
            return jsonify({
                "message": f"Successfully indexed {repo_url}",
                "details": result
            }), 200
        else:
            return jsonify({
                "error": result.get('message', 'Unknown error during indexing')
            }), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =========================
# Chat with Repository
# =========================
@app.route('/api/chat', methods=['POST'])
def chat():

    if not rag_engine:
        return jsonify({"error": "RAG Engine not initialized."}), 500

    data = request.json
    query = data.get('query')

    if not query:
        return jsonify({"error": "query is required"}), 400

    try:
        answer = rag_engine.query(query)

        return jsonify({
            "answer": answer,
            "sources": []
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
