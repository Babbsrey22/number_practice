# Prog01: Create a program that ask user to input 10 numbers, 
# Display all numbers that don't have duplicate 

num_list = []

# Input 10 numbers 
for num in range(0, 10):
    number = int(input(f"Enter number {num + 1}: "))
    num_list.append(number)

# Append numbers with no duplicate 

for num in num_list:
    if number.count(num) == 1:
        print(number)