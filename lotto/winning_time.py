import random

class WinningTime:

    #does extractions 
    @staticmethod    
    def extractions():
        extracts = {
        "Bari": [], "Cagliari": [], "Firenze": [], "Genova": [], "Milano": [],       #potrebbe essere un dizionario di classi....ragionaci
        "Napoli": [], "Palermo": [], "Roma": [], "Torino": [], "Venezia": [], 
        }
        for key in extracts:
            while len(extracts[key]) < 5:
                number = random.randint(1, 90)
                if number not in extracts[key]:
                    extracts[key].append(number)
        
        return extracts

    #calculate total win
    def win_calculator(winning_tickets):
        total_gross = 0
        multiplier = {
            "Ambata": [11.23, 5.61, 3.74, 2.8, 2.24, 1.87, 1.60, 1.4, 1.24, 1.12], 
            "Ambo": [0, 250, 83.33, 41.66, 25, 16.66, 11.9, 8.92, 6.94, 5.55],
            "Terno": [0, 0, 4500, 1125, 450, 225, 128.57, 80.35, 53.57, 37.5],
            "Quaterna": [0, 0, 0, 120000, 24000, 8000, 3428.57, 1714.28, 952.38, 571.42], 
            "Cinquina":[0, 0, 0, 0, 6000000, 1000000, 285714.28, 107142.85, 47619.04, 23809.52]
        }
        for ticket in winning_tickets:
            win = float(ticket.bet) * multiplier[ticket.b_type][len(ticket.numbers) -1]
            if ticket.ruota == "Tutte":
                total_gross += win/10
            else:
                total_gross += win
        
        return f"{total_gross:.2f}"

    #print the ticket containing the total win
    def wins_printer(gross, net):
        gross = gross
        net = f"{net:.2f}"
        win_ticket = ""
        win_ticket += "+--------------------------- +\n"
        win_ticket += "|          You win!          |\n"
        win_ticket += f"|   Gross win = {(gross).ljust(9)}€   |\n"
        win_ticket += f"|   Net win   = {(net).ljust(9)}€   |\n"
        win_ticket += "+--------------------------- +"
        return win_ticket