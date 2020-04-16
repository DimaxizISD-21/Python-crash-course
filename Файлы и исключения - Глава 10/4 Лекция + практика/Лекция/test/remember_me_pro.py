import json

filename = 'username.json'

try:
    with open(filename) as file:
        username = json.load(file)
except FileNotFoundError:
    username = input('Как тебя зовут? ')
    with open(filename, 'w') as file:
        json.dump(username, file)
        print('Мы запомнили ваше имя: ' + username + '!')
else:
    print('Добро пожаловать, ' + username + '!')