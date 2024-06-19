def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers_list = [10, 20, 30, 40, 50]
result = sum_of_numbers(numbers_list)
print(f"The sum of the numbers is: {result}")
