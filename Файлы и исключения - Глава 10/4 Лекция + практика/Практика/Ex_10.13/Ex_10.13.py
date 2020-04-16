#REMEMBER ME

import json

filename = 'user_asked.json'

try:
    with open(filename) as file:
        results = json.load(file)

except FileNotFoundError:
    name = input("\nКак вас зовут? ")
    ask = int(input(name.title() + ', какое ваше любимое число? '))
    with open(filename, 'w') as file:
        print('Спасибо вам, мы обработаем вашу информацию!')
        results = {}
        results['Name'] = name.title()
        results['Favorite_number'] = ask
        json.dump(results, file)

else:
    print(results['Name'] + ', ваше любимое число это: ' + str(results['Favorite_number']))