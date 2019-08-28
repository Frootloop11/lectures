
name_to_age = {'Bill': 21, 'Jane': 4, 'Jack': 56, 'Thomas': 19}

get_name = input("Enter a name:")
get_age = int(input("Enter an age:"))

name_to_age[get_name] = get_age

for name, age in name_to_age.items():
    print("{:6} - {:2}".format(name, age))
