from board import Board


class Player:
    # Smallest board size allowed in this implimentation
    board_size = 5

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @classmethod
    def set_board_size(cls, board_size):
        cls.board_size = board_size


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

# Take turns
print(player1.get_name())
player1.place_ships()
player1.board.print_board()

print(player2.get_name())
player2.place_ships()
player2.board.print_board()

print(player1.get_name())
player1.board.fire_missile(player2.board)
player1.board.print_board()

print(player2.get_name())
player2.board.fire_missile(player1.board)
player2.board.print_board()

print(player1.get_name())
player1.board.fire_missile(player2.board)
player1.board.print_board()

print(player2.get_name())
player2.board.fire_missile(player1.board)
player2.board.print_board()
