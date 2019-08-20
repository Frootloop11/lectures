AGE_THRESHOLD = 18

"""Warm up for 01 - beginings
Write pseudocoade to ask the user for their age and
 tell them if they are an adult of child
 write python code
 """

"""
get age
if age > 18
    print adult
else
    print child
"""


age = int(input("Age: "))
if age >= 18:
    print("Adult")
else:
    print("Child")


def determine_adult(age):
    return age >= AGE_THRESHOLD
