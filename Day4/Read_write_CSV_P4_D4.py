import pandas as pd
import numpy as np

'''df = pd.read_csv("Transaction_data.csv")

print(df.describe())

#df.to_csv("output_transaction.csv",index=False)  # index = false prevents pandas from writing the dataframe index as a column 

df = pd.read_csv(
    "Transaction_data.csv",
    usecols=["tran_id","amount"]
)

print(df)

'''

for chunck in pd.read_csv ("Larger_Transactions",chunksize=100000):
    print(chunck.shape)