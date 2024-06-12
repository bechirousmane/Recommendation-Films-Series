from movie import MovieManager
from user import UserManager
from recommendation import Recommender

def main():
    movie_manager = MovieManager()
    user_manager = UserManager()
    recommender = Recommender()

    # Ajout de films
    movie_manager.add_movie("The Matrix", "Sci-Fi")
    movie_manager.add_movie("Inception", "Sci-Fi")
    
    # Ajout d'évaluations
    user_manager.add_rating(1, 1, 5.0)
    user_manager.add_rating(1, 2, 4.5)

    # Recommandation de films
    recommendations = recommender.recommend_movies(1)
    print(f"Recommendations for user 1: {recommendations}")

if __name__ == "__main__":
    main()

