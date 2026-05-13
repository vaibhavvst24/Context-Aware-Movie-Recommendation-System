import torch
import pandas as pd
from preprocess import load_data
from model import RecommenderNet

# Load dataset
df, user_encoder, movie_encoder = load_data()

movies_df = pd.read_csv("data/ml-latest-small/movies.csv")

# Model parameters
num_users = df['user'].nunique()
num_movies = df['movie'].nunique()

# Load model
model = RecommenderNet(num_users, num_movies)

model.load_state_dict(
    torch.load("models/recommender.pth")
)

model.eval()


def recommend_movies(user_id, context_value, top_k=5):

    recommendations = []

    # Encode user
    encoded_user = user_encoder.transform([user_id])[0]

    for movie_id in df['movie'].unique():

        user_tensor = torch.tensor(
            [encoded_user],
            dtype=torch.long
        )

        movie_tensor = torch.tensor(
            [movie_id],
            dtype=torch.long
        )

        context_tensor = torch.tensor(
            [[context_value]],
            dtype=torch.float32
        )

        with torch.no_grad():
            prediction = model(
                user_tensor,
                movie_tensor,
                context_tensor
            )

        score = prediction.item()

        recommendations.append((movie_id, score))

    # Sort by score
    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    # Top recommendations
    top_movies = recommendations[:top_k]

    results = []

    for movie_encoded, score in top_movies:

        original_movie_id = movie_encoder.inverse_transform(
            [movie_encoded]
        )[0]

        movie_title = movies_df[
            movies_df['movieId'] == original_movie_id
        ]['title'].values[0]

        results.append((movie_title, round(score, 2)))

    return results