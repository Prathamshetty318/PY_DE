transactions=[
    {"tran_id" : "TXN001","amount" : 1500,"status" : "SUCCESS","mode" : "UPI"},
    {"tran_id" : "TXN002","amount" : 2500,"status" : "Failed","mode" : "Card"},
    {"tran_id" : "TXN003","amount" : 500,"status" : "PENDING","mode" : "UPI"},
    {"tran_id" : "TXN004","amount" : 25000,"status" : "SUCCESS","mode" : "Card"},
    {"tran_id" : "TXN005","amount" : 2000,"status" : "PENDING","mode" : "UPI"}   
]

total_transactions = len(transactions)

successful_transactions = 0
failed_transactions = 0
successful_amount = 0
failed_amount = 0
total_amount = 0
payment_modes = set()
Pending_transactions = 0
goodamounttransctionid = []

for transaction in transactions:
    payment_modes.add(transaction["mode"])

    status = transaction["status"].upper()

    if  status == "SUCCESS":
        successful_transactions += 1
        successful_amount += transaction["amount"]

    elif status == "FAILED":
        failed_transactions += 1
        failed_amount += transaction["amount"]

    elif status == "PENDING":
        Pending_transactions += 1

    if status == "SUCCESS" or status == "FAILED":
        total_amount += transaction["amount"]

    if transaction["amount"]> 2000:
        goodamounttransctionid.append(transaction["tran_id"])

highest_amount = max(transaction["amount"] for transaction in transactions)
Lowest_amount = min(transaction["amount"] for transaction in transactions)
average_amount = total_amount / total_transactions

Successful_transactions_list = [transaction for transaction in transactions if transaction["status"].upper() == "SUCCESS"]

print("Total number of transactions:", total_transactions)
print("Number of successful transactions:", successful_transactions)
print("Number of failed transactions:", failed_transactions)
print("Total amount of successful transactions:", successful_amount)
print("Total amount of failed transactions:", failed_amount)
print("Payment modes used:", payment_modes)
print("Total amount of all transactions:", total_amount)
print("Number of pending transactions:", Pending_transactions)
print("Highest transaction amount:", highest_amount)
print("Lowest transaction amount:", Lowest_amount)
print("Average transaction amount:", average_amount)
print("Successful transactions:", Successful_transactions_list)
print("Transactions with amount greater than 2000 :", goodamounttransctionid)
