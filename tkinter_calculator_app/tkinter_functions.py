from tkinter import (Tk, Entry)
import tkinter as tk
import tkinter_buttons as buttons
import ast
import math

# Create calculator app base with entry field
base = Tk()
base.title('Tkinter Calculator')
display_field = Entry(base, font=18)
display_field.grid(row=1, columnspan=5, sticky=tk.EW, padx=4, pady=4)

''' List that will store values and functions from
    calculator entry to be modified and evaluated
'''
action_list = []


def get_last_num_op():
    '''
        get_last_num_op : identifies last number, whether
            last number is negative, and last operator if
            entered after last number in order to modify
            with other functions

        Returns:
            start_new_string (str) : calculator display string shortened
                to exclude last number and operator
            last_entry (int or float) : last number entered
            last_operator (str) : if operator entered after last number
                returns last operator value or blank if none
            new_index (int) : action_list index location to update last_entry
            last_num_index (int) : action_list index location of last
                number entered to update last operator if an operator
                entered after last number
            negative_last_entry (str) : value = '-' if last number entered
                is negative or blank if number positive
    '''
    global action_list

    current_display = display_field.get()
    current_display_len = len(current_display)
    action_list_len = len(action_list)
    last_operator = ''
    negative_last_entry = ''

    # Stores value and index of last entry
    last_entry = action_list[-1]
    last_entry_len = len(str(last_entry))
    new_index = action_list_len - last_entry_len
    last_num_index = -1

    ''' If last entry not number, updates value and index
        for last number entered
    '''
    if isinstance(last_entry, str):
        last_operator = current_display[-1]
        last_entry = action_list[-2]
        last_entry_len = len(str(last_entry)) + len(last_operator)
        new_index = action_list_len - last_entry_len
        last_num_index = -2

    # Checks if last number entered is negative
    try:
        if action_list[new_index - 1] == '-':
            negative_last_entry = '-'
            last_entry_len += len(negative_last_entry)
            new_index -= len(negative_last_entry)
    except Exception:
        pass

    start_new_string = current_display[0:current_display_len - last_entry_len]
    return [start_new_string, last_entry, last_operator, new_index,
            last_num_index, negative_last_entry]


def update_display_text(new_string):
    '''
        update_display_text : clears calculator display field
            and updates with new_string

        Args:
            new_string (str) : calculator display string updated
                with new values by other functions
    '''
    display_field.delete(0, 'end')
    display_field.insert(0, new_string)


def update_action_list(new_index, new_list_entry,
                       closing_operator, last_num_index):
    '''
        update_action_list : update action_list with
            values modified by other functions

        Args:
            new_index (int) : action_list index location to insert value
            new_list_entry (str): value of operator from other functions
                to insert in action_list at new_index
            closing_operator (str): closing operator from other functions
                to insert in action_list after last number
            last_num_index (int) : action_list index location of last
                number entered to update last operator if an operator
                entered after last number
    '''
    action_list.insert(new_index, new_list_entry)

    if closing_operator == '':
        pass
    elif last_num_index == -1:
        action_list.append(closing_operator)
    else:
        action_list.insert(-1, closing_operator)


def generate_new_string(new_display_string, closing_display_string):
    '''
        generate_new_string : create new display field entry string
            updated from other functions

        Args:
            new_display_string (str): portion of display field entry
                string updated from other functions
            closing_display_string (str): new string portion to add
                at end of display field entry

        Returns:
            new_string (str) : updated display field entry string
            new_index (int) : index location to update action_list
                with updated values
            last_num_index (int) : action_list index location of
                last number entered
    '''
    # Get index and values for last number and operator
    results = get_last_num_op()
    start_new_string = results[0]
    last_entry = results[1]
    last_operator = results[2]
    new_index = results[3]
    last_num_index = results[4]
    negative_last_entry = results[5]

    new_string = start_new_string + new_display_string + \
        negative_last_entry + str(last_entry) + \
        closing_display_string + last_operator
    return [new_string, new_index, last_num_index]


