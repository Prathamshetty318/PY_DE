# treal api conatins nestd josn in repsonses inmosy cases

transaction = {
    "tran_id": "TXN001",
    "amount": 1500,
    "customer": {
        "customer_id": 101,
        "name": "Rahul"
    },
    "payment": {
        "mode": "UPI",
        "status": "SUCCESS"
    }
}

print (transaction["customer"]["name"])
print(transaction["payment"]["mode"])