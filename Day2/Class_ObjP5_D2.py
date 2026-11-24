class Transaction:

    def __init__(self, tran_id, amount, status, mode):
        self.tran_id = tran_id
        self.amount = amount
        self.status = status
        self.mode = mode

    def validate_transaction(self):
        try:
            amount = int(self.amount)
        except (ValueError, TypeError):
            print(f"{self.tran_id}: Invalid Data")

        else:    
            if amount <= 0:
                print(f"{self.tran_id}: Invalid")
            else:
                print(f"{self.tran_id}: Valid")

    def display_transaction(self):
        print(f"Transaction ID: {self.tran_id}")
        print(f"Amount: {self.amount}")
        print(f"Status: {self.status}")
        print(f"Mode: {self.mode}")


t1 = Transaction(101, 5000, "Success", "UPI")
t2 = Transaction(102, -1000, "Failed", "CARD")
t3 = Transaction(103, "abc", "Success", "UPI")

t1.display_transaction()
t1.validate_transaction()
t2.display_transaction()
t2.validate_transaction()
t3.display_transaction()
t3.validate_transaction()