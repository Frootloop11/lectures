def main():
    user_age = 0
    is_valid_input = False
    while not is_valid_input:
        try:
            user_age = int(input("age: "))
            if user_age < 0:
                print("Age must be greater then 0")
            else:
                is_valid_input = True

        except ValueError:
            print("Age must be valid number!")
    if is_even(user_age):
        print("{} is even".format(user_age))
    else:
        print("{} is odd".format(user_age))


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


main()


def test_is_even():
    for i in range(5):
        print("{} is {}".format(i, is_even(i)))
