"""transaction = {
    "tran_id": "TXN001",
    "amount": "INVALID",
    "status": "SUCCESS"
}

try:
    amount = int(transaction["amount"])
    print (amount+100)

except ValueError:
    print("Invalid amount value. Please provide a valid integer.")

except TypeError:
    print("An error occurred while processing the amount.")

finally:
    print("Transaction processing completed.")"""

    
test_transactions = [
    {"tran_id": "TXN001", "amount": "1500"},
    {"tran_id": "TXN002", "amount": "-500"},
    {"tran_id": "TXN003", "amount": "INVALID"},
    {"tran_id": "TXN004", "amount": "0"}
]


def process_data(test_transaction):
    try:
        amount = int(test_transaction["amount"])
        

    except (ValueError, TypeError):
        return "Invalid Data"

    if amount <= 0:
        return "Invalid"
    else:
        return "Valid"


for test_transaction in test_transactions:
    result = process_data(test_transaction)
    print(test_transaction["tran_id"], result)