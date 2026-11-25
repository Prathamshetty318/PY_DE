import csv

#reading a file
'''
with open("Transaction_data.csv","r") as file: # reading file using csv reader 
    reader = csv.reader(file)

    for row in reader:
        print(row)

'''        
'''
with open("Transaction_data.csv","r",encoding = "utf-8-sig") as file: # reading file using csv DictReader
    reader = csv.DictReader(file)

    for row in reader:
        print(row["tran_id"])
        print(row["amount"])
        print(row["status"])


#write a csv file

successful_Transaction = [
    {"tran_id":"TXN101","amount":1000,"status":"successful"},
    {"tran_id":"TXN102","amount":2000,"status":"Failed"}
]

with open("successful_Transaction.csv","w", newline ="") as file:
    fieldnames = ["tran_id","amount","status"]

    writer = csv.DictWriter(file,fieldnames= fieldnames)

    writer.writeheader() # write the header to the file
    writer.writerows(successful_Transaction) # write the data to the file

'''
# DictWriter  creates a  csv wrieter that accespts dict 
# wrietheader write column names
# writerows write multiple rows of data to the file
# wruiterow write a single row of data to the file
# newline="" helps prevent unwanted blank lines, particularly on Windows.    


total = 0 
success = 0
failed = 0 
pending = 0 


successfultransaction = []

with open ("Transaction_data.csv","r" , encoding= "utf-8-sig" ) as file:
     reader = csv.DictReader(file)


     for row in reader :

            total += float(row["amount"]) 

            if row["status"].lower() == "success":
                success += 1
                successfultransaction.append(row)

            elif row["status"].lower() == "failed":
                 failed += 1

            elif row["status"].lower() == "pending":
                 pending =+ 1

print("total transaction ", total)
print("success count", success)
print("failed count", failed)
print("pending count", pending)

with open("successfultransaction.csv","w",newline = "") as file:

    fieldnames = ["tran_id","amount","status","mode"]

    writer = csv.DictWriter(file, fieldnames = fieldnames)

    writer.writeheader()
    writer.writerows(successfultransaction)

print("successfultransactions saved ")


          




