from recommend import recommend_movies


def get_recommendations(user_id, context):

    movies = recommend_movies(user_id, context)

    return [
        {
            "movie": movie,
            "predicted_rating": score
        }
        for movie, score in movies
    ]