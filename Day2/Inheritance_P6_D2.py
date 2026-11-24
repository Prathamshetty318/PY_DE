class Transaction:

    def __init__ (self, tran_id,amount):
        self.tran_id = tran_id
        self.amount = amount

    def display(self):
        print(self.tran_id, self.amount)

class UPITransaction(Transaction):

    def payment_method(self):
        print("Processing UPI Payment")

class CardTransaction(Transaction):

    def payment_method(self):
        print("Processing Card Payment")


upi = UPITransaction("TXN101",5000)
card = CardTransaction("TXN102",10000)

upi.display()
upi.payment_method()


card.display()
card.payment_method()