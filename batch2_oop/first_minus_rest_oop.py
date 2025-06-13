#prog6_firstminusrest

class FirstMinusRest:
    def __init__(self):
        self.all_numbers = []

    def input_numbers(self):
        for num in range(0, 10):
            number = float(input(f"Enter number {num + 1}: "))
            self.all_numbers.append(number)
    
    def get_result(self):
        self.result = self.all_numbers[0]
        for number in self.all_numbers[1:]:
            self.result -= number
        print(self.result)


first_minus_rest = FirstMinusRest()
first_minus_rest.input_numbers()
first_minus_rest.get_result()