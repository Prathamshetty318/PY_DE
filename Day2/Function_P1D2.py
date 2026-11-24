'''
#funct and param and args 
transactions=[
    {"tran_id" : "TXN001","amount" : 1500,"status" : "SUCCESS","mode" : "UPI"},
    {"tran_id" : "TXN002","amount" : 2500,"status" : "Failed","mode" : "Card"},
    {"tran_id" : "TXN003","amount" : 500,"status" : "PENDING","mode" : "UPI"},
    {"tran_id" : "TXN004","amount" : 25000,"status" : "SUCCESS","mode" : "Card"},
    {"tran_id" : "TXN005","amount" : 2000,"status" : "PENDING","mode" : "UPI"}   
]


def calculate_total(transactions):

    total = 0
    for transaction in transactions:
        total += transaction["amount"]
    return total


total = calculate_total(transactions)

print (total)


# multiple param
def calculate_transaction_fee(amount,percentage):
    fee = (amount * percentage)/100
    return fee

result = calculate_transaction_fee(5000,2)
print(result)    


#default param
def calculate_fee(amount, percentage=2):
    return amount * percentage / 100

print(calculate_fee(5000))
print(calculate_fee(5000, 3))

'''


def add(a, b):
    return a + b

print (add(5, 10))  # Output: 15    