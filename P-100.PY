class Atm(object):
    def __init__(self, atm, pin,balance):
        self.atm = atm
        self.pin=pin
        self.balance = balance

    def balanceEnquiry(self):
        print("CHECKING BALANCE...")

    def CashWithdrawl(self):
        print('WITHDRAWLING GIVEN CASH AMOUNT.....')

jeff = Atm(30000296829,1596,10000)

print(jeff.atm)
    
