import PySimpleGUI as sg
import other_stuff

sg.theme('Dark')
sg.SetOptions(font="Georgia 10")

exit = other_stuff.exit
ok = other_stuff.ok
words = other_stuff.list_to_string(other_stuff.words)

time_taken = 10

layout = [
            [sg.Text("Quick, type!                                          ", key='-TEXT-')],
            [sg.InputText(key='-INPUT-')],
            [sg.Button('', image_data=exit, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='-EXIT-'), 
            sg.Button('', image_data=ok, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0,  key='-OK-')],
            [sg.Text()]]

# Create the window
window = sg.Window('Typing Test', layout, no_titlebar=True, grab_anywhere=True)

do_not_reroute_stdout = True

# Create an event loop
while True:
    event, values = window.read()
    if event == '-OK-' and window['-INPUT-'].read() == other_stuff.typetest:
            window['-TEXT-'].update(f"Correct! Your speed was {other_stuff.word_amount / (time_taken / 60)} WPM")
    # End program if user closes window or
    # presses the OK button
    if event == '-EXIT-' or event == sg.WIN_CLOSED:
        break