from checking import Checker
from interface import InOut

class Inputs:

    #return number of tickets
    def number_of_tickets(num_of_tickets):
        num_of_tickets = Checker.check_num_input(num_of_tickets)
        if num_of_tickets:
            return num_of_tickets  
        else:
            return Inputs.number_of_tickets(InOut.ins("How many tickets do you want? Digit a number from 1 to 5, or 0 to exit: ") )          
  
    #return bet type
    def bet_type(bet_type):  
        bet_type = Checker.check_type(bet_type)
        if bet_type:
            return bet_type
        else:
            return Inputs.bet_type(InOut.ins("Enter a valid bet type: "))
    
    #return how many numbers the user want to play
    def how_many_numbers(num, bet_type):
        how_many = Checker.check_how_many_numbers(num, bet_type)
        if how_many:
            return how_many
        else:
            return Inputs.how_many_numbers(InOut.ins("How many numbers for your bet? "), bet_type)

    #return the 'ruota'
    def get_ruota(ruota):
        ruota = Checker.check_ruota(ruota)
        if ruota:
            return ruota
        else:
            return Inputs.get_ruota(InOut.ins("On wich 'ruota'? "))

    #return bet's amount
    def get_bet(bet):
        bet = Checker.check_bet(bet)
        if bet:
            return bet
        else:
            return Inputs.get_bet(InOut.ins("Enter a valid bet "))

