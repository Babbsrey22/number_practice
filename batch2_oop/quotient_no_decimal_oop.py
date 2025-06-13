#prog4_quotientnodecimal

class QuotientNoDecimal:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def input_numbers(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))

    def find_quotient(self):
        if self.num1 > self.num2:
            self.quotient = self.num1 / self.num2
        else:
            self.quotient = self.num2 / self.num1
        print(f"The quotient of {self.num1} and {self.num2}, without the decimal point, is {self.quotient:.0f}.")


quotient = QuotientNoDecimal()
quotient.input_numbers()
quotient.find_quotient()