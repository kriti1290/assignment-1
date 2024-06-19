
numbers_list = [10, 20, 5, 40, 15]

min_value = numbers_list[0]
max_value = numbers_list[0]

for number in numbers_list:
    if number < min_value:
        min_value = number
    if number > max_value:
        max_value = number

print(f"The minimum value in the list is: {min_value}")
print(f"The maximum value in the list is: {max_value}")
