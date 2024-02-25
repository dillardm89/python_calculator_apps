# Values displayed on calculator buttons
button_text = ['%', 'π', 'e', 'Clr', '\u232B',
               '²\u221Ax', 'ʸ\u221Ax', '¹/ₓ', '|x|', 'MOD',
               'x²', '(', ')', 'n!', '÷',
               'xʸ', '7', '8', '9', 'x',
               '10ˣ', '4', '5', '6', '-',
               'log', '1', '2', '3', '+',
               'ln', '±', '0', '.', '=']

# Values displayed in calculator entry field
# 'skip' for buttons with separate functions in tkinter_functions
display_text = ['%', 'π', 'e', 'skip', 'skip',
                '^(¹/₂)', '^(1/', '^(-1)', 'skip', 'MOD',
                '²', '(', ')', 'skip', '÷',
                '^', '7', '8', '9', 'x',
                'skip', '4', '5', '6', '-',
                'skip', '1', '2', '3', '+',
                'skip', 'skip', '0', '.', 'skip']

# Button actions either specific values or function calls
button_action = ['/100', '*(335/113)', '*2.71828', 'clear_all', 'clear_last',
                 '**(1/2)', '**(1/', '**(-1)', 'abs_value', '%',
                 '**2', '(', ')', 'factorial', '/',
                 '**', 7, 8, 9, '*',
                 'ten_exponent', 4, 5, 6, '-',
                 'log_func', 1, 2, 3, '+',
                 'nat_log', 'toggle_negative', 0, '.', 'compute']