def btn_function(text, action):
    '''
        btn_function : update display field and action_list
            with text / action value of button pressed

        Args:
            text (str) : display_text value for selected button
            action (str) : button_action value for selected button
    '''
    global action_list

    display_text_len = len(display_field.get())

    # Stores last value if action_list not empty
    try:
        last_entry = action_list[-1]
    except Exception:
        last_entry = ''

    ''' If last entry is number and action is number,
        updates action_list value with new number (ex: 1 + 2 -> 12).
        Otherwise, appends action_list with action value
    '''
    if (isinstance(last_entry, (int, float))
            and isinstance(action, (int, float))):
        new_last_entry = str(last_entry) + str(action)
        action_list[-1] = type(last_entry)(new_last_entry)
    else:
        action_list.append(action)

    # Appends display field with text value
    display_field.insert(display_text_len, text)


def clear_all():
    '''
        clear_all : clears display field entry and action_list
    '''
    global action_list
    display_field.delete(0, 'end')
    action_list = []


def clear_last():
    '''
        clear_last : removes last entered item from display
            field entry and action_list
    '''
    global action_list

    try:
        last_entry = action_list[-1]

        ''' Check if last item entered is number or operator to
            clear last digit of number or full operator function
        '''
        if isinstance(last_entry, str):
            try:
                last_display_text = buttons.display_text[
                    buttons.button_action.index(last_entry)]
            except Exception:
                last_display_text = ')'
            finally:
                delete_from_index = (len(display_field.get()) -
                                     len(last_display_text))
                display_field.delete(delete_from_index, 'end')
                action_list.pop()
        elif len(str(last_entry)) == 1:
            display_field.delete(len(display_field.get())-1, 'end')
            action_list.pop()
        else:
            new_last_entry_str = str(last_entry)[0:-1]
            new_last_entry = type(last_entry)(new_last_entry_str)

            action_list[-1] = new_last_entry
            display_field.delete(len(display_field.get())-1, 'end')
    except Exception:
        clear_all()


def toggle_negative():
    '''
        toggle_negative : toggle last number entered between
            negative and positive value
    '''
    global action_list

    current_display = display_field.get()
    current_display_len = len(current_display)
    last_display_text = ''
    new_string = ''
    reversed_action_list = list(reversed(action_list))

    ''' Iterate through reverse of action_list to identify
        the last number entered then determines whether to
        update positive or negative based on adjacent values,
        finally updates action_list and display field entry

        Ex: 9+7 -> 9-7, abs(9) -> abs(-9), 57 -> -57,
            9x8 -> 9x-8, 10^(-6) -> 10^(6)
    '''
    for k in range(len(reversed_action_list)):
        if isinstance(reversed_action_list[k], str):
            try:
                last_display_text = (buttons.display_text[
                    buttons.button_action.index(reversed_action_list[k])]
                    + last_display_text)
            except Exception:
                last_display_text = ')'
            finally:
                continue

        if (k+1) >= len(reversed_action_list):
            reversed_action_list.insert(k+1, '-')
            new_display_text = '-' + \
                str(reversed_action_list[k]) + last_display_text
            new_display_len = len(new_display_text) - 1

        elif reversed_action_list[k+1] == '+':
            reversed_action_list[k+1] = '-'
            new_display_text = '-' + \
                str(reversed_action_list[k]) + last_display_text
            new_display_len = len(new_display_text)

        elif (reversed_action_list[k+1] == '-'
                and (k+2) >= len(reversed_action_list)):
            del reversed_action_list[k+1]
            new_display_text = str(reversed_action_list[k]) + last_display_text
            new_display_len = len(new_display_text) + 1

        elif (reversed_action_list[k+1] == '-'
              and reversed_action_list[k+2] in ('*', '/', '**')):
            del reversed_action_list[k+1]
            new_display_text = str(reversed_action_list[k]) + last_display_text
            new_display_len = len(new_display_text) + 1

        elif (reversed_action_list[k+1] == '-'
                and isinstance(reversed_action_list[k+2], str)):
            reversed_action_list[k+1] = '+'
            new_display_text = '+' + \
                str(reversed_action_list[k]) + last_display_text
            new_display_len = len(new_display_text)

        elif reversed_action_list[k+1] == '-':
            reversed_action_list[k+1] = '+'
            new_display_text = '+' + \
                str(reversed_action_list[k]) + last_display_text
            new_display_len = len(new_display_text)

        else:
            reversed_action_list.insert(k+1, '-')
            new_display_text = '-' + \
                str(reversed_action_list[k]) + last_display_text
            new_display_len = len(new_display_text) - 1

        action_list = list(reversed(reversed_action_list))
        break

    start_new_string = current_display[0:current_display_len - new_display_len]
    new_string = start_new_string + new_display_text
    update_display_text(new_string)


