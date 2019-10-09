"""
Take in a file
Find and return the longest line in that file
print the line number and length character
"""


def main():
    line_number, length = find_longest_line("warm_up.py")
    print(line_number, length)


def find_longest_line(file_name):
    max_line_number, max_length = -1, 0
    with open(file_name, 'r') as in_file:
        for i, line in enumerate(in_file, 1):   # enumerate starts the file at 1
            if len(line) > max_length:
                max_length = len(line)
                max_line_number = i
    return max_line_number, max_length


main()
