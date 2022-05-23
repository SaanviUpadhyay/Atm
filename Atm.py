class Atm(object) :
    def __init__(self , card_number , pin_number) :
        self.card_naumber=card_number
        self.pin_number=pin_number

    def cashwithdrawl(self):
        money=int(input("amount  : 2"))
        if money<100000 :
            print("Money Withdrawn")
        else :
            print("Insufficient Money")
            
    def balanceEnquiry(self):
        print("10000")

cstm1=Atm("10duv875ne","97660")
cstm1.cashwithdrawl()


        


    