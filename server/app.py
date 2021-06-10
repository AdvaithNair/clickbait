# Dependencies
from flask import Flask,request,jsonify
from flask_cors import CORS

# Utils
import utils.secrets as secrets
import utils.recommender as recommender

# Routes
from routes import user

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return secrets.MONGODB_URL

@app.route('/user')
def hello_user():
    print('Here')
    return "MAIN Hello"

@app.route('/rec', methods=['GET'])
def recommend():
    # video_id = request.args.get('id')
    video_id = '2kyS6SvSYSE'
    res = recommender.results(video_id)
    return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)