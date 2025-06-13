#prog6_exponentials

class Exponential:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def input_numbers(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))

    def convert_exponential(self):
        self.exponential = self.num1 ** self.num2
        print(self.exponential)


exponential = Exponential()
exponential.input_numbers()
exponential.convert_exponential()