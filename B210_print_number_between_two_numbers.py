# Prog10: Create a program that ask user to input 2 numbers,
# Print all the numbers between the two numbers

# Input 2 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Print after num1 to before num2 (excluding both numbers)
in_between = []

for num in range(num1 + 1, num2):
    in_between.append(num)

print(in_between)