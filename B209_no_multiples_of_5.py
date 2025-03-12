# Prog09: Create a program that print all the numbers,
# Starting from 0 to 100 except numbers ending in zero or ending five

num = 0
not_multiple_of_5 = []

# Append numbers 0-100 without multiples of 5 (while loop)
while num < 100:
    num += 1
    if num % 5 != 0:
        not_multiple_of_5.append(num)
# Print list