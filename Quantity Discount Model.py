import math

#Quantity Discount Model

print('This will calculate ONLY if your H is constant: ')

# calculates regular EOQ

print('What is your annual demand? ')
D = input()
             
print('What is your setup cost per order/order cost per order? ')
S = input()

print('What is your holding cost?' )
H = input()

#EOQ calculation
x = (float(D) * float(S)) * 2
z = x/float(H)
q = math.sqrt(z)
qStar = int(round(q))

print('Q* or the Economic Order Quantity is = ', str(qStar) )
print('Now look at this EOQ and look at which quantity pruchased it falls under, the price/unit is your P.')

print('What is your price/unit? ')
P = input()

print('Your Total Cost under the Quantity discount model is: ')
totalHoldingCost = (float(qStar)/2) * float(H)
totalSetupCost = (float(D)/qStar) * float(S)
priceDemand = (float(P) * float(D))

totalCost = (totalHoldingCost + totalSetupCost + priceDemand)

print(int(round(totalCost)))
             

             
                   
                   

             

             
