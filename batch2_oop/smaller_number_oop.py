#prog1_smallernumber

class SmallerNumber:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def input_numbers(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))

    def find_smaller_num(self):
        if self.num1 < self.num2:
            print(self.num1, "is the smaller number.")
        else:
            print(self.num2, "is the smaller number.")


smaller_number = SmallerNumber()
smaller_number.input_numbers()
smaller_number.find_smaller_num()