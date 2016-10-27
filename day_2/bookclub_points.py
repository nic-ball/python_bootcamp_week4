books = int(input("How many books have you purchased this month? \n"))


if books >= 4:
    print("You have earned 60 points!!!")


elif books == 3:
    print("You have earned 30 points!!")


elif books == 2:
    print("You have earned 15 points!")


elif books == 1:
    print("You have earned 5 points.")


elif books == 0:
    print("You haven't earned any points this month. ")


else:
    print("Do you know how to read?")
