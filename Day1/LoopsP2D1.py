'''amounts = [100, 200, 300, 400, 500]

for amount in amounts:
    print(amount)

total = 0

for amt in amounts:
    total = total + amt

print (total)
'''

amount_1 = [1000,2000,500,2500,5000,10000,100,250] 

#list comprising of transaction amounts traditional method
'''
large_amounts = []

for amt in amount_1:
    if amt > 1000:
        large_amounts.append(amt)

print(large_amounts)

'''

#list comprising of transaction amounts using list comprehension

large_amounts = [amt for amt in amount_1 if amt>1000]
print(large_amounts)