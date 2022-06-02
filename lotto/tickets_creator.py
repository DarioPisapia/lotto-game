from inputs import Inputs
from interface import InOut
from ticket import Ticket
from checking import Checker

class Tickets_out: 
    
    #create tickets    
    def ticket_generator(num_of_tickets):
        list_of_tickets = []
        for n in range(num_of_tickets): 

            #takes informations for every ticket
            bet_type = Inputs.bet_type(InOut.ins("Enter bet type: "))
            how_many_numbers = Inputs.how_many_numbers(InOut.ins("How many numbers for your bet? "), bet_type)
            numbers = Ticket.get_numbers(how_many_numbers)
            ruota = Inputs.get_ruota(InOut.ins("On wich 'ruota'? "))
            bet = Inputs.get_bet(InOut.ins("How much for this ticket? "))

            #creates a ticket and appends it to a list of tickets
            t = Ticket(bet_type, numbers, ruota, bet)
            list_of_tickets.append(t)

        return list_of_tickets

    #print tickets
    def tickets_printer(list_of_tickets):          
        for ticket in list_of_tickets:       
            InOut.out(ticket)                        

    #winning tickets
    def winning_tickets(list_of_tickets, extracts):   
        to_win = {"Ambata": 1, "Ambo": 2, "Terno": 3, "Quaterna": 4, "Cinquina":5}
        winning_tickets = []
        for t in list_of_tickets:      
            ruota = t.ruota
            numbers = t.numbers
            b_type = t.b_type
            win = to_win[b_type]
            if Checker.check_win(ruota, numbers, win, extracts):
                winning_tickets.append(t)
        return winning_tickets  

