from fleets import SmallFleet
from ships import Ship


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
                    else:
                        print(" " + item.get_symbol() + " |", end="")
                print("\t", end="")
            row_num += 1
        print("\n")

    def place_ships(self):
        fleet = self.small_fleet.get_ships_in_fleet()
        ship_placements_remaining = len(fleet)

        for ship in fleet:
            self.print_board()

            # Get input from user regarding where ships should be placed
            print(
                f"You have {ship_placements_remaining} ships left to place.\n"
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
            # Convert str to int and subtract 97 as that is the value of 'a',
            # 'b' is 98 and so on.
            start_y__coord = ord(start_y__coord) - 97

            ship_position = self.create_ship_position_coords(
                direction, start_x_coord, start_y__coord, ship.length
            )

            is_ship_position_valid = self.check_valid_position(ship_position)

            if is_ship_position_valid is True:
                self.add_ship_to_board(ship_position, ship)
            else:
                print(is_ship_position_valid)

            ship_placements_remaining -= 1

    def create_ship_position_coords(
        self, direction, start_x_coord, start_y__coord, ship_length
    ):
        """Creates list of ship coords to be used in testing

        Args:
            direction (str): Horizontal ('l') or vertical ('d') axis
            start_x_coord (int): X coordinate to start from
            start_y__coord (int): Y coordinate to start from
            ship_length (int): Length of ship

        Returns:
            list: 2D list of coordinates to represent the placement of the
            ship
        """
        ship_coords = []

        if direction == "d":
            for i in range(0, ship_length):
                ship_coords.append([start_y__coord + i, start_x_coord])
        else:
            for i in range(0, ship_length):
                ship_coords.append([start_y__coord, start_x_coord + i])
        return ship_coords

    def check_valid_position(self, input_array):
        """
        Checks if coords (passed as a list) are empty and in-bounds
        """
        valid_placement = False
        for x, y in input_array:
            try:
                if self.play_board[x][y] is None:
                    valid_placement = True
                elif isinstance(self.play_board[x][y], Ship):
                    # Ship collision detected
                    valid_placement = (
                        f"Placement overlaps "
                        f"{self.play_board[x][y].get_name()}. "
                        "Please try again..\n"
                    )
                    break
            except IndexError as e:
                # Out of range
                valid_placement = (
                    "Selected position would put the ship out of bounds. "
                    "Please try again..\n"
                )
                break
        return valid_placement

    def add_ship_to_board(self, input_array, ship):
        for x, y in input_array:
            self.play_board[x][y] = ship


new_test_board = Board(5)
new_test_board.place_ships()
