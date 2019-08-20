def main():
    print("guess a number between 1-10")

    SECRET = 5

    user_guess = int(input("? "))
    while user_guess != SECRET:
        print("Wrong! Guess again")
        user_guess = int(input("? "))
    print("You Got it!")


main()
