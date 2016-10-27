RESIDENTIAL = 1
COMMERCIAL = 2
INDUSTRIAL = 3
QUIT_CHOICE = 4


#Program to display utility info
def main():
    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()
        choice = int(input("Enter your selection: "))
    if choice == RESIDENTIAL:
        print("Your bill is", residential)
    elif choice == COMMERCIAL:
        print("your bill is", commercial)
    elif choice == QUIT_CHOICE:
        print("Exiting the program...")
    else:
        print("ERROR: Invalid selection")

meter_reading = float(input("Enter your initial meter reading: "))
latest_meter_reading = float(input("Enter your latest meter reading: "))


#Process customer information and display results
gallons_used = meter_reading - latest_meter_reading // 10

# r = residential, c = commercial, i = industrial


def display_menu():
    print("MENU")
    print("1) Residential")
    print("2) Commercial")
    print("3) Industrial")
    print("4) Quit")


def residential():
    return 5 + (gallons_used * 0.0005)


def commercial():
    if gallons_used <= 4000000:
        return 1000
    else:
        return 1000 + (gallons_used * 0.00025)


def industrial():
    if gallons_used <= 4000000:
        return 1000
    elif gallons_used >= 4000000 and gallons_used < 10000000:
        return 2000
    elif gallons_used >= 10000000:
        return 2000 + (gallons_used * 0.00025)
    else:
        print("ERROR: Does not compute...")




print("Your customer code is: ", customer_code)
print("Your initial meter reading: ", meter_reading)
print("Your latest meter reading is: ", latest_meter_reading)
print(gallons_used)
print("Your current bill is: ",)

