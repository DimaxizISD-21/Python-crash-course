# import pizza #Импортирование всего модуля

# pizza.make_pizza(20, 'pepperoni')
# pizza.make_pizza(16, 'tomato', 'cheese', 'mushrooms', 'peppers')

#####################################################################

# from pizza import make_pizza #Импортирование конкретных функций

# make_pizza(20, 'pepperoni')
# make_pizza(16, 'tomato', 'cheese', 'mushrooms', 'peppers')

#####################################################################

# from pizza import make_pizza as mp #Назначение псевдонима для функции

# mp(20, 'pepperoni')
# mp(16, 'tomato', 'cheese', 'mushrooms', 'peppers')

#####################################################################

# import pizza as p #Назначение псевдонима для модуля

# p.make_pizza(20, 'pepperoni')
# p.make_pizza(16, 'tomato', 'cheese', 'mushrooms', 'peppers')

#####################################################################

from pizza import * #Импортирование всех функций модуля

make_pizza(20, 'pepperoni')
make_pizza(16, 'tomato', 'cheese', 'mushrooms', 'peppers')