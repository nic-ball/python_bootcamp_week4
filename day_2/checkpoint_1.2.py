sales = float(input("Enter the amount of sales: "))


if sales >= 10000:
    commission_rate = 0.2
    commission = sales * commission_rate


print("You met your sales target!")
print("Your bonus is £", format(commission, ',.2f'), sep='')