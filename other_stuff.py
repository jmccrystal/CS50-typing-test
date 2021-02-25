import random
import output

word_amount = 50

exit = output.exit
ok = output.ok

def get_words():
    with open("words.txt", "r") as file:
        return file.read().split(', ')

words = get_words()

# Generate the random words from the list of words
def generate_test(num_of_words):
    return random.sample(words, num_of_words)

typetest = generate_test(word_amount)

def list_to_string(input_string):
    output_string = " "  
    return (output_string.join(input_string)) 

if __name__ == "__main__":
    print(typetest)
