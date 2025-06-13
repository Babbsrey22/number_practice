#prog1_biggernumber

class BiggerNumber:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def input_numbers(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))

    def find_bigger_num(self):
        if self.num1 > self.num2:
            print(self.num1, "is the bigger number.")
        else:
            print(self.num2, "is the bigger number.")


bigger_number = BiggerNumber()
bigger_number.input_numbers()
bigger_number.find_bigger_num()