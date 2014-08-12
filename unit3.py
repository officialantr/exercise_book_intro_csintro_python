__author__ = 'Anaelys'
import math

# pending - 9, *10, 13, 14, *15, *17


def calculate_volume_sphere(radius):
    v = 4/3 * math.pi * (radius ** 3)
    return v


def calculate_area_sphere(radius):
    area = 4 * math.pi * (radius ** 2)
    return area


def volume_area():
    print("This program calculates the volume and surface area of a sphere from its radius")
    print()
    radius = eval(input("Enter the radius of the sphere: "))

    print("The volume of the sphere is:", calculate_volume_sphere(radius))
    print("The area of the sphere is:", calculate_area_sphere(radius))


def pizza_program():
    print("This program calculates the cost per square inch of a circular pizza,")
    print("given its diameter and price")
    print()
    radius = eval(input("Enter the diameter of the pizza(in inches): "))/2
    price = eval(input("Enter the price of the pizza: "))
    area = math.pi * (radius ** 2)  # square inch
    cost_per_square_inch = area/price
    print("The cost per square inch of the pizza is:", cost_per_square_inch)


def hydrocarbon_program():
    print("This program determines the molecular weight of a hydrocarbon.")
    print()
    h = 1.0079
    c = 12.011
    o = 15.9994

    number_h = eval(input("Enter the number of hydrogen atoms: "))
    number_c = eval(input("Enter the number of carbon atoms: "))
    number_o = eval(input("Enter the number of oxygen atoms: "))

    total = h * number_h + c * number_c + o * number_o

    print("The molecular weight of the hydrocarbon is ", total, "grams/mole")


def lightning_strike_program():
    print("This program determines the distance to a lightning strike based on the time elapsed")
    print("between the flash and the sound of the thunder.")
    print()

    time = eval(input("Enter the time (in seconds) elapsed between the flash and thunder: "))
    distance = 1100 * time  # 1110 ft/second

    distance_miles = distance/5280  # 1 mile is 5280 ft.

    print("The distance to a lightening strike is ", distance_miles, "miles")


def konditorei_coffee_program():
    print("This program calculates the cost of an order")
    print()
    pounds = eval(input("Enter the number of pounds of the order: "))
    cost = pounds * 12 + 1.50  # 12 = 10.50 + 1.50
    print("The cost of the order is $", cost, sep="")


def slope_line_program():
    print("This program calculates the slope of a line through two (non-vertical) points")
    print("entered by the user and determines between them")
    print()
    x1, y1 = eval(input("Enter the coordinates of the point 1 separated by comma (x1,y1) : "))
    x2, y2 = eval(input("Enter the coordinates of the point 2 separated by comma (x2,y2) : "))

    slope = (y2 - y1)/(x2 - x1)
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    print("The slope of the line is", slope )
    print("The distance between the two points is:", distance)


def gregorian_epact_program():
    print("This program calculates the Gregorian Epact")
    print("")

    year = eval(input("Enter the year to calculate the corresponding epact: "))

    c = year//100
    epact = (8 + (c//4) - c + ((8*c+13)//25) + 11*(year % 19)) % 30

    print("The epact for the year", year, "is", epact)


def sum_fist_numbers_program():
    print("This program sums the first n natural numbers")
    print()
    number = eval(input("Enter n: "))

    result = sum(range(1, number+1))
    result_cubes = sum([i**3 for i in range(1, number+1)])

    print("The sum of the first", number, "natural numbers is", result)
    print("The sum of the cubes of the first", number, "natural numbers is", result_cubes)


def nth_fibonacci_program():
    print("")
    print()

    n = eval(input("Enter n: "))
    a, b = 0, 1  # By definition, the first two numbers in the Fibonacci sequence are 1 and 1

    amount_number_serie = 1
    while amount_number_serie < n:
        a, b = b, b + a
        amount_number_serie += 1

    print("The nth Fibonacci number is", b)


def main():
    options = {1: volume_area,
               2: pizza_program,
               3: hydrocarbon_program,
               4: lightning_strike_program,
               5: konditorei_coffee_program,
               6: slope_line_program,
               7: gregorian_epact_program,
               8: sum_fist_numbers_program,
               9: nth_fibonacci_program}

    print(""" Menu:
              Press 1 to execute "Volume and Area of a Sphere Program"
              Press 2 to execute "Pizza cost per square inch Program"
              Press 3 to execute "Hydrocarbon Program"
              Press 4 to execute "Lightening Strike Program"
              Press 5 to execute "Konditorei Coffee Program"
              Press 6 to execute "Slope of a Line Program"
              Press 7 to execute "Gregorian Epact Program"
              Press 8 to execute "Sum First n Numbers Program"
              Press 9 to execute "nth Fibonacci Number Program"
    """)
    option = eval(input())
    options[option]()

main()

