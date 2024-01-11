#!/usr/bin/python3
'''Determine if all the boxes can be opened'''


def canUnlockAll(boxes):
    '''Check if all boxes can be unlocked'''
    size = len(boxes)
    unlocked = [False] * size
    unlocked[0] = True

    for i in range(size):
        if unlocked[i]:
            for key in boxes[i]:
                if 0 <= key < size:
                    unlocked[key] = True
                    for sub_key in boxes[key]:
                        if 0 <= sub_key < size:
                            unlocked[sub_key] = True
        if len(boxes[i]) == 0:
            unlocked[i] = True,

    return all(unlocked)

# boxes = [[1], [2], [3], [4], []]
# print(canUnlockAll(boxes)) # -> True

# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes)) # -> True

# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes)) # -> False
