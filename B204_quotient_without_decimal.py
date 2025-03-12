# Prog04: Create a program that ask user to input 2 numbers,
# Print the quotient of the two numbers without the decimal point

# Input 2 numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Print quotient without decimal point
if num1 > num2:
    quotient = int(num1 / num2)
else:
    quotient = int(num2 / num1)
print(f"The quotient of {num1} and {num2}, without the decimal point, is {quotient}.")