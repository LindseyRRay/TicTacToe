#!/usr/bin/env python3

##################
# Global Imports #
from flask import *
import numpy as np
import json

#################
# Local Imports #
import minimax as m
import board as b

########
# Code #

# Setting up the app
app = Flask(__name__)
app.debug = True

# Setting up the board
board = b.Board()

# Serving the home page.
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

# Getting the state of the board.
@app.route("/api/pull/state", methods=["GET"])
def getState():
    over = board.isGameOver()
    if over:
        winner = board.findWinner()
    else:
        winner = board.nil

    resp = make_response(json.dumps({
        "over"  : over,
        "winner": winner,
        "turn"  : board.whoseMove(),
        "state" : np.ravel(board.board).tolist()
    }), 200)
    resp.headers["Content-Type"] = "application/json;charset=UTF-8"
    return resp

# Pushing a move to the board.
def runAI(board):
    if board.whoseMove() == board.p2:

        pos, _, _ = m.Optimal_Game_Strategy(board)

        board.performMove(pos[0], pos[1], board.p2)
        return True
    return False

@app.route("/api/push/move", methods=["POST"])
def postMove():
    decoded = json.loads((request.data.decode("utf-8")))

    decoded["row"] = int(decoded["row"])
    decoded["col"] = int(decoded["col"])

    if decoded["row"] == None or decoded["col"] == None:
        myJson = json.dumps({
            "error"  : True,
            "msg"    : "Not enough data.",
            "refresh": False
        })
    else:

        if board.isGameOver():
            myJson = json.dumps({
                "error": True,
                "msg": "Game Over",
                "refresh": True})

        elif not board.performMove(decoded["row"], decoded["col"], board.p1):
            myJson = json.dumps({
                "error"  : True,
                "msg"    : "Position is taken.",
                "refresh": False
            })
        else:
            if not runAI(board):
                myJson = json.dumps({
                    "error"  : True,
                    "msg"    : "This shouldn't be happening.",
                    "refresh": False
                })
            else:
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
