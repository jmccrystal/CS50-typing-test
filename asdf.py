import pickle

with open('words.txt', 'r') as f:
    qwert = f.read().split(', ')
    f.close()

with open('words.pkl', 'wb') as f:
    pickle.dump(qwert, f)
    f.close()

with open('words.pkl', 'rb') as f:
    try:
        while True:
            print(pickle.load(f))
    except EOFError:
        f.close()
