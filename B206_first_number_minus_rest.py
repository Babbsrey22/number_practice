# Prog06: Create a program that ask user to input 10 numbers,
# Print the result of the first number minus all of the remaining numbers

all_numbers = []

# Input 10 numbers (for loop)
for num in range(0, 10):
    number = float(input(f"Enter number {num + 1}: "))
    all_numbers.append(number)

# First number minus sum of last 9
result = all_numbers[0]
for number in all_numbers[1:]:
    result -= number 

# Print result
print(result)