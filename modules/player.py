from board import Board
from itertools import cycle


class Player:
    # Smallest board size allowed in this implimentation
    board_size = 5
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
        self.board.fire_missile(self.opponent)


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


# DEBUG

# Set Board Size
Player.set_board_size(5)

# Create Players
player1 = HumanPlayer("Test_Human")
player2 = ComputerPlayer()

# Set Player Opponents
player1.opponent = player2
player2.opponent = player1

players = [player1, player2]

turn = cycle(players)
fleet_destroyed = False
for player in players:
    current_player = next(turn)
    print(current_player.get_name())
    current_player.place_ships()

while fleet_destroyed == False:
    current_player = next(turn)
    print(current_player.get_name())
    current_player.board.print_board()
    current_player.board.fire_missile(current_player.opponent.board)
    current_player.board.print_board()
    fleet_destroyed = current_player.opponent.board.fleet.is_fleet_destroyed()
