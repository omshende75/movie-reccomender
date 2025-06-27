import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def load_data():
    ratings = pd.read_csv("data/ratings.csv")
    movies = pd.read_csv("data/movies.csv")
    movies = pd.concat([movies, movies['genres'].str.get_dummies(sep='|')], axis=1)
    return ratings, movies

def preprocess_data(ratings, movies):
    user_movie_matrix = ratings.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
    rated_movie_ids = user_movie_matrix.columns
    filtered_movies = movies[movies['movieId'].isin(rated_movie_ids)].copy()
    genre_features = filtered_movies.drop(columns=['movieId', 'title', 'genres']).set_index(filtered_movies['movieId'])
    movie_sim = cosine_similarity(user_movie_matrix.T)
    genre_sim = cosine_similarity(genre_features.fillna(0))
    return user_movie_matrix, movie_sim, genre_sim, genre_features.index

def recommend_movies(movie_id, movie_sim_df, genre_sim_df, movies, top_n=5):
    if movie_id not in movie_sim_df.index or movie_id not in genre_sim_df.index:
        return pd.DataFrame()
    hybrid_score = 0.6 * movie_sim_df[movie_id] + 0.4 * genre_sim_df[movie_id]
    top_movies = hybrid_score.sort_values(ascending=False).drop(movie_id).head(top_n).index
    return movies[movies['movieId'].isin(top_movies)][['movieId', 'title']]
