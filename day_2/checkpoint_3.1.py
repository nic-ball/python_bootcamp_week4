own_home = input("Do you own you home? Yes: 1 and No: 2\n")
years_employed = int(input("How many years have you been at your current employer\n"))

if own_home == 1 and years_employed >= 3:
    print("How much would you like?")


elif own_home == 1 or years_employed <= 3:
    print("You qualify for a loan! Congratulations")


elif own_home == 2 and years_employed >= 3:
    print("You qualify for a loan!")


else:
    print("Sorry, Go get a job....Loser")