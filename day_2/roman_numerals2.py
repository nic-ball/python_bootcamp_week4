units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]

for test_it in range(1, 11):
    ten, unit = divmod(test_it, 10)
    print(test_it[ten]+units[unit])