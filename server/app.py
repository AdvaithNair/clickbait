from flask import Flask
from flask_cors import CORS
# import server.routes.user as user

app = Flask(__name__)
# CORS(app)

@app.route('/user')
def user_hello():
    # user.hello_user()
    return "x";

@app.route('/')
def hello():
    return "Hello"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)