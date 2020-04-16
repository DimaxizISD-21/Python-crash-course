#Упражнение 8.15

# import printing_functions

# unprinted_model = ['Samsung Galaxy S10', 'Xiaomi', 'Meizu']
# completed_models = []
# printing_functions.print_models(unprinted_model, completed_models) #unprinted_model[:] - делает копию списка
# printing_functions.show_models(completed_models)

###################################################################

#Упражнение 8.16

# from printing_functions import print_models

# unprinted_model = ['Samsung Galaxy S10', 'Xiaomi', 'Meizu']
# completed_models = []

# print_models(unprinted_model, completed_models)

###################################################################

# from printing_functions import print_models as pm

# unprinted_model = ['Samsung Galaxy S10', 'Xiaomi', 'Meizu']
# completed_models = []

# pm(unprinted_model, completed_models)

###################################################################

# import printing_functions as pf

# unprinted_model = ['Samsung Galaxy S10', 'Xiaomi', 'Meizu']
# completed_models = []

# pf.print_models(unprinted_model, completed_models) #unprinted_model[:] - делает копию списка
# pf.show_models(completed_models)

###################################################################

# from printing_functions import *

# unprinted_model = ['Samsung Galaxy S10', 'Xiaomi', 'Meizu']
# completed_models = []

# print_models(unprinted_model, completed_models) #unprinted_model[:] - делает копию списка
# show_models(completed_models)

###################################################################

#Упражнение 8.17

# name_magicans = ['Solderax', 'Alakozam', 'Robert Orion']

# def show_magicans(name_magicans):
# 	for name in name_magicans:
# 		print(name)

# show_magicans(name_magicans)

###################################################################

# def make_album(n_group, n_album, 
# 	track=''):
# 	artist = {
# 			'name_group': n_group,
# 			'name_album': n_album
# 		}

# 	if track:
# 		artist['tracks'] = track

# 	return artist

# while True:
# 	print("\nЗдравствуйте, вы попали в музыкальную студию Records!")
# 	print("Если вы хотите выйти из программы то введите 'exit'\n")
	
# 	try:
# 		n_group = input('Введите название группы: ')

# 		if n_group == 'exit':
# 			print("Вы вышли из программы...")
# 			break

# 		n_album = input('Введите название альбома: ')

# 		if n_album == 'exit':
# 			print("Вы вышли из программы...")
# 			break

# 		track = int(input('Введите количество песен в альбоме: '))

# 	except ValueError:
# 		print('\nВы ввели неверное значение!')
# 		print("Попробуйте ещё раз")
# 		continue

# 	except KeyboardInterrupt:
# 		print("\nВы вышли из программы...")
# 		break

# 	formated = make_album(n_group, n_album, track)
# 	print(formated)

###################################################################

# def city_country(city, country):
# 	formated = city + ", " + country
	
# 	return formated.title()

# inputed = city_country('vasylkiv', 'ukraine')
# print(inputed)

# inputed = city_country('paris', 'france')
# print(inputed)

# inputed = city_country('new york', 'usa')
# print(inputed)