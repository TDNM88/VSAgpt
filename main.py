from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from create_file import create_text_file
from send_email import send_email

app = Flask(__name__)
CORS(app)

# Get the API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/create_file', methods=['POST'])
def api_create_file():
    data = request.json
    conversation = data.get('conversation')
    filename = data.get('filename')
    file_format = data.get('file_format')
    
    result = create_text_file(conversation, filename, file_format, openai.api_key)
    return jsonify(result)

@app.route('/send_email', methods=['POST'])
def api_send_email():
    data = request.json
    subject = data.get('subject')
    body = data.get('body')
    to_email = data.get('to_email')
    filename = data.get('filename')
    
    result = send_email(subject, body, to_email, filename)
    return jsonify(result)

if __name__ == "__main__":
    app.run()
