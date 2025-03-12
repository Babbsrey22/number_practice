# Prog01: Create a program that ask user to input 10 numbers, 
# Display all numbers that don't have duplicate 

num_list = []

# Input 10 numbers 
for num in range(0, 10):
    number = int(input(f"Enter number {num + 1}: "))
    num_list.append(number)

print(f"The numbers entered are {num_list}")

# Append numbers with no duplicate 
no_duplicates = []

for number in num_list:
    if num_list.count(number) == 1:
        no_duplicates.append(number)
        
print(f"The numbers with no duplicates are {no_duplicates}")