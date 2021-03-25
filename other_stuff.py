# This file is for text generation and other variables
import pickle
import random
import output
import os

word_amount = 10

exit_icon = output.exit
ok_icon = output.ok


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
