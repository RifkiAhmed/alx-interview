#!/usr/bin/python3
'''
Minimum number of copy all and paste operations required to result in
exactly n H characters in the file
'''


def minOperations(n):
    '''
    Return the minimum number of copy all and paste operations to create
    a text file of n 'H' characters.

    Args:
    n (int): The number of 'H' characters to create in the text file.

    Returns: the minimum number of copy all and paste operations required
    to create a text file with n 'H' characters. if n is impossible to
    achieve 0 is returned.
    '''
    text = 1  # Numbre of 'H' characters in the text file
    copy = 1  # Copy of the file text
    operations = 0  # Numbre of Copy All and Past operations

    # print('\nH', end='')
    while (text < n):
        if n % text == 0:
            copy = text
            # print(' > Copy All', end='')
            text *= 2
            # print(f' > Past > {"".join(["H"] * text)}', end='')
            operations += 2
        else:
            text += copy
            # print(f' > Past > {"".join(["H"] * text)}', end='')
            operations += 1
    # print()
    return operations


# Examples
# test_values = [0, 1, 2, 4, 9, 12, 7842956142]
# for n in test_values:
#     operations = minOperations(n)
#     print("Min # of operations to reach {} char: {}".format(n, operations))
#
# Results
# Min # of operations to reach 0 char: 0
# Min # of operations to reach 1 char: 0
# Min # of operations to reach 2 char: 2
# Min # of operations to reach 4 char: 4
# Min # of operations to reach 9 char: 6
# Min # of operations to reach 12 char: 7
# Min # of operations to reach 7842956142 char: 28464
