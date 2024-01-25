#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int: The peak element in the list.
    """

    # Check if the list is empty
    if list_of_integers is None or list_of_integers == []:
        return None

    # Initialize variables for binary search
    srt = 0
    end = len(list_of_integers)
    index = ((end - srt) // 2) + srt
    index = int(index)

    # Base cases for lists of size 1 and 2
    if end == 1:
        return list_of_integers[0]
    if end == 2:
        return max(list_of_integers)

    # Check if the middle element is a peak
    if (
        list_of_integers[index] >= list_of_integers[index - 1] and
        list_of_integers[index] >= list_of_integers[index + 1]
    ):
        return list_of_integers[index]

    # Recursively search in the right half if the right neighbor is larger
    if index > 0 and list_of_integers[index] < list_of_integers[index + 1]:
        return find_peak(list_of_integers[index:])

    # Recursively search in the left half if the left neighbor is larger
    if index > 0 and list_of_integers[index] < list_of_integers[index - 1]:
        return find_peak(list_of_integers[:index])
