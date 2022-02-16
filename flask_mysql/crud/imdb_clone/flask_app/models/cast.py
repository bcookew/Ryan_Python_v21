from flask_app.config.mysqlconnection import connectToMySQL

class Cast:
    db = "actors_and_movies_schema"

    def __init__(self, data):
        self.id = data['id']

        self.movie_id = data['movie_id']
        self.title = data['title']
        self.release_date = data['release_date']

        self.actor_id = data['actor_id']
        self.name = data['name']
        self.role = data['role']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']