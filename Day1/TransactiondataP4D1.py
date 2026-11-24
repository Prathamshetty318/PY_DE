transactions = [
    {
        "transaction_id": "TXN001",
        "amount": 1500,
        "status": "SUCCESS",
        "mode": "UPI"
    },
    {
        "transaction_id": "TXN002",
        "amount": 2500,
        "status": "FAILED",
        "mode": "POS"
    },
    {
        "transaction_id": "TXN003",
        "amount": 3500,
        "status": "SUCCESS",
        "mode": "UPI"
    }
]

print(transactions[0])

print (transactions[1]["amount"])