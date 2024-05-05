from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route("/hello")
    def hello():
        return jsonify(message="Hello, World!")

    @app.route('/user')
    def user():
        user_info = {
            "name": "Alice",
            "age": 30,
            "city": "New York"
        }
        return jsonify(user_info)

    @app.route('/error')
    def error():
        return jsonify(error="Something went wrong"), 500

    return app


# if __name__ == '__main__':
#     app = create_app()
#     app.run(debug=True)
