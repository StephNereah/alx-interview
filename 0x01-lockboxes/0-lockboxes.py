#!/usr/bin/python3
"""
Module to solve the lockboxes problem.
"""


def canUnlockAll(lockboxes):
    """
    Determines if all the lockboxes can be unlocked.

    Each box contains keys to other boxes. The function checks whether it's
    possible to unlock all boxes starting from the first box (index 0).

    Args:
        lockboxes (list of list): A list where each index represents a box,
                                  and each element is a list of keys contained
                                  in that box.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    if not isinstance(lockboxes, list):
        return False
    if len(lockboxes) == 0:
        return False

    # Iterate through each box starting from the second (index 1).
    for box_id in range(1, len(lockboxes) - 1):
        is_unlocked = False

        # Check if the current box (box_id) can be unlocked
        for i in range(len(lockboxes)):
            # Check if the box_id is in the list of keys of the current box (i)
            # and make sure it's not the same box (i != box_id).
            if (box_id in lockboxes[i] and
                    i != box_id):
                is_unlocked = True
                break

        # If a box can't be unlocked, return False.
        if not is_unlocked:
            return False

    return True
