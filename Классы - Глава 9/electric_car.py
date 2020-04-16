from car import Car

class Battery:
	def __init__(self, battery_size = 70):
		#Инициализирует атрибуты аккумулятора.
		self.battery_size = battery_size

	def describe_battery(self):
		print('This car has ' + str(self.battery_size) + ' -kwh battery.')

	#########---Добавляем метод get_range---#########
	def get_range(self):
		#Выводит приблизительный запас хода для аккумулятора.
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		messsage = 'This car can go approximately ' + str(range)
		messsage += ' miles on a full charge. '
		print(messsage)


class ElectricCar(Car):
	#Представляет аспекты машины, специфические для электромобилей.
	def __init__(self, make, model, year):
		#Инициализирует атрибуты класса-родителя.
		#Затем инициализирует атрибуты, специфические для электромобиля.
		super().__init__(make, model, year)
		self.battery = Battery() #Принимает параметры класса Battery