from flask import Flask
from flask_sock import Sock
from polly import polly_request

app = Flask(__name__)
sock = Sock(app)

@sock.route('/echo')
def echo(sock):
    while True:
        data = sock.receive()
        send_data = polly_request(data)
        sock.send(send_data)

