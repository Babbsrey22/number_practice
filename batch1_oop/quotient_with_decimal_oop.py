#prog5_quotientdecimal

class QuotientDecimal:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def input_numbers(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))

    def find_quotient(self):
        self.quotient = self.num1 / self.num2
        print(self.quotient)


quotient = QuotientDecimal()
quotient.input_numbers()
quotient.find_quotient()