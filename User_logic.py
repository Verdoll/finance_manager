#класс юзера

class User():
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.accounts = []

    def change_password(self, new_password):
        if self.password != new_password:
            self.password = new_password


