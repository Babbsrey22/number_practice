#prog8_oddnumoutof10

class FindOddNumbers:
    def __init__(self):
        self.odd_count = 0
        self.odd_numbers = []
    
    def odd_number_count(self):
        for num in range (0, 10):
            number = float(input(f"Enter number {num + 1}: "))
            if number % 2 != 0:
                self.odd_count += 1
                self.odd_numbers.append(number)
    
    def display_result(self):
        print(self.odd_numbers)
        print(f"Out of 10 numbers, {self.odd_count} are odd.")


odd_number = FindOddNumbers()
odd_number.odd_number_count()
odd_number.display_result()


