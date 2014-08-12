__author__ = 'Anaelys'


def convert():
    # A program to compute and print a table of Celsius temperatures and the Fahrenheit equivalents
    # every 10 degrees from 0C to 100C.

    from prettytable import PrettyTable

    table = PrettyTable(["Celsius ", "Fahrenheit"])

    for celsius_temp in range(0, 110, 10):
        fahrenheit_temp = 9 / 5 * celsius_temp + 32
        table.add_row([celsius_temp, fahrenheit_temp])

    print("This program computes and prints a table of Celsius temperatures and the Fahrenheit equivalents")
    print("every 10 degrees from 0C to 100C.")
    print()
    print(table)


def avg():
    # A simple program to average exam scores
    print("This program computes the average of exam scores")

    scores = eval(input("Enter scores separated by a comma: "))  # scores store a tuple
    average = sum(scores)/len(scores)

    print("The average of the scores is:", average)


def futval():
    # A program to compute the value of an investment carried 10 years into the future.
    print("This program calculates the future value")
    print("of a 10-year investment")

    principal = eval(input("Enter the initial principal: "))  # amount of money being invested in dollars.
    apr = eval(input("Enter the annual interest rate: "))  # annual percentage rate expressed as a decimal number.

    for i in range(10):
        principal = principal * (1 + apr)  # principal + principal * apr

    print("The value in 10 years is:", principal)


def futval_period():
    # A program to compute the value of an investment carried n years into the future where
    # the interest is compounded x times a year.

    print("""
This program calculates the future value of an investment carried certain amount of years"
where the interest is compounded certain times a year into the future""")
    print()

    years = eval(input("Enter the number of years for the investment: "))
    principal = eval(input("Enter the initial principal: "))
    annual_rate = eval(input("Enter the annual interest rate: "))
    period = eval(input("""Enter the number of times that the interest is
    compounded each year: """))

    for i in range(years * period):
        principal = principal * (1 + annual_rate/period)

    print("The value in", years, "years is:", principal)


def calculator():
    # A program to calculate mathematical expressions
    print("This program calculates mathematical expressions")
    print()

    for i in range(100):
        expression = eval(input("Enter the mathematical expression: "))
        print("The result is:", expression)


def main():

    options = {1: convert,
               2: avg,
               3: futval,
               4: futval_period,
               5: calculator}

    print("""Menu:
             Press 1 to execute "Covert Program"
             Press 2 to execute "Average Program"
             Press 3 to execute "Investment Program"
             Press 4 to execute "Investment by Compounded Period  Program"
             Press 5 to execute "Calculator Program"
    """)

    option = eval(input())

    options[option]()


main()
