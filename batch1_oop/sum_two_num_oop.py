#prog3_sumtwonums

class SumTwoNumbers:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def input_numbers(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))

    def find_sum(self):
        self.sum = self.num1 + self.num2
        print(self.sum)


sum = SumTwoNumbers()
sum.input_numbers()
sum.find_sum()