##################  Построение простого графика  ##################

import matplotlib.pyplot as plt

# squares = [1, 4, 9, 16, 25]
# plt.plot(squares)
# plt.show()

##################  Изменения типа надписей и толшины графика  ##################

# squares = [1, 4, 9, 16, 25]
# plt.plot(squares, linewidth=5)

## Назначение заголовка диаграммы и меток осей.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)

## Назначение размера шрифта делений на осях.
# plt.tick_params(axis='both', labelsize=14)

# plt.show()

##################  Корректировка графика  ##################

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.plot(input_values, squares, linewidth=5)

# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# plt.tick_params(axis='both', labelsize=14)

# plt.show()

##################  Нанесение и оформление отдельных точек функцией scatter()  ##################

# plt.scatter(2, 4, s=200)

# # Назначение заголовка диаграммы и меток осей.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # Назначение размера шрифта делений на осях.
# plt.tick_params(axis='both', which='major', labelsize=14)

# plt.show()

##################  Вывод серии точек функцией scatter()  ##################

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# plt.scatter(x_values, y_values, s=100)

# # Назначение заголовка диаграммы и меток осей.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # Назначение размера шрифта делений на осях.
# plt.tick_params(axis='both', which='major', labelsize=14)

# plt.show()

##################  Автоматическое вычисление данных  ##################

# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, s=40)

# # Назначение заголовка диаграммы и меток осей.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # Назначение размера шрифта делений на осях.
# plt.tick_params(axis='both', which='major', labelsize=14)

# # Назначение диапазона для каждой оси.
# plt.axis([0, 1100, 0, 1100000])
# plt.show()

##################  Удаление контуров точек  ##################

# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, edgecolors='none', s=40)

# # Назначение заголовка диаграммы и меток осей.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # Назначение размера шрифта делений на осях.
# plt.tick_params(axis='both', which='major', labelsize=14)

# # Назначение диапазона для каждой оси.
# plt.axis([0, 1100, 0, 1100000])
# plt.show()

##################  Определение пользовательских цветов  ##################

# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40) # c=(0, 0, 0.8)

# # Назначение заголовка диаграммы и меток осей.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # Назначение размера шрифта делений на осях.
# plt.tick_params(axis='both', which='major', labelsize=14)

# # Назначение диапазона для каждой оси.
# plt.axis([0, 1100, 0, 1100000])
# plt.show()

##################  Цветовые карты  ##################

# x_values = list(range(1001))
# y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, 
#     edgecolors='none', s=40)

# # Назначение заголовка диаграммы и меток осей.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # Назначение размера шрифта делений на осях.
# plt.tick_params(axis='both', which='major', labelsize=14)

# # Назначение диапазона для каждой оси.
# plt.axis([0, 1100, 0, 1100000])
# plt.show()

##################  Автоматическое сохранение диаграмм  ##################

# x_values = list(range(1001))
# y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, 
#     edgecolors='none', s=40)

# # Назначение заголовка диаграммы и меток осей.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # Назначение размера шрифта делений на осях.
# plt.tick_params(axis='both', which='major', labelsize=14)

# # Назначение диапазона для каждой оси.
# plt.axis([0, 1100, 0, 1100000])
# plt.savefig('squares_plot.png', bbox_inches='tight') # Замена plt.show()

##################  Упрражнения 15.1 - 15.2  ##################

# Упрражнения 15.1

###Построение 5 кубов

# x_values = [1, 2, 3, 4, 5]
# cubes = [1, 8, 27, 64, 125]

# plt.scatter(x_values, cubes, c='red', edgecolors='none', s=40)

# # Назначение заголовка диаграммы и меток осей.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # Назначение размера шрифта делений на осях.
# plt.tick_params(axis='both', which='major', labelsize=14)

# plt.show()

###Построение 5000 кубов

# x_values = list(range(5001))
# cubes = [x**3 for x in x_values]

# plt.scatter(x_values, cubes, c='red', edgecolors='none', s=40)

# # Назначение заголовка диаграммы и меток осей.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # Назначение размера шрифта делений на осях.
# plt.tick_params(axis='both', which='major', labelsize=14)

# # Назначение диапазона для каждой оси.
# plt.axis([0, 5100, 0, 5100**3])
# plt.show()

# Упрражнения 15.2

# x_values = list(range(5001))
# cubes = [x**3 for x in x_values]

# plt.scatter(x_values, cubes, c=cubes, cmap=plt.cm.Blues,
#     edgecolors='none', s=40)

# # Назначение заголовка диаграммы и меток осей.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # Назначение размера шрифта делений на осях.
# plt.tick_params(axis='both', which='major', labelsize=14)

# # Назначение диапазона для каждой оси.
# plt.axis([0, 5100, 0, 5100**3])
# plt.show()

##################  Случайное блуждание  ##################

#random_walk.py

from random import choice
# #Класс для генерирования случайных блужданий
# class RandomWalk():
#     def __init__(self, num_points=5000):
#         #Инициализирует атрибуты блуждания
#         self.num_points = num_points
#         # Все блуждания начинаются с точки (0, 0)
#         self.x_values = [0]
#         self.y_values = [0]

##################  Выбор направления  ##################        

# #random_walk.py

# class RandomWalk():
#     def __init__(self, num_points=5000):
#         #Инициализирует атрибуты блуждания
#         self.num_points = num_points
#         # Все блуждания начинаются с точки (0, 0)
#         self.x_values = [0]
#         self.y_values = [0]

#     def fill_walk(self):
#         #Вычисляет все точки блуждания
#         while len(self.x_values) < self.num_points:
#             # Определение направления и длины перемещения.
#             x_direction = choice([1, -1])
#             x_distance = choice([0, 1, 2, 3, 4])
#             x_step = x_direction * x_distance
            
#             y_direction = choice([1, -1])
#             y_distance = choice([0, 1, 2, 3, 4])
#             y_step = y_direction * y_distance

#             # Отклонение нулевых перемещений.
#             if x_step == 0 and y_step == 0:
#                 continue
            
#             # Вычисление следующих значений x и y.
#             next_x = self.x_values[-1] + x_step
#             next_y = self.y_values[-1] + y_step

#             self.x_values.append(next_x)
#             self.y_values.append(next_y)

##################  Вывод случайного блуждания  ##################  

# #rw_visual.py

# from random_walk import RandomWalk

# # Построение случайного блуждания и нанесение точек на диаграмму.
# rw = RandomWalk()
# rw.fill_walk()
# plt.scatter(rw.x_values, rw.y_values, s=15)
# plt.show()