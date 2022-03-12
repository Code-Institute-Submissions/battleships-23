from .fleets import SmallFleet, LargeFleet
from .ships import Ship
from .mixins import Mixins
from time import sleep
import random


class Board:
    """
    Class to represent the game board
    """

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, size, board_is_automated=False):
        self.size = size
        # Idea to use 2 boards per player, 1 to hold ships and 1 to hold
        # guesses from David Bowers project.
        # CREDIT: David Bowers
        # URL: https://github.com/dnlbowers/battleships
        self.play_board = Board.create_board(size)
        self.guess_board = Board.create_board(size)
        if self.size == 5:
            self.fleet = SmallFleet()
        elif self.size == 9:
            self.fleet = LargeFleet()
        self.board_is_automated = board_is_automated

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

        alphabet = self.alphabet[0:len(combined_boards) + 1]

        print("")
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
                    elif item == "MISS":
                        print(" 0 |", end="")
                    elif item == "HIT":
                        print(" X |", end="")
                    else:
                        print(" " + item.get_symbol() + " |", end="")
                print("\t", end="")
            row_num += 1
        print("\n")

    def place_ships(self, automate_placement=False):
        fleet = self.fleet.get_ships_in_fleet()
        ship_placements_remaining = len(fleet)
        Mixins.clear_terminal()
        for ship in fleet:
            while True:
                # If board functions (or specifically the placement of ships)
                # are automated then generate random input, else display board
                # and prompt for input.
                if self.board_is_automated or automate_placement:
                    direction = random.choice(["h", "v"])
                    start_x_coord = random.randint(0, self.size - 1)
                    start_y_coord = random.randint(0, self.size - 1)
                else:
                    self.print_board()
                    # Present information to user regarding current ship to be
                    # placed
                    print(
                        f"You have {ship_placements_remaining} "
                        "ships left to place."
                        "\n\n"
                        "You are currently placing your "
                        f"'{ship.get_name()}' "
                        f"which is '{ship.length}' grid spaces long.\n"
                    )

                    # Functions which prompt for and validate user input
                    # regarding ship placement
                    direction = self.prompt_for_ship_direction()
                    (
                        start_x_coord,
                        start_y_coord,
                    ) = self.prompt_for_coordinates()

                # Create a list of coordinates the ship will occupy on the
                # board, its position.
                ship_position = self.create_ship_position_coords(
                    direction, start_x_coord, start_y_coord, ship.get_length()
                )

                # Check if each of the coordinates the ship would occupy
                # are empty and within the bounds of the board size.
                is_ship_position_valid = self.check_valid_position(
                    ship_position
                )

                # If valid, place the ship on the board, else inform the
                # user why.
                if is_ship_position_valid is True:
                    self.add_ship_to_board(ship_position, ship)
                    Mixins.clear_terminal()
                    break
                else:
                    # If board functions (or specifically the placement of
                    # ships) are automated the do not print feedback.
                    if self.board_is_automated or automate_placement:
                        continue
                    else:
                        Mixins.clear_terminal()
                        print(is_ship_position_valid)

            ship_placements_remaining -= 1

    def prompt_for_ship_direction(self):
        while True:
            direction = input(
                "Please enter an orientation for your ship"
                " ('h' = horizontal, 'v' = vertical)\n>> "
            )
            if direction != "" and direction in "HVhv":
                direction = direction.lower()
                print("")
                return direction
            else:
                continue

    def prompt_for_coordinates(self):
        x_coord = 0
        y_coord = 0

        while True:
            x_coord = input(
                f"Enter Start x Coordinate (1 - " f"{self.size})\n>> "
            )
            try:
                x_coord = int(x_coord)
            except ValueError:
                print("Invalid Input! Please enter a number.")
                continue
            if x_coord >= 1 and x_coord <= self.size:
                x_coord = x_coord - 1
                break
            else:
                print(
                    "Invalid Input! "
                    "Please enter a number in the range specified."
                )
        print("")

        while True:
            y_coord = input(
                f"Enter Start y Coord (a - "
                f"{self.alphabet[self.size-1]})\n>> "
            )
            try:
                y_coord = y_coord.lower()
                # Convert string to its Unicode to return the integer value and
                # subtract 97 as that is the value of 'a', 'b' is 98 and so on.
                y_coord = ord(y_coord) - 97
            except TypeError:
                print("Invalid Input! Please enter a letter.")
                continue
            if y_coord >= 0 and y_coord <= self.size - 1:
                break
            else:
                print(
                    "Invalid Input! "
                    "Please enter a letter in the range specified."
                )

        return x_coord, y_coord

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

        if direction == "h":
            for i in range(0, ship_length):
                ship_coords.append([start_y__coord, start_x_coord + i])
        elif direction == "v":
            for i in range(0, ship_length):
                ship_coords.append([start_y__coord + i, start_x_coord])
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
                        f"The selected position overlaps your "
                        f"{self.play_board[x][y].get_name()}. "
                        "Please try again..\n"
                    )
                    break
            except IndexError as e:
                # Out of range
                valid_placement = (
                    "The selected position would put the ship out of bounds. "
                    "Please try again..\n"
                )
                break
        return valid_placement

    def add_ship_to_board(self, input_array, ship):
        for x, y in input_array:
            self.play_board[x][y] = ship

    def fire_missile(self, opponents_board, input_x_coord=0, input_y_coord=0):
        while True:
            if self.board_is_automated:
                x_coord = input_x_coord
                y_coord = input_y_coord
            else:

                (
                    x_coord,
                    y_coord,
                ) = self.prompt_for_coordinates()

            valid_position = self.check_valid_position([[y_coord, x_coord]])

            if valid_position is True or "position overlaps" in valid_position:
                # Check guess is original
                if self.guess_board[y_coord][x_coord] is not None:
                    if self.board_is_automated:
                        # Return False to prompt the Computer Player to
                        # generate another guess
                        return False
                    else:
                        print(
                            "You have previously launched a missile here. "
                            "Please try again.\n"
                        )
                else:
                    break

        # Check the opponent's play board
        fire_missile_result = opponents_board.check_if_hit(x_coord, y_coord)
        if fire_missile_result == "MISS":
            self.update_guess_board(x_coord, y_coord, fire_missile_result)
        elif fire_missile_result == "HIT" or fire_missile_result == "SUNK":
            self.update_guess_board(x_coord, y_coord, "HIT")
        print(f"\n{(fire_missile_result).capitalize()}!")
        sleep(2)
        # Return True to break the input loop in the Player Class as the
        # Computer Player guess was valid
        return True

    def check_if_hit(self, x_coord, y_coord):
        shot_result = self.play_board[y_coord][x_coord]
        if isinstance(shot_result, Ship):
            shot_result.increment_hit_counter()
            return "HIT" if shot_result.get_floatation_status() else "SUNK"
        else:
            return "MISS"

    def update_guess_board(self, x_coord, y_coord, guess_result):
        self.guess_board[y_coord][x_coord] = guess_result
