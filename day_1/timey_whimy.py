total_seconds = float(input('Enter a number of seconds: '))
#Get the number of hours
hours = total_seconds // 3600
#Get the number of remaining minutes
minutes = (total_seconds // 60) % 60
#Get the number of remaining seconds
seconds = total_seconds % 60


print('The number of hours, minutes and seconds are: ')
print('Hours: ', hours)
print('Minutes: ', minutes)
print('Seconds: ', seconds)



