sales = float(input("Enter the amount of sales: "))


if sales > 500:
    bonus = 50.0
    commission_rate = 0.12
    # Calculate the commission rate
    commission = sales * commission_rate


print("You met your sales quota!")
# print(sales)
# display the commission..
print("The commission is £", format(commission, ',.2f'), sep='')
