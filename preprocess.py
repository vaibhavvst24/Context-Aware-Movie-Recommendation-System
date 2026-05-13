import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data():

    # Load dataset
    ratings = pd.read_csv("data/ml-latest-small/ratings.csv")
    movies = pd.read_csv("data/ml-latest-small/movies.csv")

    # Merge datasets
    df = pd.merge(ratings, movies, on="movieId")

    # Create context feature from timestamp
    df['datetime'] = pd.to_datetime(df['timestamp'], unit='s')
    df['hour'] = df['datetime'].dt.hour

    def get_time_of_day(hour):
        if hour < 12:
            return 0  # Morning
        elif hour < 18:
            return 1  # Evening
        else:
            return 2  # Night

    df['time_context'] = df['hour'].apply(get_time_of_day)

    # Encode users and movies
    user_encoder = LabelEncoder()
    movie_encoder = LabelEncoder()

    df['user'] = user_encoder.fit_transform(df['userId'])
    df['movie'] = movie_encoder.fit_transform(df['movieId'])

    return df, user_encoder, movie_encoder