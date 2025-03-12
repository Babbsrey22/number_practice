# Prog01: Create a program that ask user to input 10 numbers,
# Display all numbers that have duplicate

num_list = []
duplicates = []

# Input 10 numbers
for num in range(0, 10):
    number = float(input(f"Enter number {num + 1}: "))
    num_list.append(number)

# Append duplicates
for number in num_list:
    if num_list.count(number) != 1:
        duplicates.append(number)

print(duplicates)