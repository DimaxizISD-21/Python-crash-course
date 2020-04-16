try:
    number_one = int(input('Введите первое число: '))
    number_two = int(input('Введите второе число: '))
    
    result = number_one + number_two
    print('Результат: ' + str(result))

except ValueError:
    print('Недопустимое значение...')
