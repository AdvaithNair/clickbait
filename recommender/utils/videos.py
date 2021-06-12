import pandas as pd
import os
import ast
import utils.recommender as recommender

'''
Gets Random Videos from Dataset

num: number of videos to get from dataset

Returns formatted dictionary of random preview videos
'''
def get_random(num = 8):
    data = recommender.get_data()
    data = data.sample(n = num)
    return format_light_data(data)
    
'''
Gets Singular Video from Dataset

id: ID of video to get from dataset

Returns formatted dictionary of singular full video
'''
def get_video(id):
    data = recommender.get_data()
    video = data.loc[data['video_id'] == id]
    return format_data(video)


'''
Formats Data for Full Video Page

data: DataFrame of videos to be formatted (usually 1 row)

Returns formatted full video dictionary of data
'''
def format_data(data):
    data = data.rename(columns={"video_id": "id", "channel_title": "channel", "publish_time": "date", "thumbnail_link": "thumbnail"})
    data = data.drop(columns=["dislikes", "likes", "comment_count"])
    data['tags'] = data['tags'].apply(literal_return)
    data = data.iloc[:,1:]
    return data.to_dict('records')

'''
Formats Data for Preview Component

data: DataFrame of videos to be formatted

Returns formatted preview video dictionary of data
'''
def format_light_data(data):
    data = data.rename(columns={"video_id": "id", "channel_title": "channel", "publish_time": "date", "thumbnail_link": "thumbnail"})
    data = data.drop(columns=["dislikes", "likes", "comment_count", "tags", "description"])
    data = data.iloc[:,1:]
    return data.to_dict('records')

'''
Formats Tags Array for JSON Response

val: tag value from dataframe

Returns accurate value for formatted tag
'''
def literal_return(val):
    try:
        return ast.literal_eval(val)
    except (ValueError, SyntaxError) as e:
        return val