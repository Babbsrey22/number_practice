# Prog02: Create a program that ask user to input a number,
# Continue asking until the user input is invalid;
# Display the number with the most number of duplicate

# Input infinite amount of number until ValueError

num_list = []
most_common_number = 0

while True:
    try:
        for num in range(0, 10):
            number = int(input(f"Enter number {num + 1}: "))
            num_list.append(number)
    except ValueError:
        break

print(f"The numbers input are {num_list}")
