import random


def main():

    number1 = random.randrange(10)

    number2 = random.randrange(5, 10)

    number3 = random.randrange(0, 101, 10, 12)

    number4 = random.random()

    print('The number is', number1, number2, number3, number4)

    print(random.randint(1, 10))


main()
