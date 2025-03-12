# Prog10: Create a program that print all the numbers,
# Starting from 0 to 100 except numbers ending in zero

not_multiple_10 = []

# Append numbers 0-100 without multiples of 10
for num in range(0, 101):
    if num % 10 != 0:
        not_multiple_10.append(num)

# Print list
print(not_multiple_10)