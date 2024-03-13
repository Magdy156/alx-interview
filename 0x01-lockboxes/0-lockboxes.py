#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Return True if all the boxes can be opened
    """
    keys = [0]  # 1st box is unlocked
    number_of_boxes = len(boxes)

    for key in keys:
        for boxItem in boxes[key]:
            """
            the 2nd condition for efficiency if we have box item
            greater than the index of the last item in the boxes
            """
            if boxItem not in keys and boxItem < number_of_boxes:
                keys.append(boxItem)
    if len(keys) == number_of_boxes:
        return True
    return False
