import unittest
from movie import MovieManager
from user import UserManager

class TestMovieManager(unittest.TestCase):
    def test_add_movie(self):
        movie_manager = MovieManager()
        movie_manager.add_movie("Test Movie", "Test Genre")
        movie = movie_manager.get_movie(1)
        self.assertEqual(movie.title, "Test Movie")

class TestUserManager(unittest.TestCase):
    def test_add_rating(self):
        user_manager = UserManager()
        user_manager.add_rating(1, 1, 5.0)
        ratings = user_manager.get_user_ratings(1)
        self.assertEqual(len(ratings), 1)
        self.assertEqual(ratings[0].rating, 5.0)

if __name__ == '__main__':
    unittest.main()
