#!/usr/bin/python3
'''
Minimum number of copy all and paste operations required to result in
exactly n H characters in the file
'''
# from typing import Tuple


def copy_all(i, text):
    '''Return a copy of the text file'''
    # print(' > copy all', end='')
    return (i + 1, text)


def paste(i, text, copy):
    '''Append the copy string into the text file'''
    # print(' > past > ', end='')
    text += copy
    # print(f' {text} ', end='')
    return (i + 1, text)


def minOperations(n):
    '''
    Return the minimum number of copy all and paste operations to create a text
    file of n 'H' characters.

    Args:
    n (int): The number of 'H' characters to create in the text.

    Returns:
    int: The minimum number of copy all and paste operations required to create
    a text file with n 'H' characters. if n is impossible to achieve 0 isreturn
    '''
    text: str = 'H'
    copy: str = ''
    i: int = 0
    while len(text) <= n:
        if len(text) == n:
            return i

        if len(text) == 1:
            # print('H', end='')
            i, copy = copy_all(i, text)
            i, text = paste(i, text, copy)
            if len(text) == n:
                # print('\n')
                return i

        if n % len(text) == 0:
            i, copy = copy_all(i, text)
            while True:
                i, text = paste(i, text, copy)
                if len(text) == n:
                    # print('\n')
                    return i
                if n % len(text) == 0:
                    i, copy = copy_all(i, text)

        else:
            i, text = paste(i, text, copy)
            if len(text) == n:
                # print('\n')
                return i
    return 0


# n = 0
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# # -> Min # of operations to reach 0 char: 0

# n = 1
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# # -> Min # of operations to reach 1 char: 1

# n = 2
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# # -> Min # of operations to reach 2 char: 2

# n = 4
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# # -> Min # of operations to reach 4 char: 4

# n = 9
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# # -> Min # of operations to reach 9 char: 6

# n = 12
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# # -> Min # of operations to reach 12 char: 7
