class BankAccount:

    def __init__ (self,balance=1000):
        self.__balance =  balance

    def get_balance(self):
        return self.__balance    

    def deposit (self,amount):
        if amount > 0:
            self.__balance += amount

account = BankAccount(5000)

account.deposit(1000)

print(account.get_balance())

# Here, __balance uses name mangling to discourage direct access.