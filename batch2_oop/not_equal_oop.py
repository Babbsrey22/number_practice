#prog2_printnotequal

class NotEqualNum:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def input_numbers(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))

    def is_not_equal(self):
        if self.num1 != self.num2:
            print("Not Equal")
            pass


not_equal_num = NotEqualNum()
not_equal_num.input_numbers()
not_equal_num.is_not_equal()