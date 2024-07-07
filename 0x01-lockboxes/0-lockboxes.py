#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes in the given list can be unlocked.

    Args:
        boxes (list): A list of lists representing the lockboxes.
        Each inner list contains the keys to other boxes.

    Returns:
        bool: True if all the boxes can be unlocked, False otherwise.
    """
    OpenedBoxesKeys = {0}
    queue = [0]
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < len(boxes) and key not in OpenedBoxesKeys:
                OpenedBoxesKeys.add(key)
                queue.append(key)
    return len(OpenedBoxesKeys) == len(boxes)
