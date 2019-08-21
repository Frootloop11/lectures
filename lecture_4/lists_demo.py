subjects = ['CP1404', 'CP2406', 'CP1804']
#
# for subject in enumerate(subjects):
#     print(" - {}".format(subject))
#
# # for i in range(len(subjects)):
# #     print("{} - {}".format(i + 1, subjects[i]))


# scores = []
# score = int(input("Score: "))
# while score >= 0:
#     scores.append(score)
#     score = int(input("Score: "))
# print("Your highest score is", max(scores))

subjects.append("MA1000")
print(subjects)

# cp_subjects = []
# for subject in subjects:
#     if subject.startswith("CP"):
#         cp_subjects.append(subject)

count_cps = sum((1 for subject in subjects if subject.startswith("CP")))
print(count_cps)

cp_subjects = [subject for subject in subjects if subject.startswith("CP")]
print(cp_subjects)

year_numbers = [int(subject[2]) for subject in subjects if subject.startswith("CP")]
print(year_numbers)
