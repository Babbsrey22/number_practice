# Prog08: Create a program that print all the odd numbers,
# Starting from 0 to 100

odd_numbers = []
odd_num = -1

# Append odd numbers 0-100 (while loop)
while odd_num < 99:
    odd_num += 2
    odd_numbers.append(odd_num)
    
# Print list