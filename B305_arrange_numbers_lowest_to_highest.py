# Prog05: Create a program that ask user to input a number, 
# Continue asking until the user input is invalid; 
# Display the number from lowest to highest, 
# Clue: sort() function 

# Input infinite amount of numbers until ValueError 
num_list = []

while True:
    try:
        number = int(input("Enter any number: "))
        num_list.append(number)
    except ValueError:
        num_list.sort()
        print(num_list)
        break