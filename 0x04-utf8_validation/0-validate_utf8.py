#!/usr/bin/python3
'''UTF-8 encoding validation'''


def validUTF8(data):
    '''Determines if data set represents a valid UTF-8 encoding
    '''

    i = 0
    while i < len(data):
        if (data[i] & 0x80) == 0x00:
            i += 1
        elif (data[i] & 0xE0) == 0xC0 and (i + 1) < len(data):
            if (data[i + 1] & 0xC0) != 0x80:
                return False
            i += 2
        elif (data[i] & 0xF0) == 0xE0 and (i + 2) < len(data):
            if any((data[i + j] & 0xC0) != 0x80 for j in range(1, 3)):
                return False
            i += 3
        elif (data[i] & 0xF8) == 0xF0 and (i + 3) < len(data):
            if any((data[i + j] & 0xC0) != 0x80 for j in range(1, 4)):
                return False
            i += 4
        else:
            return False

    return True
