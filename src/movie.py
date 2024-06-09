from database import session, Movie

class MovieManager:
    def add_movie(self, title, genre):
        movie = Movie(title=title, genre=genre)
        session.add(movie)
        session.commit()

    def get_movie(self, movie_id):
        return session.query(Movie).filter(Movie.id == movie_id).first()

    def get_all_movies(self):
        return session.query(Movie).all()
