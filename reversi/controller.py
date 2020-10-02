class Controller():
    def __init__(self, game, player_one, player_two):
        self.game = game
        self.player_one = player_one
        self.player_two = player_two
        self.passes = 0

    def process_player(self, player, color):
        if self.game.get_coverage(color):
            cell_idx = player.get_input(self.game)
            self.game.make_turn(cell_idx, color)
        else:
            self.passes += 1

    def process(self):
        while True:
            self.passes = 0
            self.process_player(self.player_one, "b")
            self.process_player(self.player_two, "w")
            if self.passes == 2:
                break
        self.game.is_finished = True
