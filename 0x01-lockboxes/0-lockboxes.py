#!/usr/bin/python3
""" lockBoxes"""


def canUnlockAll(boxes):
    """ checks if keys in lockbox can unlock other lockboxes
        that all will be unlocked """

    the_keys = set()
    length = len(boxes)
    opened_boxes = []
    i = 0

    while i < length:
        prev_i = i
        opened_boxes.append(i)
        the_keys.update(boxes[i])
        for key in the_keys:
            if key != 0 and key < length and key not in opened_boxes:
                i = key
                break
        if prev_i != i:
            continue
        else:
            break

    for i in range(length):
        if i not in opened_boxes and i != 0:
            return False
    return True
