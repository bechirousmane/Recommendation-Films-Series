import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from database import session, Rating, Movie

class Recommender:
    def __init__(self):
        self.movies = pd.read_sql(session.query(Movie).statement, session.bind)
        self.ratings = pd.read_sql(session.query(Rating).statement, session.bind)
        self.user_movie_matrix = self._create_user_movie_matrix()

    def _create_user_movie_matrix(self):
        df = self.ratings.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)
        return df

    def recommend_movies(self, user_id, num_recommendations=5):
        user_ratings = self.user_movie_matrix.loc[user_id].values.reshape(1, -1)
        similarity_matrix = cosine_similarity(user_ratings, self.user_movie_matrix)
        similar_users = similarity_matrix.argsort().flatten()[-num_recommendations:]
        recommended_movies = self.ratings[self.ratings['user_id'].isin(similar_users)]['movie_id'].unique()
        return self.movies[self.movies['id'].isin(recommended_movies)].title.tolist()

