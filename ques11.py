
def fibonacci_sequence(n):
 
    fibonacci_numbers = [0, 1]

    for i in range(2, n):
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)

    return fibonacci_numbers

n = int(input("Enter the number of Fibonacci numbers to generate: "))

fibonacci_numbers = fibonacci_sequence(n)

print("First", n, "numbers in Fibonacci sequence:", fibonacci_numbers)
