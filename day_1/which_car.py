car1_price = float(input('Enter the price of Car 1: '))
car1_mpg = float(input('Enter the MPG of Car 1: '))

car2_price = float(input('Enter the price of Car 2: '))
car2_mpg = float(input('Enter the MPG of Car 2: '))

avg_miles = float(input('Enter the average amount of miles that you travel in a year: '))
total_miles = avg_miles * 10

price_per_gallon = 5.32
price_per_mile1 = price_per_gallon * total_miles // car1_mpg
price_per_mile2 = price_per_gallon * total_miles // car2_mpg

total_price1 = car1_price + price_per_mile1
total_price2 = car2_price + price_per_mile2
print("The total cost of Car 1 over 10 years is: ", total_price1)
print("The total cost of Car 2 over 10 years is: ", total_price2)