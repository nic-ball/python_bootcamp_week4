A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60


def main():
    # Get the test score from the user
    score = int(input("Enter your test score: "))
    # Determine the grade
    if score >= A_SCORE:
        print("Your grade is A.")
    elif score >= B_SCORE:
        print("Your grade is B.")
    elif score >= C_SCORE:
        print("Your grade is C.")
    elif score >= D_SCORE:
        print("Your grade is D.")
    else:
        print("Your grade is F.")


main()
