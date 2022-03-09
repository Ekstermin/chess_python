from flask import Flask, jsonify, make_response  # , abort
import chess

figure_name = ("king", "queen", "rooks", "bishop", "knights", "pawns")
position_test = ("a", "b", "c", "d", "e", "f", "g", "h")


def check_position(arg_pos: str) -> bool:
    """Check if position is corect"""
    flag = False
    arg_position = arg_pos.lower()
    # print(arg_position)
    if len(arg_position) == 2:
        # print("długośc 2")
        try:
            if (
                arg_position[0] in position_test
                and int(arg_position[1]) > 0
                and int(arg_position[1]) < 9
            ):
                flag = True
        except ValueError:
            flag = False
    return flag


def check_figure(arg_fig: str) -> bool:
    flag = False
    if arg_fig.lower() in figure_name:
        flag = True
    else:
        flag = False
    return flag


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    body = ""
    with open("home.html", "r") as file:
        body = file.read()
    return body


# `curl http://localhost:8000/api/v1/rook/h2`
@app.route("/api/v1/<figure>/<pos>/", methods=["GET"])
def get_move(pos, figure):

    if check_figure(figure):
        if check_position(pos):
            # ("king", "queen", "rooks", "bishop", "knights", "pawns")
            if figure == "king":
                fig = chess.King(pos)
            elif figure == "queen":
                fig = chess.Queen(pos)
            elif figure == "rooks":
                fig = chess.Rooks(pos)
            elif figure == "bishop":
                fig = chess.Bishops(pos)
            elif figure == "knights":
                fig = chess.Knights(pos)
            elif figure == "pawns":
                fig = chess.Pawns(pos)

            output = make_response(
                jsonify(
                    {
                        "availableMoves": fig.list_available_moves(),
                        "currentField": fig.field,
                        "error": None,
                        "figure": figure,
                    }
                ),
                200,
            )
        else:
            output = make_response(
                jsonify(
                    {
                        "availableMoves": [],
                        "error": "Field does not exist.",
                        "figure": figure,
                        "currentField": pos,
                    }
                ),
                409,
            )
            # abort(409)
    else:

        output = make_response(
            jsonify(
                {
                    "availableMoves": [],
                    "error": "Figure does not exist.",
                    "figure": figure,
                    "currentField": pos,
                }
            ),
            404,
        )
        # abort(404)

    return output


# `curl http://localhost:8000/api/v1/rook/h2/h3`
@app.route("/api/v1/<figure>/<pos>/<move>", methods=["GET"])
def get_move_avaible(pos, figure, move):
    if check_figure(figure):
        if check_position(pos):
            if check_position(move):
                # ("king", "queen", "rooks", "bishop", "knights", "pawns")
                if figure == "king":
                    fig = chess.King(pos)
                elif figure == "queen":
                    fig = chess.Queen(pos)
                elif figure == "rooks":
                    fig = chess.Rooks(pos)
                elif figure == "bishop":
                    fig = chess.Bishops(pos)
                elif figure == "knights":
                    fig = chess.Knights(pos)
                elif figure == "pawns":
                    fig = chess.Pawns(pos)

                fig.validate_move(move)
                output = make_response(
                    jsonify(
                        {
                            "move": fig.validate_move(move),
                            "currentField": fig.field,
                            "error": None,
                            "figure": figure,
                            "destField": move,
                        }
                    ),
                    200,
                )
            else:
                # wrong position to move
                output = make_response(
                    jsonify(
                        {
                            "move": "invalid",
                            "figure": figure,
                            "error": "Current move is not permitted.",
                            "currentField": pos,
                            "destField": move,
                        }
                    ),
                    409,
                )

        else:
            # wrong position for figure
            output = make_response(
                jsonify(
                    {
                        "move": "invalid",
                        "figure": figure,
                        "error": "Field does not exist.",
                        "currentField": pos,
                        "destField": move,
                    }
                ),
                409,
            )
    else:
        # wrong figure name
        output = make_response(
            jsonify(
                {
                    "move": "invalid",
                    "figure": figure,
                    "error": "Figure does not exist.",
                    "currentField": pos,
                    "destField": move,
                }
            ),
            404,
        )
    return output


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


@app.errorhandler(500)
def server_error(error):
    return make_response(jsonify({"error": "Server failed"}), 500)


if __name__ == "__main__":
    app.run(debug=False)


# Unit test

# check valid position from URL argument
def test_check_position():
    assert check_position("a1")


def test_check_position_wrong():
    assert not check_position("Z1")


# check valid figure from URL argument
def test_check_figure():
    assert check_figure("king")


def test_check_figure_wrong():
    assert not check_figure("kingg")
