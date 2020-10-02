class ConsoleView():
    def __init__(self):
        self.line = "  ╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬"
        self.board_marking = "    a   b   c   d   e   f   g   h"

    def get_piece(self, cell):
        piece = " "
        if cell == "b":
            piece = "○"
        if cell == "w":
            piece = "●"
        return piece

    def update(self, game):
        print(self.board_marking)
        print(self.line)
        for j in range(8):
            print(j+1, end=" ")
            for i in range(8):
                piece = self.get_piece(game.field[i][j])
                print(f"║ {piece}", end=" ")
            print("║")
            print(self.line)
