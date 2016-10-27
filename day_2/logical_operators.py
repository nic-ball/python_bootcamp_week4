minutes = int(input("Minutes: "))
temperature = int(input("Temp: "))


if temperature < 20 and minutes > 12:
    print("The temperature is in the danger zone!")


minutes = int(input("Minutes: "))
temperature = int(input("Temp: "))


if temperature < 20 or minutes > 12:
    print("The temperature is in the danger zone")


if not(temperature < 20):
    print("The temperature is in the danger zone")