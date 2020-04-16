filename = 'guest_book.txt'
with open(filename, 'a') as file:
    moon = input('Как ваше настроение? : ')
    file.write('\nТекущее настроение: ' + moon)


print('\nВывод содержимого файла "guest_book.txt"\n')
with open(filename) as file:
    for line in file:
        print(line.rstrip())
