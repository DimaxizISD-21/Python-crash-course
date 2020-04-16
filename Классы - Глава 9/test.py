#Импортирование одного класса

# from car import Car

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

#########################################################

#Хранение нескольких классов в модуле

# from car import ElectricCar

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

#########################################################

#Импортирование нескольких классов из модуля

# from car import Car, ElectricCar

# my_beetle = Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())

#########################################################

#Импортирование всего модуля

# from car import *

# my_beetle = Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())

#########################################################

#Импортирование модуля в модуль

########---my_car.py---########

# from car import Car
# from electric_car import ElectricCar

# my_beetle = Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())

########---electric_car.py---########

# from car import Car

# class Battery:
# 	def __init__(self, battery_size = 70):
# 		#Инициализирует атрибуты аккумулятора.
# 		self.battery_size = battery_size

# 	def describe_battery(self):
# 		print('This car has ' + str(self.battery_size) + ' -kwh battery.')

# 	#########---Добавляем метод get_range---#########
# 	def get_range(self):
# 		#Выводит приблизительный запас хода для аккумулятора.
# 		if self.battery_size == 70:
# 			range = 240
# 		elif self.battery_size == 85:
# 			range = 270

# 		messsage = 'This car can go approximately ' + str(range)
# 		messsage += ' miles on a full charge. '
# 		print(messsage)


# class ElectricCar(Car):
# 	#Представляет аспекты машины, специфические для электромобилей.
# 	def __init__(self, make, model, year):
# 		#Инициализирует атрибуты класса-родителя.
# 		#Затем инициализирует атрибуты, специфические для электромобиля.
# 		super().__init__(make, model, year)
# 		self.battery = Battery() #Принимает параметры класса Battery

########---car.py---########

# class Car:
# 	def __init__(self, make, model, year):
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer_reading = 0

# 	def get_descriptive_name(self):
# 		full_name = str(self.year) + ' ' + self.make + ' ' + self.model
# 		return full_name.title()

# 	def read_odometer(self):
# 		print('This car has ' + str(self.odometer_reading) + ' miles on it.')

# 	def update_odometer(self, mileage):
# 		if mileage >= self.odometer_reading:
# 			self.odometer_reading = mileage
# 		else:
# 			print('You can`t roll back an odometer!')

# 	def increment_odometer(self, miles):
# 		self.odometer_reading += miles


