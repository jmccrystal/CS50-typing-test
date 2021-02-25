import time
import math
import PySimpleGUI as sg
import other_stuff

sg.theme('Dark')
sg.SetOptions(font="Bahnschrift 15", )

exit_icon = other_stuff.exit_icon
ok_icon = other_stuff.ok_icon
words = other_stuff.list_to_string(other_stuff.type_test)
time_taken = 0

layout = [
    [sg.Text("Quick, type!", size=(45, None), key='-TEXT-'), sg.Text(time_taken, size=(3, 1), key='-TIMER-')],
    [sg.Input(key='-INPUT-')],
    [sg.Button('', image_data=exit_icon, button_color=(sg.theme_background_color(), sg.theme_background_color()),
               border_width=0, key='-EXIT-'),
     sg.Button('', image_data=ok_icon, button_color=(sg.theme_background_color(), sg.theme_background_color()),
               border_width=0, bind_return_key=True, key='-OK-')],
    [sg.Text(words, size=(50, int(other_stuff.word_amount / 4)))]]

# Create the window
window = sg.Window('Typing Test', layout, no_titlebar=False, grab_anywhere=True)
test = 1

do_not_reroute_stdout = True
test_running = False
test_done = False

# Create an event loop
while True:
    event, values = window.read(timeout=1)

    if event == '-OK-' and values['-INPUT-'] == words:
        test_running = False
        test_done = True
        window['-TEXT-'].update(f"Nice! Your speed was {round(other_stuff.word_amount / (time_taken / 60))} WPM")

    window['-TIMER-'].update(time_taken)

    if len(values['-INPUT-']) > 0 and not test_done:
        test_running = True

    if not test_running:
        start_time = time.time() + .5

    if test_running:
        time_taken = round(time.time() - start_time)

    # End program if user presses the X icon
    if event == '-EXIT-' or event == sg.WIN_CLOSED:
        break
