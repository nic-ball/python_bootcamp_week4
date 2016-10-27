speed = int(input("Please enter the Speed you were travelling: "))


if speed >= 0 and speed < 70:
    print("The speed", speed, "MPH",  "was legal!")


elif speed < 0:
    print("Travelling at", speed, "MPH!!!", "Where you in reverse?")


else:
    print("The speed", speed, "MPH", "was a bit too quick!")
