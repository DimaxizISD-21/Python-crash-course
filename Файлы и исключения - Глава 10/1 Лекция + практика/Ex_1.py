#Упражнения 10.1 - 10.2
#Упражнение 10.1

# filename = 'learning_python.txt'
#
# print('\n-----Чтение всего файла-----\n')
# with open(filename) as file:
#     content = file.read()
#     print(content)
#
# print('\n-----Чтение с перебором строк объекта файла-----\n')
# with open(filename) as file:
#     for line in file:
#         print(line.rstrip())
#
# print('\n-----Чтение с сохранением строк в списке с последующим выводом списка вне блока with-----\n')
# with open(filename) as file:
#     lines = file.readlines()
#
# for line in lines:
#     print(line.rstrip())

###############################################################################
#Упражнение 10.2

# filename = 'learning_python.txt'
#
# with open(filename) as f:
#     lines = f.readlines()
#
# print('\n---Вывод обычной строки файла---\n')
# for line in lines:
#     print(line.rstrip())
#
# print('\n---Замена Python на C---\n')
# for line in lines:
#     line = line.rstrip()
#     print(line.replace('Python', 'C'))
