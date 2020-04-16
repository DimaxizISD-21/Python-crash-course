import json

filename = 'user_asked.json'

name = input("\nКак вас зовут? ")
# moon = input('How your moon? : ')
ask = int(input(name.title() + ', какое ваше любимое число? '))

with open(filename, 'w') as file:
    # file.write('Name: ' + name.title() + '\nFavorite number: ')
    json.dump(ask, file)
    # file.write('\nCurrent moon: ' + moon)

with open(filename) as file:
    result = json.load(file)
    print(name.title() + ', ваше любимое число это: ' + str(result))