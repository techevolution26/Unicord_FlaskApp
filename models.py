class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password 

Users = [
    User(1, 'user1', 'password1'),
    User(2, 'user2', 'password2')
]        