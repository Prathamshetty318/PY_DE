transactions=[
    {"tran_id" : "TXN001","amount" : 1500,"status" : "SUCCESS","mode" : "UPI"},
    {"tran_id" : "TXN002","amount" : 2500,"status" : "Failed","mode" : "Card"},
    {"tran_id" : "TXN003","amount" : 500,"status" : "PENDING","mode" : "UPI"},
    {"tran_id" : "TXN004","amount" : 25000,"status" : "SUCCESS","mode" : "Card"},
    {"tran_id" : "TXN005","amount" : 2000,"status" : "PENDING","mode" : "UPI"}   
]

def count_transactions(transactions):
    return len(transactions)

def calculate_total(transactions):  #totalamount
    total =0
    for transaction in transactions:
        total += transaction["amount"]
    
    return total

def filter_successful(transactions): #successfultransactions
    successful = []

    for transaction in transactions:
        if transaction["status"].upper() == "SUCCESS":
            successful.append(transaction)

    return successful        

def find_highest_transaction(transactions):
    return max(transactions, key=lambda x: x["amount"])

print ("Total Number of Transactions: ", count_transactions(transactions))
print ("Total Amount of Transactions: ", calculate_total(transactions))
print ("Successful Transactions: ", filter_successful(transactions))
print ("Highest Transaction: ", find_highest_transaction(transactions))
