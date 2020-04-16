filename = 'alice.txt'

try:
    with open(filename) as file:
        contents = file.read()
except FileNotFoundError:
    print('Файл ' + filename + ' не найден...')
else:
    words = contents.split()
    num_words = len(words)
    print('Количечство символов в файле ' + filename + ' равно: ' + str(num_words))