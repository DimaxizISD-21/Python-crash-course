def get_formatted_name(f_name, l_name, middle=''):
    if middle:
        full_name = f_name + ' ' + l_name + ' ' + middle
    else:
        full_name = f_name + ' ' + l_name
    return full_name.title() 

# test = get_formatted_name('oleksiy', 'nikolaenko')
# print(test)