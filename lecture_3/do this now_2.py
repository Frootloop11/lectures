# def count_letters(string):
#     """Count the letters in string"""
#     count = 0
#     for character in string:
#         if character.isalpha():
#             count += 1
#         return count
#
#     print(count_letters('ABC 12'))


def is_adult(age):
    if age >= 18:
        return True
    else:
        return False


age = int(input("Age: "))
print("Adult" if is_adult(age) else "child")


ages = [1, 34, 0]
number_of_children = 0
for age in ages:
    if not is_adult(age):
        number_of_children += 1
print("There are {} kids".format(number_of_children))


# result = determine_adulthood(age)
# if result == "Adult":
#     print("Adulters")

