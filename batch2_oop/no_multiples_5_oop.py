#prog9_nomultiplesof5

class NoMultiples5:
    def __init__(self):
        self.not_multiple_5 = []
        self.num = 0

    def remove_multiples_of_5(self):
        while self.num < 100:
            self.num += 1
            if self.num % 5 != 0:
                self.not_multiple_5.append(self.num)
        print(self.not_multiple_5)


no_multiples_5 = NoMultiples5()
no_multiples_5.remove_multiples_of_5()