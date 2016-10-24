value1 = 99
value2 = 45.9
value3 = 7.0
value4 = 7
value5 = 'abc'

print(value1.__class__)
print(value2.__class__)
print(value3.__class__)
print(value4.__class__)
print(value5.__class__)

#reading input from the keyboard string type
#get the users first name
first_name = input('Enter your first name: ')
#get the users last name
last_name = input('Enter your last name: ')
#print a greeting to the user
print('Hello, ', first_name, last_name)


string_value = input('How many hours did you work?\n')
hours = int(string_value)
print(hours)

#example 2: better
hours = int(input('How many hours did you work?\n'))
print(hours)