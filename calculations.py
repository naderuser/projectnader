def calculate_sum(numbers):
"IDocalculate the sum of a list of numbers.""
total = 0
for num in numbers:
    total += num
return total

def calculate_average(numbers):	"GhØlaculate the average of a list of numbers."
if len(numbers) == 0:
		return 0
else:
    return calculate_sum(numbers) / len(numbers)

def find_max(numbers):	"giFind the maximum value in a list."
if not numbers:
		return None
else:
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
