from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class User:
    def __init__( self, data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one_user(cls, data):
        query = """
            SELECT *
            FROM users
            WHERE id = %(user_id)s;
        """

        result = connectToMySQL( DATABASE ).query_db( query, data )
        current_user = cls( result[0] )
        return current_user