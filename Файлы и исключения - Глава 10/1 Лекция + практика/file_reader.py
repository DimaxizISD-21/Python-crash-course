#Чтение всего файла

# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)

####################################################
#Пути к файлам

# with open('folder/pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)

####################################################

# file = 'folder/pi_digits.txt'
# with open(file) as file:
#     contents = file.read()
#     print(contents)

####################################################
#Чтение по строкам

# filename = 'folder/pi_digits.txt'
#
# with open(filename) as file_object:
#     for line in file_object:
#         print(line)

####################################################
#Создание списка строк по содержимому файла

# filename = 'folder/pi_digits.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
#     for line in lines:
#         print(line.rstrip()) #rstrip() - удаляет пустые строки
