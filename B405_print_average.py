# Prog05: Create a program that ask user to input a number, 
# Continue asking until the user input is invalid;
# Display the average

# Input infinite amount of numbers until ValueError
num_list = []

while True:
    try:
        number = int(input("Enter any number: "))
        num_list.append(number)
    except ValueError:
        print("Stopping input...")
        break

# Print average 
count = len(num_list)
amount = sum(num_list)
average = amount / count
print(average)