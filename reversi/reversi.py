FIELD_WIDTH = 8


class InvalidCell(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"InvalidCell: {self.message}"
        else:
            return "InvalidCell"


class Reversi():
    def __init__(self):
        self.is_finished = False
        self.free_cells = 60
        self.field = [" " for i in range(64)]
        self.field[27] = "w"
        self.field[28] = "b"
        self.field[35] = "b"
        self.field[36] = "w"
        self.piece = " "
        self.current_player = "b"

    def turn(self):
        self.free_cells -= 1

    def check_up(self, cell):
        prev = False
        curr = self.field[cell]
        not_curr = "w" if curr == "b" else "b"
        for i in range(cell - FIELD_WIDTH, 0, -FIELD_WIDTH):
            up = self.field[i]
            if up == curr:
                return None
            if up == not_curr:
                prev = True
                continue
            if up == " " and prev is True:
                return i
            return None

    def check_down(self, cell):
        prev = False
        curr = self.field[cell]
        not_curr = "w" if curr == "b" else "b"
        for i in range(cell + FIELD_WIDTH, FIELD_WIDTH ** 2, FIELD_WIDTH):
            up = self.field[i]
            if up == curr:
                return None
            if up == not_curr:
                prev = True
                continue
            if up == " " and prev is True:
                return i
            return None

    def check_vertical(self, cell):
        moves = []
        up = self.check_up(cell)
        down = self.check_down(cell)
        if up is not None:
            moves.append(up)
        if down is not None:
            moves.append(down)
        return moves

    def check_left(self, cell):
        prev = False
        curr = self.field[cell]
        not_curr = "w" if curr == "b" else "b"
        first_in_row = 0
        for i in range(0, FIELD_WIDTH ** 2, FIELD_WIDTH):
            if cell < i:
                first_in_row = i - FIELD_WIDTH
                break
        for i in range(cell - 1, first_in_row - 1, -1):
            left = self.field[i]
            if left == curr:
                return None
            if left == not_curr:
                prev = True
                continue
            if left == " " and prev is True:
                return i
            return None
        return None

    def check_right(self, cell):
        prev = False
        curr = self.field[cell]
        not_curr = "w" if curr == "b" else "b"
        last_in_row = 0
        for i in range(0, FIELD_WIDTH ** 2, FIELD_WIDTH):
            if cell < i:
                last_in_row = i
                break
        for i in range(cell + 1, last_in_row + 1):
            left = self.field[i]
            if left == curr:
                return None
            if left == not_curr:
                prev = True
                continue
            if left == " " and prev is True:
                return i
            return None
        return None

    def check_horizontal(self, cell):
        moves = []
        left = self.check_left(cell)
        right = self.check_right(cell)
        if left is not None:
            moves.append(left)
        if right is not None:
            moves.append(right)
        return moves

    def next(self):
        if self.current_player == "b":
            pass
        else:
            self.current_player = "w"
        return self.current_player

    def make_turn(self, cell_idx, color):
        coverage = self.get_coverage(color)
        self.flip_pieces(cell_idx, coverage[cell_idx])

