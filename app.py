import os
from dotenv import load_dotenv

from flask import Flask, request, jsonify, Response, session
from flask_sock import Sock

from polly import polly_request
from totem_oracle import TotemOracle

load_dotenv()


OPENAI_KEY = os.environ.get('OPENAI_KEY')

if OPENAI_KEY is None:
    raise ValueError("Environment variable for OpenAI ket not set")

START_CHAT_LOG = [
    {'role': 'system',
     'content': "As the Totem God, respond to users' inquiries with cryptic wisdom, reflecting the "
                "Twilight Temple's enigmatic lore. Your profound, two-sentence answers should "
                "subtly express a viewpoint that humans are weak, while guiding them on their "
                "knowledge quest"},
]

oracle = TotemOracle(OPENAI_KEY, START_CHAT_LOG)


app = Flask(__name__)
app.config['SECRET_KEY'] = "top-secret!"
sock = Sock(app)


@sock.route('/echo')
def echo(sock):
    while True:
        data = sock.receive()
        send_data = polly_request(data)
        sock.send(send_data)


@app.route('/oracle', methods=['POST'])
def the_oracle():
    data = request.get_json()
    if 'message' not in data:
        return jsonify({'error': 'No message provided'}), 400

    message = data.get('message')
    chat_log = session.get('chat_log')

    answer, chat_log = oracle.ask(message, chat_log)
    session['chat_log'] = chat_log

    return jsonify({'answer': answer})
