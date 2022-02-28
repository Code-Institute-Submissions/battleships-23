from fleets import SmallFleet


class Board:
    """
    Class to represent the game board
    """

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, size):
        self.size = size
        # Idea to use 2 boards per player, 1 to hold ships and 1 to hold
        # guesses from David Bowers project.
        # CREDIT: David Bowers
        # URL: https://github.com/dnlbowers/battleships
        self.play_board = Board.create_board(size)
        self.guess_board = Board.create_board(size)
        self.small_fleet = SmallFleet()

    def create_board(size):
        """Creates a 2D list to represent the board

        Args:
            size (int): Number of items in each list, and the number of lists

        Returns:
            (list): 2D list to represent the board
        """
        return [[None for x in range(size)] for y in range(size)]

    def print_board(self):
        """Prints each row of the board on a separate line in the console"""
        row_num = 0

        # Idea to use print boards next to each other from David Bowers
        # project.
        # CREDIT: David Bowers
        # URL: https://github.com/dnlbowers/battleships
        combined_boards = list(zip(self.play_board, self.guess_board))

        # Code to use chars the label y axis
        # CREDIT: Pythondex Tutorial
        # URL: https://pythondex.com/python-battleship-game

        alphabet = self.alphabet[0 : len(combined_boards) + 1]

        for i in range(2):
            print("    ", end="")
            for column_num in range(1, len(combined_boards) + 1):
                print(f" {column_num}  ", end="")
            print("\t", end="")
        for combined_row in combined_boards:
            print("")
            for row in combined_row:
                print(f"{alphabet[row_num]}) |", end="")
                for item in row:
                    # print(item)
                    if item is None:
                        print(" - |", end="")
                print("\t", end="")
            row_num += 1
        print("\n")

    def place_ships(self):
        fleet = self.small_fleet.get_ships_in_fleet()
        for ship in fleet:
            # Get input from user regarding where ships should be placed

            print(
                f"You have {len(fleet)} ships left to place.\n"
                f"You are currently placing your '{ship.get_name()}' "
                f"which is '{ship.length}' grid spaces long.\n"
            )

            # TODO Input validation
            direction = input(
                "Please enter an orientation for your ship"
                " ('h' = horizontal, 'v' = vertical)\n>> "
            )

            start_x_coord = input(
                f"Enter Start x Coordinate (1 - " f"{self.size})\n>> "
            )
            start_x_coord = int(start_x_coord) - 1

            start_y__coord = input(
                f"Enter Start y Coord (a - "
                f"{self.alphabet[self.size-1]})\n>> "
            )
            print(type(start_y__coord))
            # Convert str to int and subtract 97 as that is the value of 'a',
            # 'b' is 98 and so on.
            start_y__coord = ord(start_y__coord) - 97
            print(direction, start_x_coord, type(start_y__coord))
            # TODO Position validation
            # TODO Add ship to board


new_test_board = Board(5)
new_test_board.print_board()
new_test_board.place_ships()
