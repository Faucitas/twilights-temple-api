from flask import Flask, request, jsonify, Response, session
from flask_sock import Sock
from polly import polly_request

from oracle import ask_the_oracle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'

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
    message = data.get('message')
    chat_log = session.get('chat_log')

    answer, chat_log = ask_the_oracle(message, chat_log)
    session['chat_log'] = chat_log

    return jsonify({'answer': answer})
