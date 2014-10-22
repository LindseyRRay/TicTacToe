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
    decoded = json.loads((request.data.decode("utf-8")))
    if decoded["row"] == None or decoded["col"] == None:
        myJson = json.dumps({
            "error"  : True,
            "msg"    : "Not enough data.",
            "refresh": False
        })
    else:
        if board.player_move(decoded["row"], decoded["col"], "X"):
            myJson = json.dumps({
                "error"  : True,
                "msg"    : "Position is taken.",
                "refresh": False
            })
        else:
            runAI(board)
            myJson = json.dumps({
                "error"  : False,
                "msg"    : "AI Updated.",
                "refresh": True
            })
    resp = make_response(myJson, 200)
    resp.headers["Content-Type"] = "application/json;charset=UTF-8"
    return resp

# Starting the app.
app.run()
