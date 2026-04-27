class Card():
    def __init__(self, card_id, card_name, balance):
        self.card_id = card_id
        self.card_name = card_name
        self.balance = balance


    def boost_balance(self, amount):
        self.balance += abs(amount)


    def reduce_balance(self, amount):
        self.balance -= abs(amount)

