#question 1

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

sum_result = number1 + number2

print("The sum of {} and {} is {}".format(number1, number2, sum_result))

#question 2

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number {} is even.".format(number))
else:
    print("The number {} is odd.".format(number))
    #Ques 3
 
number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("The factorial of {} is {}".format(number, factorial))
#ques 4
