# SECRET_NUMBER = 6
# number = int(input("? "))
# while number != SECRET_NUMBER:
#    print("no")
#    number = int(input("? "))
# print("YAY! Correct")


# number_of_people = 0
# total = 0
# age = int(input("Age: "))
# while age >= 0:
#     total += age
#     number_of_people += 1
#     age = int(input("Age: "))
# # TODO: use Exceptions
# if number_of_people == 0:
#     print("Not defined")
# else:
#     average = total / number_of_people
#     print(average)

# name = "Thomas"
# for i in range(0, 130, 40):
#     print("{1:8} {0:3}".format(i, name[i:]))

name = "Thomas Bennett"
for i, character in enumerate(name):
    print("{:2} = {}".format(i, character))
