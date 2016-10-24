#Calculating a Percentage
#This program gets an items original price and
#Calculates its sales price, with a 20& discount

#Get original price
original_price = float(input('Enter the items price: '))
sale_price = original_price * 0.2
reduced_price = original_price - sale_price
print('This item is on sale and is now: ', reduced_price)