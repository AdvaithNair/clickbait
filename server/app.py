# Dependencies
from flask import Flask,request,jsonify
from flask_cors import CORS

# Utils
import utils.secrets as secrets
import utils.recommender as recommender
import utils.videos as videos

app = Flask(__name__)
CORS(app)


'''
Test Route
'''
@app.route('/')
def hello():
    return secrets.MONGODB_URL


'''
Test Route
'''
@app.route('/api/user')
def hello_user():
    print('Here')
    return "MAIN Hello"


'''
Get Details for Featured Video

id: ID of featured video
'''
@app.route('/api/videos/', methods=['GET'])
def get_video():
    video_id = request.args.get('id')
    res = videos.get_video(video_id)
    return jsonify(res)


'''
Gets Similar Videos to Featured Video

id: ID of featured video
count: number of videos to get
'''
@app.route('/api/videos/recommend', methods=['GET'])
def recommend():
    # video_id = '2kyS6SvSYSE'
    video_id = request.args.get('id')
    count = int(request.args.get('count'))
    if count is None:
        count = 4
    res = recommender.results(video_id, count)
    return jsonify(res)


'''
Gets Random Videos

num: number of videos to get
'''
@app.route('/api/videos/random', methods=['GET'])
def random_recommend():
    count = int(request.args.get('num'))
    if count is None:
        count = 8
    res = videos.get_random(count)
    return jsonify(res)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)