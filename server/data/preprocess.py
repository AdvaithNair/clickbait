# Get Pandas
import pandas as pd

# Get Raw Data
raw_data = pd.read_csv('raw.csv')

# Drop Unnecessary Columns
data = raw_data.drop(['trending_date', 'category_id', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed'], axis = 1)

# Format Tags
def format_tags(s):
    return s.replace('"', '').split('|')

data['tags'] = data['tags'].apply(format_tags)

# Export to CSV
data.to_csv('processed.csv')