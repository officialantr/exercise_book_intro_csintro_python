__author__ = 'Anaelys'

# A simple program illustrating chaotic behavior.


# def main():
#     print("This program illustrates a chaotic function")
#     x = eval(input("Enter a number between 0 and 1: "))
#     y = eval(input("Enter a modifier number: "))
#     z = eval(input("How many numbers should I print? "))
#     for i in range(z):
#         x = y * x * (1 - x)
#         print(x)
#
# main()


def compare_equivalent_expressions():
    print("This program illustrates a chaotic function")
    menu = """Menu:
                - Press "0" for exiting.
                - Press "1" for entering the data """

    def exit():
        return

    def handle_data():
        z = eval(input("How many numbers should I print? "))
        expressions = ["y * x * (1 - x)", "y * (x - x * x)", "y * x - y * x *x"]
        numbers = []
        modifiers = []

        # Getting Numbers
        amount_numbers = eval(input("How many numbers will you work with? "))
        for i in range(amount_numbers):
            number = eval(input("Enter a number between 0 and 1. Number {0} of {1}: ".format(i+1, amount_numbers)))
            numbers.append(number)

        # Getting Modifiers
        modifiers_numbers = eval(input("How many modifiers will you work with? "))
        for i in range(modifiers_numbers):
            modifier = eval(input("Modifier {0} of {1}: ".format(i+1, modifiers_numbers)))
            modifiers.append(modifier)

        # Printing the input numbers
        print()
        print("Results:")

        from prettytable import PrettyTable
        table = PrettyTable(["Expression ", "Modifier"] + ["x = {0}".format(n) for n in numbers])
        table.align = "l"

        results = {}
        for ex in expressions:
            results[ex] = {}
            table.add_row([ex] + (amount_numbers + 1)*[""])

            for y in modifiers:
                results[ex][y] = {}
                print()
                table.add_row(["", "y = {0}".format(y)] + amount_numbers*[""])

                # Getting results= {expression1: {modifier1:{number1:[], number2:[]}  , modifier2:{}  }, expression2: }
                for n in numbers:
                    list_result_per_number = []
                    x = n
                    for i in range(z):
                        x = eval(ex)
                        list_result_per_number.append(x)

                    results[ex][y][n] = list_result_per_number

                parameters_to_zip = []
                for numb in numbers:
                    list_show = results[ex][y][numb]
                    parameters_to_zip.append(list_show)

                for row_numbers in zip(*parameters_to_zip):
                    table.add_row(2*[""] + list(row_numbers))
        print(table)


    options = {0: exit, 1: handle_data}
    print(menu)
    option = eval(input())
    options[option]()

compare_equivalent_expressions()