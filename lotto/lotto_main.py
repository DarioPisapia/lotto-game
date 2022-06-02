from interface import InOut
from tickets_creator import Tickets_out
from inputs import Inputs
from winning_time import WinningTime


if __name__ == "__main__": 
    InOut.ins("Welcome to the Lotto game! Press START ")

    num_of_tickets = Inputs.number_of_tickets(InOut.ins("How many tickets do you want? Digit a number from 1 to 5, or 0 to exit: "))
    
    if num_of_tickets == "See you the next time!":
        #exit game
        InOut.out(num_of_tickets)
    else:
        list_of_tickets = Tickets_out.ticket_generator(num_of_tickets)
        #print tickets
        InOut.out("\nYour tickets are:")
        Tickets_out.tickets_printer(list_of_tickets)

        #extracts numbers
        extracts = WinningTime.extractions() 

        #looking for winning tickets
        winning_tickets = Tickets_out.winning_tickets(list_of_tickets, extracts)
        if len(winning_tickets) > 0:
        #printing winning tickets and wins
            InOut.out("\nYour winning tickets are:")
            Tickets_out.tickets_printer(winning_tickets)

            gross_win = WinningTime.win_calculator(winning_tickets)
            net_win = float(gross_win) * 0.92
    
            InOut.out(WinningTime.wins_printer(gross_win, net_win))
        else:
            InOut.out("You win nothing this time, maybe the next time you will be more lucky!")
        
