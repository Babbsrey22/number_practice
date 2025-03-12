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
first_entry_only = []

for number in num_list:
    if number not in first_entry_only:
        first_entry_only.append(number)
            
# Print list
print(f"One entry of each number: {first_entry_only}")