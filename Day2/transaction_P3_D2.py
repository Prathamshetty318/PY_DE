transactions = [
    {"tran_id": "TXN001", "amount": 1500, "status": "SUCCESS", "mode": "UPI"},
    {"tran_id": "TXN002", "amount": 2500, "status": "FAILED", "mode": "CARD"},
    {"tran_id": "TXN003", "amount": 500, "status": "PENDING", "mode": "UPI"},
    {"tran_id": "TXN004", "amount": 25000, "status": "SUCCESS", "mode": "CARD"},
    {"tran_id": "TXN005", "amount": 2000, "status": "PENDING", "mode": "UPI"}
]

def count_transactions(transactions):
    return len(transactions)

def calculate_total_amount(transactions):
    total =0
    for transaction in transactions:
        total += transaction["amount"]

    return total

def calculate_successful_amount(transactions):
    total = 0

    for transaction in transactions:
        if transaction["status"].upper() == "SUCCESS":
            total += transaction["amount"]

    return total

def filter_by_status(transactions, status):
    filtered_tranactions = []

    for transaction in transactions:
        if transaction["status"].upper() == status.upper():
            filtered_tranactions.append(transaction)

    return filtered_tranactions

def find_highest_transaction(transactions):
    return max(transactions, key=lambda x: x["amount"])


def calculate_average(transactions):
    total_amount = calculate_total_amount(transactions)
    total_transactions = count_transactions(transactions)

    if total_transactions == 0:
        return 0

    return total_amount / total_transactions


print("Total Number of Transactions: ", count_transactions(transactions))
print("Total Amount of Transactions: ", calculate_total_amount(transactions))
print("Total Amount of Successful Transactions: ", calculate_successful_amount(transactions))
print("Pending Transactions: ", filter_by_status(transactions, "PENDING"))
print("Highest Transaction: ", find_highest_transaction(transactions))
print("Average Transaction Amount: ", calculate_average(transactions))

