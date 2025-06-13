#prog10_numinbetween

class NumInBetween:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.in_between = []

    def input_numbers(self):
        self.num1 = int(input("Enter the first number: "))
        self.num2 = int(input("Enter the second number: "))

    def get_num_in_between(self):
        for num in range(self.num1 + 1, self.num2):
            self.in_between.append(num)
        print(self.in_between)


num_in_between = NumInBetween()
num_in_between.input_numbers()
num_in_between.get_num_in_between()