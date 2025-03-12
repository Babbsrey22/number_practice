# Prog05: Create a program that ask user to input 2 numbers,
# Print the remainder when the first number is divided by the second number

# Input 2 numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Divide num1 by num2
remainder = num1 % num2

# Print result
print(f"The remainder of {num1} and {num2} is {remainder}")