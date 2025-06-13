#prog4_prodtwonum

class ProductTwoNumbers:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def input_numbers(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))

    def find_product(self):
        self.product = self.num1 * self.num2
        print(self.product)


product = ProductTwoNumbers()
product.input_numbers()
product.find_product()