# Prog01: Create a program that ask user to input 2 numbers,
# Print the smaller number

# Input 2 numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Print smaller number
if num1 < num2:
    print(f"{num1} is smaller than {num2}")
else:
    print(f"{num2} is smaller than {num1}")  