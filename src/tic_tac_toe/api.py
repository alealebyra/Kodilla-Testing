from flask import Flask, abort, jsonify, request

from .utilities import tic_tac_toe_winner

app = Flask(__name__)

app.testing = True
client = app.test_client()


@app.route('/winner', methods=['GET'])
def winner():
    board = request.args.get('board', '').replace('_', ' ')
    try:
        return jsonify({
            'winner': tic_tac_toe_winner(board)
        })
    except ValueError:
        abort(400)
