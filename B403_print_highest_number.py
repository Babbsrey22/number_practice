# Prog03: Create a program that ask user to input a number, 
# Continue asking until the user input is invalid;
# Display the highest number

# Input infinite amount of numbers until ValueError
num_list = []

while True:
    try:
        number = int(input("Enter any number: "))
        num_list.append(number)
    except ValueError:
        print("Stopping number input...")
        print(num_list)
        highest_num = max(num_list)
        print(f"The highest number is {highest_num}")
        break