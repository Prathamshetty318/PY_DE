import pandas as pd

#series 1d array
amount = pd.Series([1000,2000,3000,4000])

#print(amount)

#DataFrames 2d array

transactions = [
    { "transaction_id": "TXN001", "amount": 1500, "status": "SUCCESS", "mode": "UPI"},
    { "transaction_id": "TXN002", "amount": 2500, "status": "FAILED",  "mode": "POS"},
    { "transaction_id": "TXN003", "amount": 3500, "status": "SUCCESS", "mode": "UPI"}
]

transaction = {
    "tran_id" : [101,102,103,104],
    "amount" :[1000,2000,2000,3000],
    "status" : ["SUCCESS","FAILED","PENDING","SUCCESS"]
}


df = pd.DataFrame(transaction)

#print(df)

#inspecting datasets : rather than cleaning blindly we will 1st inspect the data 
'''
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())


print(df[["tran_id","amount"]]) #[] single brac one series double [] dataframe

'''

# filtering 
'''
successful = df[df["status"]=="SUCCESS"]
print(successful)

high_amount = df[df["amount"] > 2500]
print(high_amount)

'''

#multiple condition

result = df[(df["status"]=="SUCCESS") & (df["amount"] > 2000)]
print(result) 