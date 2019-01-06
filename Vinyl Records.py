print('Hipster\'s Local vinyl records- customer order details\n')
na=input('Enter the customer\'s name:')
dis=int(input('Enter the distance in kilometers for delivery:'))
pur=int(input('Enter the cost of cost of records purchased $:'))

de=dis*15
tax1=(float(de))*(15/100)
tax2=(float(pur))*(15/100)
to=float(de)+tax1+tax2
print('Purchase summary for',na)
print('Delivery Cost $:',de)
print('Total cost $:',to)
