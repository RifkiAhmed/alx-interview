#!/usr/bin/python3
'''Determine if all the boxes can be opened'''


def canUnlockAll(boxes):
    '''Check if all boxes can be unlocked'''
    if not isinstance(boxes, list):
        return False

    size = len(boxes)
    if size <= 1:
        return True

    unlocked = [False] * size
    unlocked[0] = True

    for i in range(size):
        if unlocked[i]:
            for key in boxes[i]:
                if 1 <= key < size:
                    unlocked[key] = True
                if key < i and key != 0 and unlocked[key]:
                    for sub_key in boxes[key]:
                        if 1 <= sub_key < size:
                            unlocked[sub_key] = True
    return all(unlocked)

# boxes = [[1], [2], [3], [4], []]
# print(canUnlockAll(boxes)) # -> True

# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes)) # -> True

# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes)) # -> False
