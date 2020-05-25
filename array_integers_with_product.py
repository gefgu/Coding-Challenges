"""Given an array of integers,
return a new array such that each element at index i of the new array is the
product of all the numbers in the original array except the one at i."""
"""BONUS: Don't use division"""
from operator import mul
from functools import reduce


def array_integers_with_product(list_values):
    return [reduce(mul, list(list_values[:index] + list_values[index+1:])) for index in range(len(list_values))]


assert array_integers_with_product([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert array_integers_with_product([3, 2, 1]) == [2, 3, 6]
