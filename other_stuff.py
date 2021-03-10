# This file is for text generation and other variables
import pickle
import random
import output
import sys
import os

word_amount = 10

exit_icon = output.exit
ok_icon = output.ok


# not storing in onefile mode anymore, so no need for this function
# # Thanks to https://stackoverflow.com/users/1889973/max for this function
# # for using files in the binary
# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")
#
#     return os.path.join(base_path, relative_path)

def resource_path(relative_path):
    return os.path.join('.', relative_path)


with open(resource_path('words.pkl'), 'rb') as f:
    try:
        while True:
            words = pickle.load(f)
    except EOFError:
        f.close()


# Generate the random words from the list of words
def generate_test(num_of_words):
    return random.sample(words, num_of_words)


def list_to_string(input_string):
    output_string = " "
    return output_string.join(input_string)


type_test = list_to_string(generate_test(word_amount))
