def show_names_animal(filename):
    try:
        with open(filename) as file:
            contents = file.read()
            print('\n' + contents)
    except FileNotFoundError:
        print('Файл под названием ' + filename + ' не найден...')

filenames = [
    'cats.txt', 
    'dogs.txt', 
]

print('\n-------Клички разных животных-------' + '\nНа данный момент доступные такие файлы: ')
for file in filenames:
    print(' -' + file)

while True:
    try:
        filename = input('\nНажмите Ctrl + C для выхода \nВведите название файла: ')
        show_names_animal(filename)
    except KeyboardInterrupt:
        print('\nВыход из программы...')
        break