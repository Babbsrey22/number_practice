# Prog07: Create a program that ask user to input 10 numbers,
# Print how many are even numbers

even_count = 0
even_number = []

# Input 10 numbers (for loop)
for num in range(0, 100):
    number = float(input(f"Enter number {num + 1}: "))
    
# Append and count even numbers
# Print list and count