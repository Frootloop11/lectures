def main():
    first_names = ["A", "B", "C", "D"]
    numbers = [3, 1, 0, 2]
    print(find_oldest_name(first_names, numbers))


def find_oldest_name(names, ages):
    if not ages:
        return None
    index_of_oldest = 0
    age_of_oldest = ages[0] #TODO reconsider
    for i, age in enumerate(ages[1:], 1):
        if age > age_of_oldest:
            index_of_oldest = i
            age_of_oldest = age
    return names[index_of_oldest]


if __name__ == '__main__':
    main()
