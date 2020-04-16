def print_models(unprinted_model, completed_models):
	while unprinted_model:
		current_model = unprinted_model.pop()
		print('Current printing: ' + current_model)
		completed_models.append(current_model)


def show_models(completed_models):
	print('\nComplite process: ')
	for completed_model in completed_models:
		print(completed_model)
