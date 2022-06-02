import random

class Ticket:
    def __init__(self, b_type, numbers, ruota, bet):
        self.b_type = b_type
        self.numbers= numbers
        self.ruota = ruota
        self.bet = bet

    def __str__(self):
        self.numbers.sort()
        num = " ".join(self.numbers)
        self.bet = str(self.bet)
        table = ""
        table += "+---------------------------------------------------------------------------+\n"
        table += f"|  Type     |  ---{(self.b_type).ljust(30)}|           Lotto           |\n"
        table += f"|  Numbers  |  ---{(num).ljust(30)}|  Makes Programmers Crazy  |\n"
        table += f"|  Ruota    |  ---{(self.ruota).ljust(30)}|        Since 1983         |\n"
        table += f"|  Bet      |   € {(self.bet).ljust(30)}|                           |\n"
        table += "+---------------------------------------------------------------------------+"
        return table

    #create the right amount of random numbers
    def get_numbers(nums):
        numbers = []
        while len(numbers) < nums:
            n = str(random.randint(1,90))
            if n not in numbers:
                numbers.append(n)
        return numbers
