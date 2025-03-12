# Batch 1 Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
sum = 0

# Input 10 numbers (for loop)
for num in range(0, 10):
    number = float(input(f"Enter number {num + 1}: "))
    sum += number

# Print sum
print(f"The sum of the ten numbers is {sum}")