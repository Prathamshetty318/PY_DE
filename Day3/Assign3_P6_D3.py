import csv

valid_records = []
invalid_records = []

with open ("transaction_data.csv","r",encoding= "utf-8-sig") as file :
    reader = csv.DictReader(file)

    for row in reader:

        reason = ""
         #checked tran_id
        if not row["tran_id"].strip():
            reason = "missing transaction"

        #checked amount
        elif not row["amount"].strip():
            reason = "Missing Amount"

        else:
            try:
                row["amount"] = int(row["amount"])

                if row["amount"] < 0:
                    reason = "Negative amount"

            except ValueError:
                reason ="amount should be in integer"

        # checked ststus and amount
        if not reason and row["status"].strip().upper() not in [
            "SUCCESS", "FAILED", "PENDING"
            ]:
            reason = "Invalid transaction status"


        if reason:
            row["rejection_reason"] = reason
            invalid_records.append(row)

        else:
            valid_records.append(row)


with open("clean_transactions.csv","w",newline = "", encoding="utf-8-sig") as file :
    fieldnames = reader.fieldnames

    writer = csv.DictWriter(file,fieldnames= fieldnames)

    writer.writeheader()
    writer.writerows(valid_records)


with open("rejected_transactions.csv","w",newline = "", encoding="utf-8-sig") as file :
    fieldnames = reader.fieldnames + ["rejection_reason"]

    writer = csv.DictWriter(file,fieldnames= fieldnames)

    writer.writeheader()
    writer.writerows(invalid_records)    

print("----- PROCESSING SUMMARY -----")
print("Total records:", len(valid_records) + len(invalid_records))
print("Valid records:", len(valid_records))
print("Invalid records:", len(invalid_records))
print("Clean file created successfully!")
print("Rejected file created successfully!")

                

