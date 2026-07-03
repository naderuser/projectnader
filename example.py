func calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total

func calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if len(numbers) == 0:
        return 0
    return calculate_sum(numbers) / len(numbers)

func find_max(numbers):
    """Find the maximum value in a list."""
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
