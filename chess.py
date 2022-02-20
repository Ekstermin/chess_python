from abc import ABC, abstractclassmethod

# ChessBoard  for emulate position
board = [
    ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"],  # 1
    ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],  # 2
    ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],  # 3
    ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],  # 4
    ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],  # 5
    ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],  # 6
    ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],  # 7
    ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],  # 8
]


def check_pos(position):
    for x in range(0, 8):
        if position in board[x]:
            # print(f"jest w {x}")
            pass
        else:
            continue
        return (x, board[x].index(position))


class Figure(ABC):
    def __init__(self, field: str) -> None:
        super().__init__()
        self.field = field

    jumps = ()

    @abstractclassmethod
    def list_available_moves(self) -> list:
        """abstract method return avaible moves, must be declare in childs"""
        pass

    @abstractclassmethod
    def validate_move(self, destination_field: str) -> bool:
        pass

    def validate(self, dest_field: str) -> bool:
        flag = None
        if dest_field in self.list_available_moves():
            flag = True
            # print("można się ruszyć")
        else:
            flag = False
            # print("nie można się ruszyć")
        return flag

    def check_pos(self) -> tuple:
        for x in range(0, 8):
            if self.field in board[x]:
                # print(f"jest w {x}")
                pass
            else:
                continue
            return (x, board[x].index(self.field))

    def moves(self, planed_moved: tuple) -> list:
        try:
            a, b = check_pos(self.field)
            # print(self.check_pos())
            # print(self.field)
            move = []
            for x, y in planed_moved:
                # print("a ", x + a, y + b)
                try:
                    xb = y + a
                    ya = x + b
                    if xb < 0 or ya < 0:
                        # print("poza szachownicą if {xa} {yb}")
                        pass
                    else:
                        move.append(board[xb][ya])
                except Exception:
                    # print(f"poza szachownicą {x} ,{y}")
                    continue
        except TypeError:
            move = []
        return move


class King(Figure):
    def __init__(self, field: str):
        super().__init__(field)

    jumps = (
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
    )

    def list_available_moves(self):
        return self.moves(self.jumps)

    def validate_move(self, dest_field: str):
        return self.validate(dest_field)


class Queen(Figure):
    def __init__(self, field: str):
        super().__init__(field)

    jumps = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (-1, 1),
        (-2, 2),
        (-3, 3),
        (-4, 4),
        (-5, 5),
        (-6, 6),
        (-7, 7),
        (1, -1),
        (2, -2),
        (3, -3),
        (4, -4),
        (5, -5),
        (6, -6),
        (7, -7),
        (-1, -1),
        (-2, -2),
        (-3, -3),
        (-4, -4),
        (-5, -5),
        (-6, -6),
        (-7, -7),
        (0, -1),
        (0, -2),
        (0, -3),
        (0, -4),
        (0, -5),
        (0, -6),
        (0, -7),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 0),
        (6, 0),
        (7, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
        (0, 6),
        (0, 7),
        (-1, 0),
        (-2, 0),
        (-3, 0),
        (-4, 0),
        (-5, 0),
        (-6, 0),
        (-7, 0),
    )

    def list_available_moves(self):
        return self.moves(self.jumps)

    def validate_move(self, dest_field: str):
        return self.validate(dest_field)


class Rooks(Figure):
    def __init__(self, field: str):
        super().__init__(field)

    jumps = (
        (0, -1),
        (0, -2),
        (0, -3),
        (0, -4),
        (0, -5),
        (0, -6),
        (0, -7),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 0),
        (6, 0),
        (7, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
        (0, 6),
        (0, 7),
        (-1, 0),
        (-2, 0),
        (-3, 0),
        (-4, 0),
        (-5, 0),
        (-6, 0),
        (-7, 0),
    )

    def list_available_moves(self):
        return self.moves(self.jumps)

    def validate_move(self, dest_field: str):
        return self.validate(dest_field)


class Bishops(Figure):
    def __init__(self, field: str):
        super().__init__(field)

    jumps = (
        (1, -1),
        (2, -2),
        (3, -3),
        (4, -4),
        (5, -5),
        (6, -6),
        (7, -7),  # left up
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),  # right up
        (-1, 1),
        (-2, 2),
        (-3, 3),
        (-4, 4),
        (-5, 5),
        (-6, 6),
        (-7, 7),  # right down
        (-1, -1),
        (-2, -2),
        (-3, -3),
        (-4, -4),
        (-5, -5),
        (-6, -6),
        (-7, -7),
    )  # left down

    def list_available_moves(self):
        return self.moves(self.jumps)

    def validate_move(self, dest_field: str):
        return self.validate(dest_field)


class Knights(Figure):
    def __init__(self, field: str):
        super().__init__(field)

    jumps = (
        (-2, 1),
        (-1, 2),
        (1, 2),
        (2, 1),
        (2, -1),
        (1, -2),
        (-1, -2),
        (-2, -1),
    )

    def list_available_moves(self):
        return self.moves(self.jumps)

    def validate_move(self, dest_field: str):
        return self.validate(dest_field)


class Pawns(Figure):
    def __init__(self, field: str):
        super().__init__(field)

    jumps = ((1, -1), (1, 0), (1, 1))
    jumps2 = ((2, 0),)

    def list_available_moves(self):
        # print(self.check_pos())
        moves = []
        if self.check_pos()[0] == 1:
            # moves.extend(self.moves())
            moves.extend(self.moves(self.jumps2))
            moves.extend(self.moves(self.jumps))
        elif self.check_pos()[0] == 0:
            moves = None
        else:
            moves.extend(self.moves(self.jumps))
        return moves

    def validate_move(self, dest_field: str):
        return self.validate(dest_field)


# king = King("g7g")
# queen = Queen("d4")
# rooks = Rooks("h3")
# bishop = Bishops("c4")
# knights = Knights("d4")
# pawns = Pawns("c3")


# print(king.check_pos())
# print("król")

# print(king.field)
# print(king.list_available_moves())
# print(king.validate_move("g6"))
# print(king.validate_move("g5"))
# print("----------------------------\n")

# print("królowa")
# print(queen.field)
# print(queen.list_available_moves())
# print(queen.validate_move("g4"))
# print(queen.validate_move("e8"))
# print("----------------------------\n")

# print("wierza")
# print(rooks.field)
# print(rooks.list_available_moves())
# print(rooks.validate_move("b3"))
# print(rooks.validate_move("b4"))
# print("----------------------------\n")

# print("goniec")
# print(bishop.field)
# print(bishop.list_available_moves())
# print(bishop.validate_move("f7"))
# print(bishop.validate_move("e1"))
# print("----------------------------\n")

# print("koń")
# print(knights.field)
# print(knights.list_available_moves())
# print(knights.validate_move("e2"))
# print(knights.validate_move("c5"))
# print("----------------------------\n")

# print("pionek")
# print(pawns.field)
# print(pawns.list_available_moves())
# print(pawns.validate_move("c4"))
# print(pawns.validate_move("d2"))
# print("----------------------------\n")
