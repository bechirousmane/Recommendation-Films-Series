from database import session, Rating

class UserManager:
    def add_rating(self, user_id, movie_id, rating):
        rating = Rating(user_id=user_id, movie_id=movie_id, rating=rating)
        session.add(rating)
        session.commit()

    def get_user_ratings(self, user_id):
        return session.query(Rating).filter(Rating.user_id == user_id).all()
