import pickle
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import StandardScaler

def load_preprocessed_data():
    with open('data/user_movie_matrix.pkl', 'rb') as f:
        user_movie_matrix = pickle.load(f)
    return user_movie_matrix

def train_model(user_movie_matrix):
    # Normalisation des données
    scaler = StandardScaler(with_mean=False)  # with_mean=False because the matrix is sparse
    normalized_data = scaler.fit_transform(user_movie_matrix)

    # Réduction de dimension avec SVD
    svd = TruncatedSVD(n_components=50, random_state=42)
    matrix_reduced = svd.fit_transform(normalized_data)

    return svd, matrix_reduced, scaler

def save_model(svd, scaler):
    with open('models/svd_model.pkl', 'wb') as model_file:
        pickle.dump((svd, scaler), model_file)

if __name__ == "__main__":
    user_movie_matrix = load_preprocessed_data()
    svd, matrix_reduced, scaler = train_model(user_movie_matrix)
    save_model(svd, scaler)
