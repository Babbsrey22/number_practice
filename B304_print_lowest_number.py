# Prog04: Create a program that ask user to input a number,
# Continue asking until the user input is invalid;
# Display the lowest number

# Input inifinte amount of numbers until ValueError
num_list = []

while True:
    try:
        number = int(input("Enter any number: "))
        num_list.append(number)
    except ValueError:
        print("Stopping number input...")
        print(num_list)
        lowest_num = min(num_list)
        print(f"The lowest number is {lowest_num}")
        break