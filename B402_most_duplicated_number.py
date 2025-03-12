# Prog02: Create a program that ask user to input a number,
# Continue asking until the user input is invalid;
# Display the number with the most number of duplicate

# Input infinite amount of number until ValueError

num_list = []
duplicates = []

while True:
    try:
        number = int(input("Enter number: "))
        num_list.append(number)
    except ValueError:
        if num_list.count(number) > 1:
            duplicates.append(number)
        break

highest_num = max(duplicates)
print(f"The number with the most duplicates is {highest_num}")