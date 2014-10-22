#!/usr/bin/env python3

##################
# Global Imports #
from flask import *
import numpy as np
import json

#################
# Local Imports #
import TTTBoard

########
# Code #

# Setting up the app
app = Flask(__name__)
app.debug = True

# Setting up the board
board = TTTBoard.Tic_Tac_Board("X", "O")

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

## Serving the home page.
#url_for("/", filename="home.html")

# Getting the state of the board.
@app.route("/api/pull/state", methods=["GET"])
def getState():
    over = board.game_over()
    if over:
        winner = board.check_both()
    else:
        winner = board.default_val

    resp = make_response(json.dumps({
        "over"  : over,
        "winner": winner,
        "turn"  : board.prompt_move(),
        "state" : np.ravel(board.board).tolist()
    }), 200)
    resp.headers["Content-Type"] = "application/json;charset=UTF-8"
    return resp

# Pushing a move to the board.
def runAI(board):
    return None # TODO: Implement a way to run the AI on the board.

@app.route("/api/push/move", methods=["POST"])
def postMove():
    if request.form["coord"] == None:
        return json.dumps({
            "error"  : True,
            "msg"    : "Not enough data.",
            "refresh": False
        })
    else:
        parsed = json.loads(request.form["coord"])
        if board.player_move(parsed["row"], parsed["col"], "X"):
            return json.dumps({
                "error"  : True,
                "msg"    : "Position is taken.",
                "refresh": False
            })
        else:
            runAI(board)
            return json.dumps({
                "error"  : False,
                "msg"    : "AI Updated.",
                "refresh": True
            })

# Starting the app.
app.run()
