class User:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def describe_user(self):
		print('Fist name: ' + self.first_name)
		print('Last name: ' + self.last_name)

	def greet_user(self):
		print('Hello, ' + self.first_name)
		
user_1 = User('Олексій', 'Ніколаєнко')

print('First name: ' + user_1.first_name + 
	'\nLast name: ' + user_1.last_name)
user_1.greet_user()

class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = Privileges()

class Privileges():
	def __init__(self, privileges=[]):
		self.privileges = privileges

	def show_privileges(self):
		if self.privileges:
			for privilege in self.privileges:
				print("- " + privilege)
		else:
			print("- У этого пользователя нету привилегий.")

		# if 'Admin' in self.privileges:
		# 	print('\nЗдравствуй Админушка)' + 
		# 		'\nТебе доступны такие привилегии: ')
		# 	privilege = [
		# 	'  -разрешено удалять пользователей', 
		# 	'  -разрешено банить пользователей', 
		# 	'  -разрешено добавлять сообщения'
		# 	]

		# 	for privileg in privilege:
		# 		print(privileg)
		# elif 'User' in self.privileges:
		# 	print('\nЗдравствуй обычний юзер)))' + 
		# 		'\nТебе только можно писать письма на форуме...')

