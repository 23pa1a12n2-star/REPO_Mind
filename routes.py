from flask import request, jsonify

def register_routes(app, rag_engine):
    """Register all application routes with the Flask app instance."""
    
    @app.route('/health', methods=['GET'])
    def health_check():
        status = "healthy" if rag_engine else "degraded (missing API key)"
        return jsonify({"status": status, "service": "RepoMind AI Backend"}), 200

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
                return jsonify({"error": result.get('message', 'Unknown error during indexing')}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500

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