def abs_value():
    '''
        abs_value : update action_list and display field entry
            for absolute value function
    '''
    global action_list

    # Values to update action_list and display field string
    new_display_string = 'abs('
    new_list_entry = 'abs('
    closing_display_string = ')'
    closing_operator = ')'

    # Generate new string and get index values to update action_list
    results = generate_new_string(new_display_string, closing_display_string)
    new_string = results[0]
    new_index = results[1]
    last_num_index = results[2]

    update_action_list(new_index, new_list_entry,
                       closing_operator, last_num_index)
    update_display_text(new_string)


def ten_exponent():
    '''
        ten_exponent : update action_list and display field entry
            for exponent base 10 function
    '''
    global action_list

    # Values to update action_list and display field string
    new_display_string = '10^('
    new_list_entry = '10**('
    closing_display_string = ')'
    closing_operator = ')'

    # Generate new string and get index values to update action_list
    results = generate_new_string(new_display_string, closing_display_string)
    new_string = results[0]
    new_index = results[1]
    last_num_index = results[2]

    update_action_list(new_index, new_list_entry,
                       closing_operator, last_num_index)
    update_display_text(new_string)


def factorial():
    '''
        factorial : update action_list and display field entry
            for factorial function
    '''
    global action_list

    # Values to update action_list and display field string
    new_display_string = 'fact('
    new_list_entry = 'math.factorial('
    closing_display_string = ')'
    closing_operator = ')'

    # Generate new string and get index values to update action_list
    results = generate_new_string(new_display_string, closing_display_string)
    new_string = results[0]
    new_index = results[1]
    last_num_index = results[2]

    update_action_list(new_index, new_list_entry,
                       closing_operator, last_num_index)
    update_display_text(new_string)


def log_func():
    '''
        log_func : update action_list and display field entry
            for log base 10 function
    '''
    global action_list

    # Values to update action_list and display field string
    new_display_string = 'log('
    new_list_entry = 'math.log('
    closing_display_string = ')'
    closing_operator = ',10)'

    # Generate new string and get index values to update action_list
    results = generate_new_string(new_display_string, closing_display_string)
    new_string = results[0]
    new_index = results[1]
    last_num_index = results[2]

    update_action_list(new_index, new_list_entry,
                       closing_operator, last_num_index)
    update_display_text(new_string)


def nat_log():
    '''
        nat_log : update action_list and display field entry
            for natural log (log base e) function
    '''
    global action_list

    # Values to update action_list and display field string
    new_display_string = 'ln('
    new_list_entry = 'math.log('
    closing_display_string = ')'
    closing_operator = ',2.71828)'

    # Generate new string and get index values to update action_list
    results = generate_new_string(new_display_string, closing_display_string)
    new_string = results[0]
    new_index = results[1]
    last_num_index = results[2]

    update_action_list(new_index, new_list_entry,
                       closing_operator, last_num_index)
    update_display_text(new_string)


def compute():
    '''
        compute : converts values in action_list to strings
            then parses, compiles, and evaluates string as
            math function to display result
    '''
    global action_list

    for k in range(len(action_list)):
        action_list[k] = str(action_list[k])

    entry_string = ''.join(action_list)
    try:
        node = ast.parse(entry_string, mode='eval')
        result = eval(compile(node, '<string>', 'eval'))
        clear_all()
        action_list = [result]
        display_field.insert(0, result)
    except Exception as error:
        clear_all()
        print('error: ', error)
        display_field.insert(0, 'Error')


# Bind keyboard buttons to functions
base.bind('<Return>', compute)
base.bind('<BackSpace>', clear_last)
