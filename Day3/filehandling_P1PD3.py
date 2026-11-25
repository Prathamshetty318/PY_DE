file = open("Transactions.txt","r")
data = file.readlines() # read , realline, readines
print(data)
file.close() # normal approach

with open("Transactions.txt","r") as file:  # manages file resource safely and closes file automatically
    data = file.read()
    print(data)

#write a file

report = "Daily Trasaction Report\n"
report += "------------------------\n"
report += "Total Transaction: 100\n"
report += "Total Amount: $5000\n"   # append data to file

with open ("Report.txt","w") as file: # replace w to a to append data to file or else the data changes will be overwritten  
    file.write(report)

  