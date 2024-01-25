#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int: The peak element in the list.
    """

    if list_of_integers is None or list_of_integers == []:
        return None

    srt = 0
    end = len(list_of_integers)
    index = ((end - srt) // 2) + srt
    index = int(index)

    if end == 1:
        return list_of_integers[0]
    if end == 2:
        return max(list_of_integers)

    if (
        list_of_integers[index] >= list_of_integers[index - 1] and
        list_of_integers[index] >= list_of_integers[index + 1]
    ):
        return list_of_integers[index]

    if index > 0 and list_of_integers[index] < list_of_integers[index + 1]:
        return find_peak(list_of_integers[index:])

    if index > 0 and list_of_integers[index] < list_of_integers[index - 1]:
        return find_peak(list_of_integers[:index])
