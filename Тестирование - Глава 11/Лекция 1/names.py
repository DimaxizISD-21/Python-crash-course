from name_func import get_formatted_name

print("Нажмите 'q' чтобы выйти из программы...")
while True:
    f_name = input("\nPlease give me a first name: ")
    if f_name == 'q':
        break
    l_name = input("Please give me a last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\tNeatly formatted name: " + formatted_name + '.')