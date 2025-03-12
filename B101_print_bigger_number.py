# Batch 1 Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
# Input 2 numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Print bigger number
if num1 > num2:
    print(f"{num1} is the bigger number.")
else:
    print(f"{num2} is the bigger number.")