#json = javascript object notation

import json 


'''
transactions = {
        "tran_id": "TXN101",
        "amount": 1000,
        "status": "successful"
    }

json_data = json.dumps(transactions, indent = 4) # dumps converts python object to json string 
print(json_data)

# this is called serialization 

'''

#create a json file
'''
with open("transaction.json","w") as file:
    json.dump(transactions,file,indent=4)  # dump writes json directly in a file
    '''

# read a json file

with open("transaction.json","r") as file:
    data = json.load(file)

print(data)
print(data["tran_id"])  # load reads data from json and convert it into a python obj 


'''
Function	Purpose
json.dump()	Python object → JSON file
json.dumps()	Python object → JSON string
json.load()	JSON file → Python object
json.loads()	JSON string → Python object
'''


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