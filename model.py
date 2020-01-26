class User:
    def __init__(self, user_id, username, password):
       self.user_id = user_id
       self.username = username
       self.password = password

    def __repr__(self):
        return f'User(id={self.id})'
    def to_dict(self):
        return dict(user_id=self.user_id, username=self.username)

users = [User(1, 'user1', 'abcxyz'), User(1, 'user2', 'abcxyz')]
