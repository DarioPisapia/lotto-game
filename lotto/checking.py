
class Checker:
 #check that the input for the number of tickets is correct
    def check_num_input(num):
        if type(num) == str:
            if num.isdigit() and type(num) == str :                             
                if int(num) < 0 or int(num) > 5:
                    return False
                else:
                    if int(num) == 0:
                        return "See you the next time!"
                    else:
                        return int(num)
            else:            
                return False
        else:
            return False

    #check bet type's input      
    def check_type(bet_type):
        if type(bet_type) ==  str:
            bet_types = ["Ambata", "Ambo", "Terno", "Quaterna", "Cinquina"]
            bet_type = bet_type.capitalize()
            if bet_type in bet_types:
                return bet_type
            else:
                return False
        else:
            return False

    #check that the numbers to play is enough
    def check_how_many_numbers(num, bet_type):
        bet_types = {"Ambata": 1, "Ambo": 2, "Terno": 3, "Quaterna": 4, "Cinquina":5}
        if type(num) == str and type(bet_type) == str:
            if num.isdigit():
                if int(num) < bet_types[bet_type] or int(num) > 10:
                    return False
                else:
                    return int(num)
            else:
                return False
        else:
            return False

    #check ruota's input.
    def check_ruota(ruota):
        if type(ruota) == str:
            ruote = ["Bari", "Cagliari", "Firenze", "Genova", "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia", "Tutte"]  
            ruota = ruota.capitalize()
            if ruota in ruote:
                return ruota
            else:
                return False
        else:
            return False
            
    #check if ticket is a winning one        
    def check_win(ruota, numbers, win, extracts):
        for key in extracts:
            ok_numbers = []
            for n in numbers:
                if int(n) in extracts[key]:
                    ok_numbers.append(n)
            if len(ok_numbers) >= win and ruota == "Tutte":
                return True
            if len(ok_numbers) >= win and ruota == key:
                return True

    #check if bet is in the correct format and has no more than 2 decimals
    def check_bet(bet):
        try:
            bet = float(bet)
            if (bet * 100) == int(bet * 100) and bet > 0:
                    return bet
            else:
                return False
        except ValueError:
            return False
