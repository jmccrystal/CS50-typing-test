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
    with open('online_leaderboard.pkl', 'ab') as f:
        pickle.dump(current_score, f)
        f.close()
        return "Successfully added!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2222, debug=True)
