import PySimpleGUI as sg
import other_stuff

words = other_stuff.type_test
time_taken = 0

sg.theme('Dark')
sg.SetOptions(font="Bahnschrift 25")

# noinspection PyTypeChecker
type_test_layout = [
    [sg.Text(
        "Quick, type!",
        size=(29, None),
        pad=(1, 1),
        justification='left',
        key='-TEXT-'),

        sg.Text("0 seconds",
                size=(15, None),
                justification='r',
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
             pad=(10, 20))]
]

# noinspection PyTypeChecker
enter_name_layout = [
    [sg.Text("Great job! Enter your initials here:",
             pad=(None, 10),
             key='-TEXT-')],

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
               key='-OK-')]
]

# noinspection PyTypeChecker
leaderboard_layout = [
    [sg.Text("Top 10 scores:",
             size=(20, None),
             justification='c',
             pad=(None, 10),
             key='-TEXT-')],
    [sg.Text("1: ",
             size=(20, None),
             key='-P1-')],
    [sg.Text("2: ",
             size=(20, None),
             key='-P2-')],
    [sg.Text("3: ",
             size=(20, None),
             key='-P3-')],
    [sg.Text("4: ",
             size=(20, None),
             key='-P4-')],
    [sg.Text("5: ",
             size=(20, None),
             key='-P5-')],
    [sg.Text("6: ",
             size=(20, None),
             key='-P6-')],
    [sg.Text("7: ",
             size=(20, None),
             key='-P7-')],
    [sg.Text("8: ",
             size=(20, None),
             key='-P8-')],
    [sg.Text("9: ",
             size=(20, None),
             key='-P9-')],
    [sg.Text("10: ",
             size=(20, None),
             key='-P10-')]
]
