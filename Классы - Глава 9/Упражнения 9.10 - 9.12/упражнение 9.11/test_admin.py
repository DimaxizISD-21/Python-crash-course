from admin import Admin, Privileges, User

admin = Admin('Admin', 'Nikolaenko')

print()

admin.describe_user()
# admin.privileges = ['Admin']
admin.privileges.show_privileges()

print('\nДобавление привилегий...\n')
admin_privilege = [
	'разрешено удалять пользователей', 
	'разрешено банить пользователей', 
	'разрешено добавлять сообщения'
]

admin.privileges.privileges = admin_privilege
admin.privileges.show_privileges()