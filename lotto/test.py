
import unittest
from checking import Checker
from ticket import Ticket
from winning_time import WinningTime

class TestInputs(unittest.TestCase):

    def test_check_num_tickets(self):
        self.assertEqual(Checker.check_num_input("3"), 3)
        self.assertEqual(Checker.check_num_input(3), False)
        self.assertEqual(Checker.check_num_input("0"), "See you the next time!")
        self.assertEqual(Checker.check_num_input("6"), False)
        self.assertEqual(Checker.check_num_input("-1"), False)
        self.assertEqual(Checker.check_num_input("arw"), False)

    def test_bet_type(self):
        self.assertEqual(Checker.check_type("3"), False)
        self.assertEqual(Checker.check_type(3), False)
        self.assertEqual(Checker.check_type("Asmcke"), False)
        self.assertEqual(Checker.check_type("AmbO"), "Ambo")

    def test_how_many_numbers(self):
        self.assertEqual(Checker.check_how_many_numbers("3", "Ambo"), 3)
        self.assertEqual(Checker.check_how_many_numbers(3, 4), False)
        self.assertEqual(Checker.check_how_many_numbers("13", "Ambo"), False)
        self.assertEqual(Checker.check_how_many_numbers("1", "Ambo"), False)
        self.assertEqual(Checker.check_how_many_numbers("3", "Quaterna"), False)
        self.assertEqual(Checker.check_how_many_numbers("-3", "Ambo"), False)

    def test_ruota(self):
        self.assertEqual(Checker.check_ruota("312"), False)
        self.assertEqual(Checker.check_ruota(3), False)
        self.assertEqual(Checker.check_ruota("RoMa"), "Roma")
        self.assertEqual(Checker.check_ruota("ciccioli"), False)

    def test_numbers(self):
        #for checking the uniquity of numbers we can transform into set and it eliminats duplicates
        self.numbers = Ticket.get_numbers(10)
        self.incorrect = [3, 4, 5, 5, 6, 7, 8, 9, 10, 11]
        #check lenght
        self.assertEqual(len(Ticket.get_numbers(5)) == 5, True)
        self.assertEqual(len(Ticket.get_numbers(10)) == 10, True)
        self.assertEqual(len(Ticket.get_numbers(5)) == 6, False)
        self.assertEqual(len(Ticket.get_numbers(-5)) == 5, False)
        #check uniquity
        self.assertEqual(len(self.numbers), len(set(self.numbers)))
        self.assertNotEqual(len(self.incorrect), len(set(self.incorrect)))
      
    def test_printer(self):
        t = Ticket("Ambo", ["4", "7", "77"], "Roma", 3)
        self.assertEqual(Ticket.__str__(t) , "+---------------------------------------------------------------------------+\n"+f"|  Type     |  ---Ambo                          |           Lotto           |\n"+f"|  Numbers  |  ---4 7 77                        |  Makes Programmers Crazy  |\n"+f"|  Ruota    |  ---Roma                          |        Since 1983         |\n"+f"|  Bet      |   € 3                             |                           |\n"+"+---------------------------------------------------------------------------+")

    def test_exctraction(self):
        self.incorrect = [5, 5, 6, 7, 8]
        #check lenght
        for key in WinningTime.extractions():
            self.assertEqual(len(WinningTime.extractions()[key]), 5)
        #check uniquity
            self.assertEqual(len(WinningTime.extractions()[key]), len(set(WinningTime.extractions()[key])))
            self.assertNotEqual(len(WinningTime.extractions()[key]), len(set(self.incorrect)))

    def test_winners(self):
        self.exctracts = {"Roma": [7, 17, 27, 67, 77], "Tutte": [37, 47, 57, 87, 69]}
        self.assertEqual(Checker.check_win("Roma", [7, 34, 17, 66, 69], 2, self.exctracts), True)  
        self.assertEqual(Checker.check_win("Tutte", [7, 34, 17, 66, 69], 2, self.exctracts), True)
        self.assertEqual(Checker.check_win("Cagliari", [7, 34, 17, 66, 69], 2, self.exctracts), None)
        self.assertEqual(Checker.check_win("Roma", [7, 5, 6, 66, 69], 2, self.exctracts), None)

    def test_bet(self):
        self.assertEqual(Checker.check_bet("3.23"), 3.23)
        self.assertEqual(Checker.check_bet("3"), 3)
        self.assertEqual(Checker.check_bet("-3.23"), False)
        self.assertEqual(Checker.check_bet("3,23"), False)
        self.assertEqual(Checker.check_bet("3!23"), False)
        self.assertEqual(Checker.check_bet("a.23"), False)
        self.assertEqual(Checker.check_bet("cia"), False)
        self.assertEqual(Checker.check_bet("3.233"), False)
        self.assertEqual(Checker.check_bet(3.23), 3.23)
        self.assertEqual(Checker.check_bet(3), 3)

    def test_moneywin(self):
        t1 = Ticket("Ambo", ["4", "7", "77"], "Roma", 3)
        t2 = Ticket("Ambo", ["4", "7", "77"], "Tutte", 3)
        winning_tickets = [t1, t2]
        self.assertEqual(WinningTime.win_calculator(winning_tickets), "274.99")
        self.assertNotEqual(WinningTime.win_calculator(winning_tickets), 274.99)


if __name__ == "__main__":
    unittest.main()

