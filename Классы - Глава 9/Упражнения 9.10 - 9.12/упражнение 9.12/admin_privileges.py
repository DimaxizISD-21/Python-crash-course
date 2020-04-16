class Privileges():
	def __init__(self, privileges=[]):
		self.privileges = privileges

	def show_privileges(self):
		if self.privileges:
			for privilege in self.privileges:
				print("- " + privilege)
		else:
			print("- У этого пользователя нету привилегий.")
