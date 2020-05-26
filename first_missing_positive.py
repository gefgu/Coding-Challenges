"""Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well."""


def find_missing_positive(array):
    i = 1 # TIME = O(1) Space = O(1)
    while True: # Worst Case: TIME = O(n) Space O(1)
        if i not in array:
            return i
        i += 1


assert find_missing_positive([3, 4, -1, 1]) == 2
assert find_missing_positive([1, 2]) == 3
