#prog5_remaindertwonum

class Remainder:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def input_numbers(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))

    def get_remainder(self):
        self.remainder = self.num1 % self.num2
        print(self.remainder)


remainder = Remainder()
remainder.input_numbers()
remainder.get_remainder()