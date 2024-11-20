from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load knowledge base (as in your original script)
def load_knowledge_base(file_path):

# Define API endpoint for querying the LLM
app.route('/query', methods=['POST'])
def query_llm():
    query = request.json['query']
    response = query_knowledge_base(load_knowledge_base('personal_knowledge_base.json'), query)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
