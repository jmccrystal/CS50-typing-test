# This file is for text generation and other variables
import pickle
import random
import output

word_amount = 20

exit_icon = output.exit
ok_icon = output.ok


with open('words', 'rb') as f:
    try:
        while True:
            words = pickle.load(f)
    except EOFError:
        f.close()


# Generate the random words from the list of words
def generate_test(num_of_words):
    return random.sample(words, num_of_words)


type_test = generate_test(word_amount)


def list_to_string(input_string):
    output_string = " "
    return output_string.join(input_string)
