#prog7_evennumoutof10

class FindEvenNumbers:
    def __init__(self):
        self.even_count = 0
        self.even_numbers = []
    
    def even_number_count(self):
        for num in range (0, 10):
            number = float(input(f"Enter number {num + 1}: "))
            if number % 2 == 0:
                self.even_count += 1
                self.even_numbers.append(number)
    
    def display_result(self):
        print(self.even_numbers)
        print(f"Out of 10 numbers, {self.even_count} are even.")


even_number = FindEvenNumbers()
even_number.even_number_count()
even_number.display_result()