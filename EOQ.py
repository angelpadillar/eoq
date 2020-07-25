import math

print("Economic Order Quantity 'EOQ' Calculator")
print('What is your annual demand? ')
D = input()

print('What is your setup cost per order/order cost per order? ')
S = input()

print('What is your holding cost?' )
H = input()

x = (float(D) * float(S)) * 2
z = x/float(H)

q = math.sqrt(z)

qStar = int(round(q))

print('Q* or the Economic Order Quantity is = ', str(qStar) )

avgInvLevel = (qStar/2)

print('The average inventory Level if using EOQ is ... ', avgInvLevel)

annualHoldingCost = (avgInvLevel * float(H))

print('Annual Holding Cost is ... ', annualHoldingCost)

annualOrders = (float(D)/float(qStar))

print('The number of orders to make annualy is ...', annualOrders)


associatedAnnualOrderingCost = (float(D)/float(qStar)) * float(S)

print('The associated annual ordering cost is ...', associatedAnnualOrderingCost)
      

