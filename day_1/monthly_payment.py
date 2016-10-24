amount_due = 15000.0
monthly_payment = amount_due / 1.0
#print('The monthly payment is', monthly_payment, '.2f)
#print(12345.6789, '.2f)
print('The monthly payment', format(monthly_payment, '.2f'))

#formatting in Scientific notation
print(format(12345.6789, 'e'))
print(format(12345.6789, '.2e'))

#Inserting Comma Seperators
print(format(12345.6789, ',.2f'))

#Here is an example that formats an even larger number
print(format(123456789.456, ',.2f'))

#The comma 