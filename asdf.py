import pickle
import time

with open('words.txt', 'r') as f:
    qwert = f.read().split(', ')
    f.close()

with open('words', 'wb') as f:
    pickle.dump(qwert, f)
    f.close()

with open('words', 'rb') as f:
    try:
        while True:
            print(pickle.load(f))
    except EOFError:
        f.close()
time.sleep(11)
