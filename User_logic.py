#класс юзера

class User():
    def __init__(self, first_name, last_name, user_id, password, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.id = user_id
        self.password = password
        self.balance = balance


    def boost_balance(self, amount):
        self.balance += abs(amount)
        with open("logs.txt", "a") as logs:
            logs.write(f"{self.id} {self.first_name}  +{amount} на баланс")


    def reduce_balance(self, amount):
        self.balance -= abs(amount)
        with open("logs.txt", "a") as logs:
            logs.write(f"{self.id} {self.first_name}   -{amount} из баланса")


    def change_names(self, new_first_name, new_last_name):
        old_first_name = self.first_name
        old_last_name = self.last_name
        self.first_name = new_first_name
        self.last_name = new_last_name
        with open("logs.txt", "a") as logs:
            logs.write(f"пользователь {self.id} {old_first_name} {old_last_name} сменил имя на {self.first_name} {self.last_name}")


    def change_password(self, new_password):
        self.password = new_password


