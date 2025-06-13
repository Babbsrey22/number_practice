#prog9_evennum0-100

class FindEvenNum:
    def __init__(self):
        self.even_numbers = []

    def find_even_numbers(self):
        for num in range(0, 101):
            if num % 2 == 0:
                self.even_numbers.append(num)
        print(self.even_numbers)


even_num = FindEvenNum()
even_num.find_even_numbers()