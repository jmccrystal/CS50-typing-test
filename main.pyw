import pickle
import time
import PySimpleGUI as sg
import other_stuff
import layouts
import sys

time_taken = 0

type_test_layout = layouts.type_test_layout
enter_name_layout = layouts.enter_name_layout
leaderboard_layout = layouts.leaderboard_layout

words = other_stuff.type_test

# Create the window
window = sg.Window('Typing Test', type_test_layout, no_titlebar=False, grab_anywhere=False)

test_running = False
test_done = False


def verify_test(user_typing):
    if words == user_typing:
        return True
    else:
        return False


# Typing test event loop
while True:
    event, values = window.read(timeout=1)
    try:
        if verify_test(values['-INPUT-']):
            test_running = False
            test_done = True
            score = round(other_stuff.word_amount / (time_taken / 60))
            window['-TEXT-'].update(f"Nice! Your speed was {score} WPM.")
            window.read(timeout=1)
            time.sleep(2)
            window.close()
            break
    except TypeError:
        pass

    window['-TIMER-'].update(f"{round(time_taken, 1)} seconds")

    if event == '-OK-':
        if not verify_test(values['-INPUT-']):
            window['-TEXT-'].update("Oops! It looks like there is a mistake!")

    try:
        if len(values['-INPUT-']) > 0 and not test_done:
            test_running = True
    except TypeError:
        pass

    if not test_running:
        start_time = time.time()

    else:
        # noinspection PyUnboundLocalVariable
        time_taken = time.time() - start_time

    # End program if user presses the X icon
    if event == '-EXIT-' or event == sg.WIN_CLOSED:
        sys.exit()

window2 = sg.Window('Enter Initials', enter_name_layout, no_titlebar=False, grab_anywhere=False)

initials = ""

while True:
    event, values = window2.read()

    if event == '-OK-':
        if len(values['-INPUT-']) > 0:
            if values['-INPUT-'].isalpha():
                if len(values['-INPUT-']) == 2 or len(values['-INPUT-']) == 3:
                    initials = values['-INPUT-'].upper()
                    window2.close()
                    break
                window2['-TEXT-'].update("Can only be 2 or 3 letters")
                continue
            window2['-TEXT-'].update("Can only be letters")
            continue
        window2['-TEXT-'].update("Please enter your initials")
        continue

    # End program if user presses the X icon
    if event == '-EXIT-' or event == sg.WIN_CLOSED:
        sys.exit()

window3 = sg.Window('Leaderboard', leaderboard_layout, no_titlebar=False, grab_anywhere=False)

# update text file with initials and score
# dictionary 
# make a list of scores from text file
# sort list by score
# p1 = list[0], etc

# list of dictionaries


# get from file
# append current score
# sort scores
# put scores back in file
# profit

current_score = {'initials': initials, 'score': score}
scores = []

# get scores and append to scores list
with open(other_stuff.resource_path('scores.pkl'), 'rb') as f:
    try:
        while True:
            scores.append(pickle.load(f))
    except EOFError:
        f.close()

# append current score to score file and list
with open(other_stuff.resource_path('scores.pkl'), 'ab') as f:
    pickle.dump(current_score, f)
    scores.append(current_score)
    f.close()

# Thank you to https://stackoverflow.com/users/14796104/vibhu-upamanyu for
# this code that removes duplicate initials and sorts by the initial's
# highest score
dict_of_dict = dict()
for dic in scores:
    if dic['initials'] not in dict_of_dict:
        dict_of_dict[dic['initials']] = dic
    else:
        if dic['score'] > dict_of_dict[dic['initials']]['score']:
            dict_of_dict[dic['initials']] = dic

scores = list(dict_of_dict.values())

scores = sorted(scores, key=lambda k: k['score'])
scores.reverse()


def display_leaderboard(score_dict_list):
    for i, score_dict in enumerate(score_dict_list):
        if i < 10:
            window3[f'-P{i + 1}-'].update(f"{i + 1}: {scores[i]['initials']} - {scores[i]['score']} wpm")
    if len(score_dict_list) == 0:
        window3['-P1-'].update("Error: No scores to display!")


while True:
    event, values = window3.read(timeout=1)

    display_leaderboard(scores)

    if event == '-EXIT-' or event == sg.WIN_CLOSED:
        sys.exit()
