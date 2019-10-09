"""
i = 5
file_05
"""


NUMBER_OF_FILE = 5
for i in range(NUMBER_OF_FILE):
    with open("file_{:02}".format(i), 'w'):
        pass


