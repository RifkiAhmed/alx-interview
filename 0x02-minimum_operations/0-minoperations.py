#!/usr/bin/python3
'''
Minimum number of copy all and paste operations required to result in
exactly n H characters in the file
'''


def copy_all(i, text):
    '''Return a copy of the text file'''
    # print(' > Copy All', end='')
    return (i + 1, text)


def paste(i, text, copy):
    '''Append the copy string into the text file'''
    # print(' > Past >', end='')
    text += copy
    # print(f' {text}', end='')
    return (i + 1, text)


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
    text = 'H'
    copy = ''
    i = 0

    # print('\nH', end='')
    while (len(text) < n):
        if n % len(text) == 0:
            i, copy = copy_all(i, text)
            i, text = paste(i, text, copy)
        else:
            i, text = paste(i, text, copy)
    # print()
    return i if len(text) == n else 0


# Examples
# test_values = [0, 1, 2, 4, 9, 12]
# for n in test_values:
#     operations = minOperations(n)
#     print("Min # of operations to reach {} char: {}".format(n, operations))
