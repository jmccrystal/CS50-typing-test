from flask import Flask, jsonify
import pickle
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/get_scores', methods=['POST'])
def get_scores():
    if os.stat('online_leaderboard.pkl') == 0:
        return 'Error: No scores in leaderboard file!'
    data = []
    with open('online_leaderboard.pkl', 'rb') as f:
        try:
            while True:
                data.append(pickle.load(f))
        except EOFError:
            f.close()
    return jsonify(data)


@app.route('/add_score/<string:initials>/<int:score>', methods=['POST'])
def add_score(initials, score):
    current_score = {'initials': initials.upper(), 'score': score}
    if current_score['initials'] in ['CUM', 'DIC', 'DIK', 'LOL', 'LIT']:
        return 'Invalid initials!'
    with open('online_leaderboard.pkl', 'ab') as f:
        pickle.dump(current_score, f)
        f.close()
        return "Successfully added!"


@app.route('/remove_score/<string:initials>/<int:score>', methods=['POST'])
def remove_score(initials, score):
    data = []
    dict_to_remove = {'initials': initials.upper(), 'score': score}
    with open('online_leaderboard.pkl', 'rb') as f:
        try:
            while True:
                data.append(pickle.load(f))
        except EOFError:
            f.close()
    with open('online_leaderboard.pkl', 'wb') as f:
        for i, dictionary in enumerate(data):
            if dictionary == dict_to_remove:
                del data[i]
        for dictionary in data:
            pickle.dump(dictionary, f)
        f.close()
        return "Successfully removed!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2222, debug=True)
