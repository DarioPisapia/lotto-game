#classe che gestisce l'input e l'output astraendo il più possibile

class InOut:
    #handle input
    def ins(x=""):
        return input(x)
    #handle output
    def out(x):
        return print(x)

