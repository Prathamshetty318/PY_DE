import pandas as pd
import numpy as np

data = {
    "tran_id": ["TXN001", "TXN002", "TXN003", "TXN004",
                "TXN004", None, "TXN007", "TXN008"],
    "amount": ["1500", "2500", None, "25000",
               "25000", "700", "INVALID", "-500"],
    "status": ["SUCCESS", "failed", "PENDING", "SUCCESS",
               "SUCCESS", "SUCCESS", "FAILED", "success"],
    "mode": ["UPI", "CARD", "UPI", "CARD",
             "CARD", "UPI", "CARD", None]
}

df = pd.DataFrame(data)
'''
print(df)

print(df.info())
print(df.isnull().sum())  # isnull identifies nll val as true and sum count the true val per column 
'''

# handling  missing vals 

'''
#OPT 1 drop rows with null vals 

cleandf = df.dropna()
print(cleandf)  # this removes the rows with any null vals dont use blindly
'''

'''
#OPT 2 fill missing vals 

df["mode"] = df["mode"].fillna("unknown")

df["amount"] = df["amount"].fillna(0)

print(df)

'''
'''
#OPT 3 drop missing vals only for criticl vals 

df = df.dropna(subset=["tran_id","amount"])

print(df)

'''

# detect duplicates 
'''
print(df.duplicated())

print(df.duplicated().sum())

df = df.drop_duplicates()

print(df)

'''

#Correct data types

'''
print(df["amount"].dtype)

df["amount"] = pd.to_numeric(df["amount"], errors="coerce") #coerce nvalid values such as "INVALID" become NaN instead of raising an exception.


print(df["amount"].dtype)

'''

#Normalize text
'''
#df["status"] = df["status"].str.upper()
df["status"] = df["status"].str.strip().str.upper() # strip removes xtra white spcases 

print(df)

'''

# grouping and aggregation
'''
df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0).astype("int64")
df["status"] = df["status"].str.strip().str.upper()

print (df.groupby("status")["amount"].sum())  # group by status and calc sum amount 

print(df.groupby("mode")["amount"].sum())

print(df.groupby("status")["amount"].agg(["count","max","min","mean"]))

print(df.groupby(["status","mode"])["amount"].sum())
'''

# sorting

'''
df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0).astype("int64")

print(df.sort_values("amount",ascending=False))

print(df.sort_values("amount",ascending=True))

'''
df = df.drop_duplicates()
df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0).astype("int64")

'''
df["is_high_val"] = df["amount"]>2000
df["bonus"] = df["amount"]*0.10
df["transaction_summary"] = np.where(
    df["amount"] >= 10000,
    "High_Val",
    "Normal"
)


print(df)

'''
