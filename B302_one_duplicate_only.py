# Prog02: Create a program that ask user to input 10 numbers,
# Display all numbers,
# For numbers with duplicate, display only the first entry

num_list = []

# Input 10 numbers
for num in range(0, 10):
    number = int(input(f"Enter number {num + 1}: "))
    num_list.append(number)

print(f"The numbers entered are {num_list}")

# Append all numbers and those with one duplicate
duplicate = []
no_duplicate = []

for number in num_list:
    if num_list.count(number) == 1:
        no_duplicate.append(number)
    else:
        duplicate.append(number)

# Print list
print(no_duplicate, duplicate)