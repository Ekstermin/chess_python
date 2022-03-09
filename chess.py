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
            print(a, b)
            print(self.check_pos())
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
                except IndexError:
                    # print(f"poza szachownicą {x} ,{y}")
                    # print(e.with_traceback)
                    move = []
                    continue

        except TypeError:
            # print(e)
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

    jumps = ((-1, 1), (0, 1), (1, 1))
    jumps2 = ((0, 2),)

    def list_available_moves(self):
        # print(self.check_pos())
        moves = []
        try:
            if self.check_pos()[0] == 1:
                # moves.extend(self.moves())
                moves.extend(self.moves(self.jumps2))
                moves.extend(self.moves(self.jumps))
            elif self.check_pos()[0] == 0:
                moves = None
            else:
                moves.extend(self.moves(self.jumps))
        except TypeError:
            # move = [] return emty list if type error for wrong position
            pass
        return moves

    def validate_move(self, dest_field: str):
        return self.validate(dest_field)


# Unit tests, are pasten on the end file becaus is small modu module.
# #Tested main function because they have error handling


class TestKing:
    def test_create_King(self):
        king = King("a1")
        assert king.field == "a1"
        assert isinstance(king, King)

    def test_list_available_moves(self):
        king = King("a1")
        list_move = king.list_available_moves()
        assert len(list_move) > 0
        assert type(list_move) is list
        assert "a2" in list_move

    def test_list_available_moves_bad(self):
        king = King("a1a")
        list_move = king.list_available_moves()
        assert len(list_move) == 0
        assert type(list_move) is list

    def test_validate_move(self):
        king = King("a1")
        assert king.validate_move("a2")

    def test_validate_move_false(self):
        king = King("a1")
        assert not king.validate_move("a3")
        assert not king.validate_move("a3a")


class TestQueen:
    def test_create_Queen(self):
        queen = Queen("a1")
        assert queen.field == "a1"
        assert isinstance(queen, Queen)

    def test_list_available_moves(self):
        queen = Queen("a1")
        list_move = queen.list_available_moves()
        assert len(list_move) > 0
        assert type(list_move) is list
        assert "a4" in list_move

    def test_list_available_moves_bad(self):
        queen = Queen("a1a")
        list_move = queen.list_available_moves()
        assert len(list_move) == 0
        assert type(list_move) is list

    def test_validate_move(self):
        queen = Queen("a1")
        assert queen.validate_move("a2")

    def test_validate_move_false(self):
        queen = Queen("a1")
        assert not queen.validate_move("b3")
        assert not queen.validate_move("b3b")


class TestRooks:
    def test_create_Rooks(self):
        rooks = Rooks("a1")
        assert rooks.field == "a1"
        assert isinstance(rooks, Rooks)

    def test_list_available_moves(self):
        rooks = Rooks("a1")
        list_move = rooks.list_available_moves()
        assert len(list_move) > 0
        assert type(list_move) is list
        assert "a4" in list_move

    def test_list_available_moves_bad(self):
        rooks = Rooks("a1a")
        list_move = rooks.list_available_moves()
        assert len(list_move) == 0
        assert type(list_move) is list

    def test_validate_move(self):
        rooks = Rooks("a1")
        assert rooks.validate_move("a2")

    def test_validate_move_false(self):
        rooks = Rooks("a1")
        assert not rooks.validate_move("b3")
        assert not rooks.validate_move("b3b")


class TestBishops:
    def test_create_Bishops(self):
        bishops = Bishops("a1")
        assert bishops.field == "a1"
        assert isinstance(bishops, Bishops)

    def test_list_available_moves(self):
        bishops = Bishops("a1")
        list_move = bishops.list_available_moves()
        assert len(list_move) > 0
        assert type(list_move) is list
        assert "c3" in list_move

    def test_list_available_moves_bad(self):
        bishops = Bishops("a1a")
        list_move = bishops.list_available_moves()
        assert len(list_move) == 0
        assert type(list_move) is list

    def test_validate_move(self):
        bishops = Bishops("a1")
        assert bishops.validate_move("b2")

    def test_validate_move_false(self):
        bishops = Bishops("a1")
        assert not bishops.validate_move("b3")
        assert not bishops.validate_move("b3b")


class TestKnights:
    def test_create_Knights(self):
        knights = Knights("d4")
        assert knights.field == "d4"
        assert isinstance(knights, Knights)

    def test_list_available_moves(self):
        knights = Knights("d4")
        list_move = knights.list_available_moves()
        assert len(list_move) > 0
        assert type(list_move) is list
        assert "b3" in list_move

    def test_list_available_moves_bad(self):
        knights = Knights("a1a")
        list_move = knights.list_available_moves()
        assert len(list_move) == 0
        assert type(list_move) is list

    def test_validate_move(self):
        knights = Knights("d4")
        assert knights.validate_move("e2")

    def test_validate_move_false(self):
        knights = Knights("d4")
        assert not knights.validate_move("b4")
        assert not knights.validate_move("b3b")


class TestPawns:
    def test_create_Pawns(self):
        pawns = Pawns("b2")
        assert pawns.field == "b2"
        assert isinstance(pawns, Pawns)

    def test_list_available_moves(self):
        pawns = Pawns("b2")
        list_move = pawns.list_available_moves()
        assert len(list_move) > 0
        assert type(list_move) is list
        assert "b4" in list_move

    def test_list_available_moves_second(self):
        pawns = Pawns("b3")
        list_move = pawns.list_available_moves()
        assert len(list_move) > 0
        assert type(list_move) is list
        assert "b4" in list_move

    def test_list_available_moves_bad(self):
        pawns = Pawns("a1a")
        list_move = pawns.list_available_moves()
        assert len(list_move) == 0
        assert type(list_move) is list

    def test_validate_move(self):
        pawns = Pawns("b2")
        assert pawns.validate_move("c3")

    def test_validate_move_false(self):
        pawns = Pawns("b2")
        assert not pawns.validate_move("b5")
        assert not pawns.validate_move("b3b")
