#prog7_sum10num

class Sum10Numbers:
    def __init__(self):
        self.total = 0
        for self.num in range(0, 10):
            self.number = 0

    def input_numbers(self):
        for self.num in range (0, 10):
            self.number = float(input(f"Enter number {self.num + 1}: "))
            self.total += self.number
        print("Total sum:", self.total)


sum_numbers = Sum10Numbers()
sum_numbers.input_numbers()
