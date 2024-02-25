import time
import sys
import re

"""This is a command line Python calculator.

Returns:
    float: The result of user input for basic add, subtract, multiply,
    and divide functions.
"""


def numbers_list(user_input):
    """Function to return a list of float values for all numbers found
    within user input string

    Args:
        user_input (string): User input string for selected
        function, ex: '3 + 3'

    Returns:
        list: list of float values, ex: (3.0, 3.0)
    """

    numbers = re.findall(r'\d*\.*\d+', user_input)
    numbers = list(map(float, numbers))
    return numbers


def return_to_menu():
    """Function to return to main menu
    """

    input('Press "Enter" key to return to menu.')
    menu()


def add():
    """Function that parses numbers from user input string then adds all values

    Returns:
        float: The result of adding of all numbers entered by user
    """

    user_input = input('Enter addition statement: ')
    input_error = re.findall(r'[-/*%=]', user_input)

    while input_error:
        print('Please enter only "+" operations.')
        input_error = ""
        user_input = input('Enter addition statement: ')

    if not input_error:
        numbers = numbers_list(user_input)

        numbers_add = numbers[0]
        for i in range(1, len(numbers)):
            numbers_add += numbers[i]

        print(numbers_add)
        return_to_menu()


def subtract():
    """Function that parses numbers from user input string
    then subtracts all values

    Returns:
        float: The result of subtracting of all numbers entered by user
    """

    user_input = input('Enter subtraction statement: ')
    input_error = re.findall(r'[+/*%=]', user_input)

    while input_error:
        print('Please enter only "-" operations.')
        input_error = ""
        user_input = input('Enter subtraction statement: ')

    if not input_error:
        numbers = numbers_list(user_input)

        numbers_subtract = numbers[0]
        for i in range(1, len(numbers)):
            numbers_subtract -= numbers[i]

        print(numbers_subtract)
        return_to_menu()


def multiply():
    """Function that parses numbers from user input string then
    multiplies all values

    Returns:
        float: The result of multiplying of all numbers entered by user
    """

    user_input = input('Enter multiplication statement: ')
    input_error = re.findall(r'([*]{2})|[-+/%=]', user_input)

    while input_error:
        print('Please enter only "*" operations.')
        input_error = ""
        user_input = input('Enter multiplication statement: ')

    if not input_error:
        numbers = numbers_list(user_input)

        numbers_multiply = numbers[0]
        for i in range(1, len(numbers)):
            numbers_multiply *= numbers[i]

        print(numbers_multiply)
        return_to_menu()


def divide():
    """Function that parses numbers from user input string then
    divides all values

    Returns:
        float: The result of dividing of all numbers entered by user
    """

    user_input = input('Enter division statement: ')
    input_error = re.findall(r'([/]{2})|[-+*%=]', user_input)

    while input_error:
        print('Please enter only "/" operations.')
        input_error = ""
        user_input = input('Enter division statement: ')

    if not input_error:
        numbers = numbers_list(user_input)

        numbers_divide = numbers[0]
        for i in range(1, len(numbers)):
            numbers_divide /= numbers[i]

        print(numbers_divide)
        return_to_menu()


def exit_calculator():
    """Function to exit program
    """

    print('Exiting...')
    time.sleep(1)
    sys.exit()


def menu():
    """Main menu function for user to select function to perform
    """

    print('Calculator Operations:\n1: Add\n2: Subtract\n3: Multiply\n' +
          '4: Divide\n5: Exit')

    selection = int(input('Enter the operation number: '))

    if selection == 1:
        add()
    elif selection == 2:
        subtract()
    elif selection == 3:
        multiply()
    elif selection == 4:
        divide()
    else:
        exit_calculator()


if __name__ == "__main__":
    menu()
