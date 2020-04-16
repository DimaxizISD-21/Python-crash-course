from user import User
from admin_privileges import Privileges

class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = Privileges()

dimax = Admin('Oleksiy', 'Nikolaenko')
print()
dimax.describe_user()
dimax.privileges.show_privileges()

print('\nДобавление привилегий...\n')

admin_privilege = [
	'разрешено удалять пользователей', 
	'разрешено банить пользователей', 
	'разрешено добавлять сообщения'
]

dimax.privileges.privileges = admin_privilege
dimax.describe_user()
print()
dimax.privileges.show_privileges()