filename = 'Dubliners by James Joyce.txt'

with open(filename, 'r') as file:
    content = file.read()
    word_input = input('\nВведите англ слово: ')
    word = content.count(word_input)
    print('Количество слова ' + word_input + ' равно: ' + str(word))
