import pickle
import sys
import time
import requests

import PySimpleGUI as sg

import layouts
import other_stuff
import server_ip


time_taken = 0

type_test_layout = layouts.type_test_layout
enter_name_layout = layouts.enter_name_layout
leaderboard_layout = layouts.leaderboard_layout
leaderboard_layout2 = layouts.leaderboard_layout2

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

banned_initials = ['NIG', 'FAG', 'FUC', 'FUK']

while True:
    event, values = window2.read()

    if event == '-OK-':
        if len(values['-INPUT-']) > 0:
            if values['-INPUT-'].isalpha():
                if len(values['-INPUT-']) == 2 or len(values['-INPUT-']) == 3:
                    if values['-INPUT-'].upper() not in banned_initials:
                        initials = values['-INPUT-'].upper()
                        window2.close()
                        break
                    window2['-TEXT-'].update("Initials not allowed")
                    continue
                window2['-TEXT-'].update("Can only be 2 or 3 letters")
                continue
            window2['-TEXT-'].update("Can only be letters")
            continue
        window2['-TEXT-'].update("Please enter your initials")
        continue

    # End program if user presses the X icon
    if event == '-EXIT-' or event == sg.WIN_CLOSED:
        sys.exit()

window3 = sg.Window('Your Scores', leaderboard_layout, no_titlebar=False, grab_anywhere=False)

# list of dictionaries, each dict has initials and score
current_score = {'initials': initials, 'score': score}
scores = [current_score]
current_player_scores = []

try:
    # get scores from server
    online_scores = requests.post(f'http://{server_ip.server_ip}/get_scores').json()

    # add current score to online database
    requests.post(f'http://{server_ip.server_ip}/add_score/{current_score["initials"]}/{current_score["score"]}')
except ConnectionError:
    print("No connection!")

for score in online_scores:
    scores.append(score)

for score in scores:
    print(score)

"""
# append scores from file into scores list
with open(other_stuff.resource_path('scores.pkl'), 'rb') as f:
    try:
        while True:
            scores.append(pickle.load(f))
    except EOFError:
        f.close()

# append current score from list into file
with open(other_stuff.resource_path('scores.pkl'), 'ab') as f:
    pickle.dump(current_score, f)
    scores.append(current_score)
    f.close()
"""

# append all scores with the same initials as current player into current_player_scores
for score in scores:
    if score['initials'] == current_score['initials']:
        current_player_scores.append(score)

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
# end of citation

current_player_scores = sorted(current_player_scores, key=lambda k: k['score'])
current_player_scores.reverse()


def display_leaderboard(score_dict_list, current_window):
    for i, score_dict in enumerate(score_dict_list):
        if i < 10:
            current_window[f'-P{i + 1}-'].update(
                f"{i + 1}: {score_dict_list[i]['initials']} - {score_dict_list[i]['score']} wpm")
    if len(score_dict_list) == 0:
        current_window['-P1-'].update("Error: No scores to display!")


end_loop = False

while True:
    event, values = window3.read(timeout=10)

    if not end_loop:
        display_leaderboard(current_player_scores, window3)
        end_loop = True

    if event == '-EXIT-' or event == sg.WIN_CLOSED:
        window3.close()
        break

end_loop = False
window4 = sg.Window('All Scores', leaderboard_layout2, no_titlebar=False, grab_anywhere=False)

while True:
    event, values = window4.read(timeout=10)

    if not end_loop:
        display_leaderboard(scores, window4)
        end_loop = True

    if event == '-EXIT-' or event == sg.WIN_CLOSED:
        sys.exit()
