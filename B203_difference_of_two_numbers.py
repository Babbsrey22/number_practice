# Prog03: Create a program that ask user to input 2 numbers,
# Print the difference of the two numbers

# Input 2 numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Print difference
if num1 > num2:
    difference = num1 - num2
else:
    difference = num2 - num1

print(f"The difference between {num1} and {num2} is {difference}")