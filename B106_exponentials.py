# Batch 1 Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
# Input 2 numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Print exponential
exponential = num1 ** num2
print(f"{num1} raised to {num2} is {exponential}")