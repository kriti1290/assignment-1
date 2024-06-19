
numbers_list = [1, 2, 3, 2, 4, 2, 5, 2]
element_to_count = 2

count = 0
for item in numbers_list:
    if item == element_to_count:
        count += 1

print(f"The element {element_to_count} occurs {count} times in the list.")
