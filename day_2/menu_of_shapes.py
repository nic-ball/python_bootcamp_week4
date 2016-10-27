from day_2 import circle_pit, riggidy_riggidy_rect_angle


AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5


def main():
    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()
        choice = int(input("Enter you selection: "))
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("Enter the circles radius: "))
            print("The area is", circle_pit.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input("Enter the circles radius: "))
            print("The circumference is", circle_pit.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangles width: "))
            length = float(input("Enter the rectangles length: "))
            print("The area is", riggidy_riggidy_rect_angle.area(width, length))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangles width: "))
            length = float(input("Enter the rectangles length"))
            print("The perimeter is", riggidy_riggidy_rect_angle.perimeter(width, length))
        elif choice == QUIT_CHOICE:
            print("Exiting the program...")
        else:
            print("ERROR: Invalid selection.")


def display_menu():
    print("MENU")
    print("1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Quit")


main()
