import numpy as np


#normla py calc
amounts = [100, 200, 300, 400]

doubled = []

for amount in amounts:
    doubled.append(amount*2)

print (doubled)    

 # we write loop in this to double the each val 

amounts = np.array([100,200,100,300,400,500])

doubled = amounts *2

#basic operation

print(doubled) # is called vectorized computation - performing operation accross arry with manually writing and using a standard loop 
print(amounts)
print(type(amounts))
print(amounts+100)
print(amounts*3)
print(amounts-200)

#aggregation

print(np.sum(amounts))
print(np.min(amounts))
print(np.max(amounts))
print(np.mean(amounts))
print(np.median(amounts))


#filtering

amounts = np.array([1000, 2500, 500, 4000, 1500])

#condition = amounts > 2000   # ture false numpy cretaes a boolean mark

#print(condition)

# to avoid boolean we apply that mask this is called boolean indexing amount(condition)
high_amt = amounts[amounts >= 2500]

print(high_amt)
