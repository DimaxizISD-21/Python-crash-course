class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 15

	def describe_restaurant(self):
		print('Restaurant name: ' + self.restaurant_name)
		print('Cuisine type: ' + self.cuisine_type)

	def open_restaurant(self):
		print("Restaurant is opened!")

	def show_served(self):
		print('Served by visitors: ' + str(self.number_served) + ' peoples.')

	def set_number_served(self, served):
		self.number_served = served

	def increment_number_served(self, inc_number):
		self.number_served += inc_number