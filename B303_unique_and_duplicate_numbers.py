# Prog03: Create a program that ask user to input a number,
# Continue asking until the user input is invalid;
# Display "Unique" after input when the inputted number don't have duplicate,
# Display "Duplicate" after input when the inputted number have duplicate

# Input infinite amount of numbers until ValueError

num_list = []

while True:
    number = (input("Enter any number: "))
    num_list.append(number)
    if num_list.count(number) == 1:
        print("Unique")
    else:
        print("Duplicate")
