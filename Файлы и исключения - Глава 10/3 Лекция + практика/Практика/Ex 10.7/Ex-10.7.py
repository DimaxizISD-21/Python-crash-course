while True:
    try:
        number_one = int(input('\nВведите первое число: '))
        number_two = int(input('Введите второе число: '))
        
        result = number_one + number_two
        print('Результат: ' + str(result))

        print("\nЕсли хотите выйти нажмите Ctrl + C")
    except ValueError:
        print('Недопустимое значение...')
    
    except KeyboardInterrupt:
        print('\nВы вышли из программы...')
        break