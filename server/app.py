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


@app.route('/api/user')
def hello_user():
    print('Here')
    return "MAIN Hello"


@app.route('/api/videos/', methods=['GET'])
def get_video():
    video_id = request.args.get('id')
    res = recommender.get_video(video_id)
    return jsonify(res)


@app.route('/api/videos/recommend', methods=['GET'])
def recommend():
    # video_id = '2kyS6SvSYSE'
    video_id = request.args.get('id')
    count = int(request.args.get('count'))
    res = recommender.results(video_id, count)
    return jsonify(res)


@app.route('/api/videos/random', methods=['GET'])
def random_recommend():
    res = recommender.get_random()
    return jsonify(res)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)