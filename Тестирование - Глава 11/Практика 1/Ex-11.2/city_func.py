def value_country(name, city, population=''):
    if population:
        full_value = name + ', ' + city + ', ' + 'population: ' + str(population)
    else:
        full_value = name + ', ' + city
    return full_value.title() 
