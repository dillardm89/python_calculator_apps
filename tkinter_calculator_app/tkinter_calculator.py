from tkinter import Button
import tkinter.font as font
import tkinter_buttons as buttons
import tkinter_functions as func

''' This is a Tkinter Calculator Application.
    User can perform a variety of simple and
    scientific calculations.
'''


# Loop to create calculator buttons from tkinter_buttons
btn_width = 4
btn_height = 2
font_size = font.Font(size=14)
j = 0
for x in range(7):
    for y in range(5):
        btn_text = buttons.button_text[j]
        display_text = buttons.display_text[j]
        btn_action = buttons.button_action[j]

        ''' display_text = 'skip' for buttons with specific
            functions in tkinter_functions.
            Otherwise, button function from button_actions.
        '''
        if display_text == 'skip':
            btn_function_string = eval('func.' + btn_action)
            button = Button(func.base, text=btn_text, width=btn_width,
                            height=btn_height, font=font_size,
                            command=btn_function_string)
        else:
            button = Button(func.base, text=btn_text, width=btn_width,
                            height=btn_height, font=font_size,
                            command=lambda text=display_text,
                            action=btn_action: func.btn_function(text, action))

        button.grid(row=x+2, column=y)
        j += 1

func.base.mainloop()
