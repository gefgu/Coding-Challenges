"""Given a list of numbers and a number k, return whether any two numbers from the list add up to k."""
"""Bonus: Do it in one pass"""

def list_and_sum_results_k(list_of_values, k_value):
    """Iterate through the list_of_values and if k_value-value is in the list_of_values return True"""

    for value in list_of_values:
        if (k_value-value) in list_of_values:
            return True
    return False


assert list_and_sum_results_k([10, 15, 3, 7], 17) == True
assert list_and_sum_results_k([10, 15, 3, 7], 39) == False
assert list_and_sum_results_k([50, 17, 33, 73, 123], 50) == True
assert list_and_sum_results_k([50, 17, 33, 73], 123) == True
assert list_and_sum_results_k([50, 17], 68) == False
