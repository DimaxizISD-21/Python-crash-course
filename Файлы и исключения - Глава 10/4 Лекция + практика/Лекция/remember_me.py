import json

username = input('Как тебя зовут? ')

filename = 'username.json'

with open(filename, 'w') as file:
    json.dump(username, file)
    print('Мы запомнили ваше имя: ' + username + '!')