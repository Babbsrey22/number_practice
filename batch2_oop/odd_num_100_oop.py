#prog8_oddnum0-100

class FindOddNum:
    def __init__(self):
        self.odd_numbers = []

    def find_odd_numbers(self):
        for num in range(0, 101):
            if num % 2 != 0:
                self.odd_numbers.append(num)
        print(self.odd_numbers)


odd_num = FindOddNum()
odd_num.find_odd_numbers()