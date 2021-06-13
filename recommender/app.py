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
Get Details for Featured Video

id: ID of featured video
'''
@app.route('/api/recommender/videos', methods=['GET'])
def get_video():
    video_id = request.args.get('id')
    res = videos.get_video(video_id)
    return jsonify(res)


'''
Gets Similar Videos to Featured Video

id: ID of featured video
count: number of videos to get
'''
@app.route('/api/recommender/videos/recommend', methods=['GET'])
def recommend():
    # video_id = '2kyS6SvSYSE'
    video_id = request.args.get('id')
    count = request.args.get('count')
    if count is None:
        count = 4
    else:
        count = int(count)

    res = recommender.results(video_id, count)
    return jsonify(res)


'''
Gets Random Videos

num: number of videos to get
'''
@app.route('/api/recommender/videos/random', methods=['GET'])
def random_recommend():
    count = request.args.get('num')
    if count is None:
        count = 8
    else:
        count = int(count)
    res = videos.get_random(count)
    return jsonify(res)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)