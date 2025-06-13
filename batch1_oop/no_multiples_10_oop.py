#prog10_notmultipleof10

class NoMultiples10:
    def __init__(self):
        self.not_multiple_10 = []

    def remove_multiples_of_10(self):
        for num in range(0, 101):
            if num % 10 != 0:
                self.not_multiple_10.append(num)
        print(self.not_multiple_10)


no_mutiples_10 = NoMultiples10()
no_mutiples_10.remove_multiples_of_10()