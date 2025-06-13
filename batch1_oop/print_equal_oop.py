#prog2_printequal

class EqualNum:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def input_numbers(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))

    def is_equal(self):
        if self.num1 == self.num2:
            print("Equal")
            pass


equal_num = EqualNum()
equal_num.input_numbers()
equal_num.is_equal()