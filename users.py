from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

users = {
    '1': User('1', 'DJWolfboi', 'admin123', 'admin'),
    '2': User('2', 'Noel', 'user1234', 'user')
}

def get_user_by_username(username):
    for user in users.values():
        if user.username == username:
            return user
    return None
