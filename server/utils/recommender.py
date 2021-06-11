import pandas as pd
import scipy.sparse as sp
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import os

def get_data():
    # Get Data for Processing
    return pd.read_csv(os.path.join(os.path.dirname(__file__), '../data/processed.csv'))

def combine_tags_and_channel(data):
    # Drop Unnecessary Columns
    combined_data = data.drop(columns=['video_id', 'title', 'publish_time', 'views', 'likes', 'dislikes', 'comment_count', 'thumbnail_link', 'description'])
    
    # Combine Tags Array and Channel Title String
    combined_data['combined'] = combined_data[combined_data.columns[1:3]].apply(lambda x: ','.join(x.dropna().astype(str)),axis=1)

    # Drop Non-Combined Columns for Combined as Output 
    combined_data = combined_data.drop(columns=['tags','channel_title'])
    return combined_data

def transform_data(combined, data):
    # Create Bag of Words Matrix for Tags
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(combined['combined'])

    # Create TFIDF Matrix for Description
    # Use TFIDF since description words appearing less is more
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(data['description'].values.astype('U'))

    # Run Cosine Similarity on Sparse Matrix
    combine_sparse = sp.hstack([count_matrix, tfidf_matrix], format='csr')
    cosine_sim = cosine_similarity(combine_sparse, combine_sparse)
    return cosine_sim


def recommend_videos(video_id, data, transform, num_recs = 20):
    # Increment Num Recs for Index
    num_recs = num_recs + 1

    # Get Video's Index from Video ID
    indices = pd.Series(data.index, index = data['video_id'])
    index = indices[video_id]

    # Rank Similar Scores by Cosine Similarity
    sim_scores = list(enumerate(transform[index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recs]
    
    # Get Indices of Similar Scores
    recommended_indices = [i[0] for i in sim_scores]

    # Grab Data from Indices
    video_id = data['video_id'].iloc[recommended_indices]
    video_title = data['title'].iloc[recommended_indices]
    video_tags = data['tags'].iloc[recommended_indices]
    video_channel = data['channel_title'].iloc[recommended_indices]
    video_time = data['publish_time'].iloc[recommended_indices]
    video_thumbnail = data['thumbnail_link'].iloc[recommended_indices]
    video_description = data['description'].iloc[recommended_indices]
    video_views = data['views'].iloc[recommended_indices]

    # Throw Data into DataFrame to return
    recommended_data = pd.DataFrame(columns=['id','title','tags', 'channel', 'date', 'thumbnail', 'description', 'views'])
    recommended_data['id'] = video_id
    recommended_data['title'] = video_title
    recommended_data['tags'] = video_tags
    recommended_data['channel'] = video_channel
    recommended_data['date'] = video_time
    recommended_data['thumbnail'] = video_thumbnail
    recommended_data['description'] = video_description
    recommended_data['views'] = video_views
    return recommended_data


def results(video_id):
    # Prepare Data
    video_data = get_data()
    combined_video_data = combine_tags_and_channel(video_data)
    transform_video_data = transform_data(combined_video_data, video_data)
    
    # Validate Entry in Database
    # TODO: Could likely remove this check, inefficient once API is complete
    if video_id not in video_data['video_id'].unique():
        return 'Video Does Not Exist'
    
    else:
        recommendations = recommend_videos(video_id, video_data, transform_video_data, 10)
        return recommendations.to_dict('records')


def format_data(data):
    data = data.rename(columns={"video_id": "id", "channel_title": "channel", "publish_time": "date", "thumbnail_link": "thumbnail"})
    data = data.drop(columns=["dislikes", "likes", "comment_count"])
    data = data.iloc[:,1:]
    return data.to_dict('records')


def format_light_data(data):
    data = data.rename(columns={"video_id": "id", "channel_title": "channel", "publish_time": "date", "thumbnail_link": "thumbnail"})
    data = data.drop(columns=["dislikes", "likes", "comment_count", "tags", "description"])
    data = data.iloc[:,1:]
    return data.to_dict('records')


def get_random(num = 8):
    data = get_data()
    data = data.sample(n = num)
    return format_light_data(data)
    

def get_video(id):
    data = get_data()
    video = data.loc[data['video_id'] == id]
    return format_data(video)