import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
import pickle

def load_data():
    movies = pd.read_csv('data/movies.csv')
    ratings = pd.read_csv('data/ratings.csv')
    return movies, ratings

def preprocess_data(ratings):
    user_movie_matrix = csr_matrix((ratings['rating'], (ratings['userId'], ratings['movieId'])))
    return user_movie_matrix

def save_preprocessed_data(user_movie_matrix):
    with open('data/user_movie_matrix.pkl', 'wb') as f:
        pickle.dump(user_movie_matrix, f)

if __name__ == "__main__":
    movies, ratings = load_data()
    user_movie_matrix = preprocess_data(ratings)
    save_preprocessed_data(user_movie_matrix)
