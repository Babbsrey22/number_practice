# Prog09: Create a program that print all the even numbers
# Starting from 0 to 100 (Use for loop)

even_numbers = []

# Append even numbers 0-100
for num in range(0, 101):
    if num % 2 == 0:
        even_numbers.append(num)

# Print list
print(even_numbers)