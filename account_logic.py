class Account():
    def __init__(self, account_id, account_name):
        self.account_id = account_id
        self.name = account_name
        self.cards = []


    def return_balance(self):
        summ = 0
        try:
            for _ in self.cards:
                summ += _.balance
        except:  #нет конкретной ошибки. мб не  будет работать, хз
            pass
        return summ
