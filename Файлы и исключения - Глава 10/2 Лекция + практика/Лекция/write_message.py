#Запись в пустой файл

active = True
while active:
	filename = 'programming.txt'
	with open(filename, 'w') as file:
		f_name = input('\nВведите ваше имя: ')
		l_name = input('Введите вашу фамилию: ')
		year = str(input('Сколько вам лет? : '))
		hobby = input('Ваше любимое хобби: ')

		file.write('Имя: ' + f_name)
		file.write('\nФамилия: ' + l_name)
		file.write('\nВозвраст: ' + year + ' лет')
		file.write('\nХобби: ' + hobby)

	print('\nВывод содержимого файла "programming.txt"\n')
	with open(filename) as file:
		for line in file:
			print(line.rstrip())

	exit = input('\nВы хотите выйти из программы? y/n: ')
	if exit == 'y':	
		print('Вы вышли из программы...')
		active = False
	else:
		active = True