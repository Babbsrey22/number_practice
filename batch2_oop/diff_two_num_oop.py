#prog3_difftwonums

class DiffTwoNumbers:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def input_numbers(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))

    def find_difference(self):
        if self.num1 > self.num2:
            self.diff = self.num1 - self.num2
        else:
            self.diff = self.num2 - self.num1
        print(self.diff)


difference = DiffTwoNumbers()
difference.input_numbers()
difference.find_difference()