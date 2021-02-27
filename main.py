import time
import PySimpleGUI as sg
import other_stuff
import layouts


time_taken = 0
type_test_layout = layouts.type_test_layout
enter_name_layout = layouts.enter_name_layout
words = other_stuff.list_to_string(other_stuff.type_test)

# Create the window
window = sg.Window('Typing Test', type_test_layout, no_titlebar=False, grab_anywhere=False)

do_not_reroute_stdout = True
test_running = False
test_done = False

# Typing test event loop
while True:
    event, values = window.read(timeout=1)

    if event == '-OK-' and values['-INPUT-'] == words:
        test_running = False
        test_done = True
        print(other_stuff.word_amount)
        print(time_taken)
        window['-TEXT-'].update(f"Nice! Your speed was {round(other_stuff.word_amount / (time_taken / 60))} WPM.")
        window.read(timeout=0)
        time.sleep(2)
        window.close()
        break

    elif event == '-OK-' and values['-INPUT-'] != words:
        window['-TEXT-'].update("Oops! It looks like there is a mistake!")

    if round(time_taken) == 1:
        window['-TIMER-'].update(f"{round(time_taken)} second")

    else:
        window['-TIMER-'].update(f"{round(time_taken)} seconds")

    if len(values['-INPUT-']) > 0 and not test_done:
        test_running = True

    if not test_running:
        start_time = time.time()

    else:
        # noinspection PyUnboundLocalVariable
        time_taken = time.time() - start_time

    # End program if user presses the X icon
    if event == '-EXIT-' or event == sg.WIN_CLOSED:
        exit()


window2 = sg.Window('Enter Initials', enter_name_layout, no_titlebar=False, grab_anywhere=False)


while True:
    event, values = window2.read(timeout=1)

    if event == '-OK-' and len(values['-INPUT-']) == 2 or len(values['-INPUT-']) == 3:
        window.close()

    # End program if user presses the X icon
    if event == '-EXIT-' or event == sg.WIN_CLOSED:
        exit()
