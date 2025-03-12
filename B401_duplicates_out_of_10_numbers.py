# Prog01: Create a program that ask user to input 10 numbers,
# Display all numbers that have duplicate

num_list = []

# Input 10 numbers
for num in range(0, 10):
    number = int(input(f"Enter number {num + 1}: "))
    num_list.append(number)

print(f"The numbers input are {num_list}")

# Append duplicates
duplicates = []

for number in num_list:
    if number not in duplicates and num_list.count(number) > 1:
        duplicates.append(number)

print(f"The numbers that have duplicates are {duplicates}")