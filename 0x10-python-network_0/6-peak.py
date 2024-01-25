#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in the given list.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int: The peak element in the list.
    """

    # Check if the list is empty
    if list_of_integers is None or not list_of_integers:
        return None

    # Initialize variables for binary search
    low = 0
    high = len(list_of_integers)
    mid = (high - low) // 2 + low
    mid = int(mid)

    # Base cases for lists of size 1 and 2
    if high == 1:
        return list_of_integers[0]
    if high == 2:
        return max(list_of_integers)

    # Check if the middle element is a peak
    if (
        list_of_integers[mid] >= list_of_integers[mid - 1] and
        list_of_integers[mid] >= list_of_integers[mid + 1]
    ):
        return list_of_integers[mid]

    # Recursively search in the right half if the right neighbor is larger
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])

    # Recursively search in the left half if the left neighbor is larger
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
