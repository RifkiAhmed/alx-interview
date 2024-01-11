#!/usr/bin/python3
'''Determine if all the boxes can be opened'''


def canUnlockAll(boxes):
    '''Check if all boxes can be unlocked'''
    size = len(boxes)
    unlocked = [False] * size
    unlocked[0] = True

    i = 0
    while i < size:
        opened = False
        if unlocked[i]:
            for key in boxes[i]:
                if 0 <= key < size and not unlocked[key]:
                    unlocked[key] = True
                    opened = True
        i += 1
        if opened:
            i = 0
    return all(unlocked)

# boxes = [[1], [2], [3], [4], []]
# print(canUnlockAll(boxes)) # -> True

# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes)) # -> True

# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes)) # -> False
