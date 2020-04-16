def count_words(filename):
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        print('Файл под номером ' + filename + ' не найден...')
    else:
        words = contents.split()
        num_words = len(words)
        print('Количечство символов в файле ' + filename + ' равно: ' + str(num_words))

filenames = [
    'alice.txt', 
    'Betty Gordon at Bramble Farm.txt', 
    'Peter Cooper by Rossiter W. Raymond.txt', 
    'Plates by William John Hardy.txt',
    'test_error.txt'
]

print('\nНа данный момент доступные такие файлы: ')
i = 0
for file in filenames:
    i += 1
    print(str(i) + '. ' + file)

filename = input('\nВведите номер файла: ')
if int(filename) == 1:
    filename = filenames[0]
elif int(filename) == 2:
    filename = filenames[1]
elif int(filename) == 3:
    filename = filenames[2]
elif int(filename) == 4:
    filename = filenames[3]

count_words(filename)