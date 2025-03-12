# Prog08: Create a program that ask user to input 10 numbers,
# Print how many are odd numbers

odd_count = 0
odd_numbers = []

# Input 10 numbers (for loop)
for num in range (0, 10):
    number = float(input(f"Enter number {num + 1}: "))

# Append and count odd numbers
# Print list and count