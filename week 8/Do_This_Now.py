name_to_age = {"Bill": 21, "Jane": 34, "Sven": 56}

AGE_THRESHOLD = 35


def find_names_of_oldest():
    return [name for name, age in name_to_age.items() if age >= AGE_THRESHOLD]


print(find_names_of_oldest())
