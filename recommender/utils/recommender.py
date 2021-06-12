import pandas as pd
import scipy.sparse as sp
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import os
import ast

'''
Gets Full CSV DataSet

Returns DataFrame of videos dataset
'''
def get_data():
    # Get Data for Processing
    return pd.read_csv(os.path.join(os.path.dirname(__file__), '../data/processed.csv'))


'''
Modifies Data for Bag of Words

data: DataFrame of videos dataset

Returns DataFrame with combined column of tags and channel
'''
def combine_tags_and_channel(data):
    # Drop Unnecessary Columns
    combined_data = data.drop(columns=['video_id', 'title', 'publish_time', 'views', 'likes', 'dislikes', 'comment_count', 'thumbnail_link', 'description'])
    
    # Combine Tags Array and Channel Title String
    combined_data['combined'] = combined_data[combined_data.columns[1:3]].apply(lambda x: ','.join(x.dropna().astype(str)),axis=1)

    # Drop Non-Combined Columns for Combined as Output 
    combined_data = combined_data.drop(columns=['tags','channel_title'])
    return combined_data


'''
Applies Natural Language Processing to Data

combined: DataFrame with combined column of tags and channel
data: DataFrame of videos dataset

Returns Cosine Similarity Matrix on all videos
'''
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


'''
Gets Recommended Videos

video_id: ID of video to recommend similar videos to
data: DataFrame of videos dataset
transform: Cosine Similarity Matrix on all videos
num_recs: Number of similar videos to recommend

Returns DataFrame of the most similar videos
'''
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
    # TODO: Reduce the number of parameters here
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

'''
Formats Recommended Videos

video_id: ID of video to recommend similar videos to
num_recs: Number of similar videos to recommend

Returns Dictionary formatted list of recommended preview videos or None
'''
def results(video_id, num_recs):
    # Prepare Data
    video_data = get_data()
    combined_video_data = combine_tags_and_channel(video_data)
    transform_video_data = transform_data(combined_video_data, video_data)
    
    # Validate Entry in Database
    if video_id not in video_data['video_id'].unique():
        return None
    
    # Recommend
    else:
        recommendations = recommend_videos(video_id, video_data, transform_video_data, num_recs)
        return recommendations.to_dict('records')