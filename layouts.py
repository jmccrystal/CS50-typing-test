import PySimpleGUI as sg
import other_stuff

words = other_stuff.list_to_string(other_stuff.type_test)
time_taken = 0

sg.theme('Dark')
sg.SetOptions(font="Bahnschrift 25")

# noinspection PyTypeChecker
type_test_layout = [
    [sg.Text(
        "Quick, type!",
        size=(33, None),
        key='-TEXT-'),

        sg.Text(0,
                size=(11, 1),
                justification='right',
                key='-TIMER-')],

    [sg.Input(
        key='-INPUT-', pad=(None, 25))],

    [sg.Button('',
               image_data=other_stuff.exit_icon,
               button_color=(sg.theme_background_color(),
                             sg.theme_background_color()),
               border_width=0,
               pad=((0, 0), (0, 0)),
               key='-EXIT-'),

     sg.Button('',
               image_data=other_stuff.ok_icon,
               button_color=(sg.theme_background_color(),
                             sg.theme_background_color()),
               border_width=0,
               pad=((25, 0), (0, 0)),
               bind_return_key=True,
               key='-OK-')],

    [sg.Text(words,
             size=(44, None),
             pad=(10, 20))]]

# noinspection PyTypeChecker
enter_name_layout = [
    [sg.Text("Great job! Enter your initials here:",
             pad=(None, 10))],

    [sg.Input(pad=(None, 10),
              key='-INPUT-')],

    [sg.Button('',
               image_data=other_stuff.exit_icon,
               button_color=(sg.theme_background_color(),
                             sg.theme_background_color()),
               border_width=0,
               pad=((0, 0), (20, 25)),
               key='-EXIT-'),

     sg.Button('',
               image_data=other_stuff.ok_icon,
               button_color=(sg.theme_background_color(),
                             sg.theme_background_color()),
               border_width=0,
               pad=((25, 0), (20, 25)),
               bind_return_key=True,
               key='-OK-')]]
