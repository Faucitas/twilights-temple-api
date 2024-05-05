from flask import Flask, jsonify, request
from temple_god import generate_response

def create_app():
    app = Flask(__name__)

    @app.route("/hello")
    def hello():
        return jsonify(message="Hello, World!")

    @app.route('/god')
    def god():
        data = request.get_json()
        prompt = data.get("prompt")
        answer = generate_response(prompt)
        return jsonify(data)

    @app.route('/error')
    def error():
        return jsonify(error="Something went wrong"), 500

    return app


# if __name__ == '__main__':
    # app = create_app()
#     app.run(debug=True)
