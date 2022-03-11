from .board import Board
import random


class Player:
    # Smallest board size allowed in this implimentation
    board_size = 0
    opponent = None

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @classmethod
    def set_board_size(cls, board_size):
        cls.board_size = board_size

    def set_opponent(self, opponent_object):
        self.opponent = opponent_object

    def fire_missile(self):
        self.board.fire_missile(self.opponent.board)


class HumanPlayer(Player):
    """
    class to represent a controlable human player
    """

    def __init__(self, name):
        self.board = Board(self.board_size)
        super().__init__(name)

    def place_ships(self):
        while True:
            place_ships_response = input(
                "Would you like to place ships manually or automatically? "
                "('m' for manual or 'a' for automatic)"
                "\n>> "
            )
            if place_ships_response != "" and place_ships_response in "MmAa":
                place_ships_response.lower()
                if place_ships_response == "m":
                    self.board.place_ships()
                else:
                    self.board.place_ships(automate_placement=True)
                break


class ComputerPlayer(Player):
    """
    class to represent an automated computer player
    """

    def __init__(self):
        self.board = Board(self.board_size, board_is_automated=True)
        super().__init__("Computer")

    def place_ships(self):
        self.board.place_ships()

    def fire_missile(self):
        result = False
        while result == False:
            x_coord = random.randint(0, self.board_size - 1)
            y_coord = random.randint(0, self.board_size - 1)
            result = self.board.fire_missile(
                self.opponent.board, x_coord, y_coord
            )
