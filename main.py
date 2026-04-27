import json
from random import randint
from User_logic import User
from account_logic import Account
from cards_logic import Card

#создание нового id
def create_id():
    with open("id.txt", "r") as file:
        mem = file.read()
    new_id = str(randint(100000, 999999))
    while new_id in mem:
        new_id = str(randint(100000, 999999))
    return new_id


#красивый вывод
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
pink = '\033[35m'
white = '\033[37m'

red_back = '\033[41m'
green_back = '\033[42m'
yellow_back = '\033[43m'

end = '\033[0m'


#отделение команд
def is_logging(txt):
    if txt.startswith('\login ') and len(txt.replace(' ', '')) >= 7:
        return [True, txt.replace(' ', '').replace('\login', '')]
    else:
        return [False]


def find_login(login):
    with open('users.json', 'r') as file:
        data = json.load(file)
        if login in data:
            return True
        else:
            return False

#ОСНОВНАЯ ЛОГИКА
#вход в аккаунт:
message = ""
while message != 'exit':
    print(f'для входа в систему используйте комманду {green}\login [ваш логин]{end}')
    message = input()
    if is_logging(message)[0]:
        if find_login(is_logging(message)[1]):
            login = is_logging(message)[1]
            print(f'{green}такой пользователь существует{end}')
            with open('users.json', 'r') as file:
                data = json.load(file)
            while message != data[login]['password']:
                message = input('введите пароль: ')
                if message == '\exit':
                    break
            #функционал при входе в аккаунт
            if message == data[login]['password']:
                pass
        else:
            login = is_logging(message)[1]
            #регистрация
            print(f'{yellow}такого пользователя еще не существует{end}')
            print(f'{yellow}для регистрации придумайте пароль <:{end}')
            password = " "
            while " " in password:
                password = input('Введите пароль (без пробелов): ')
            with open('users.json', 'r') as file:
                data = json.load(file)
                data[login]['password'] = password
            with open('users.json', 'w') as file:
                json.dump(data, file)
             #функционал при входе
            pass

    else:
        print(f'{red}ошибка! попробуйте снова{end}')

def sucssesful_login(login):
    with open('users.json', 'r') as file:
        data = json.load(file)
