"""
Creates a player and holds information about the player and their board

Classes:

    Player,
    HumanPlayer,
    ComputerPlayer
"""
from .mixins import Mixins
from .board import Board


class Player:
    """
    Class to represent a player

    ...

    Class Properties
    ----------------
    board_size : int
        Number to represent both the height & width of the board
    opponent : None / object
        Player object representing this players opponent

    Attributes
    ----------
    name : str
        Name of player

    Methods
    -------
    get_name():
        Returns the player name
    set_board_size(board_size):
        Set the Class Property board_size
    set_opponent(player_object):
        Sets the players opponent
    place_ships():
        Call the board objects method to place ships in fleet
    fire_missile():
        Call the board objects method to fire a missile
    """

    board = None
    board_size = 0
    opponent = None

    def __init__(self, name):
        """
        Constructs all the necessary attributes for the player object

        Args:
            name (str): Name of player
        """
        self.name = name

    def get_name(self):
        """
        Returns the player name

        Returns:
            str: Player name
        """
        return self.name

    @classmethod
    def set_board_size(cls, board_size):
        """
        Set the Class Property board_size

        Args:
            board_size (int): Height / width of the board
        """
        cls.board_size = board_size

    def set_opponent(self, player_object):
        """
        Sets the players opponent

        Args:
            player_object (object): Object representing player's opponent
        """
        self.opponent = player_object

    def place_ships(self):
        """
        Call the board objects method to place a ship
        """
        self.board.place_ships()

    def fire_missile(self):
        """
        Call the board objects method to fire a missile
        """
        self.board.fire_missile(self.opponent.board)


class HumanPlayer(Player):
    """
    Class to represent a human controlled player

    ...

    Attributes
    ----------
    name : str
        Name of player

    Methods
    -------
    place_ships():
        Override the parent class place_ships method to provide interactivity
        for human controlled players. Prompts for (and validates) input used to
        determine if the fleet contents should be placed manually or
        automatically before calling a method of the board object
    """

    def __init__(self, name):
        """
        Constructs all the necessary attributes for a human controlled player

        Args:
            name (str): Name of player
        """
        # Initialise board
        self.board = Board(self.board_size)
        super().__init__(name)

    def place_ships(self):
        """
        Prompts for (and validates) input used to determine if the fleet
        contents should be placed manually or automatically before calling a
        method of the board object
        """
        # Input validation
        while True:
            Mixins.clear_terminal()
            place_ships_response = input(
                "\n"
                f"--- {self.get_name()} ---"
                "\n\n"
                "Would you like to place ships manually or automatically?\n"
                "('m' for manually or 'a' for automatically)"
                "\n>> "
            )
            if place_ships_response != "" and place_ships_response in "MmAa":
                place_ships_response = place_ships_response.lower()
                if place_ships_response == "m":
                    self.board.place_ships()
                else:
                    self.board.place_ships(automate_placement=True)
                break


class ComputerPlayer(Player):
    """
    Class to represent an automated player

    ...

    Attributes
    ----------
    None

    Methods
    -------
    fire_missile():
        Override the parent class fire_missile method to automate the turn.
        Create random coordinates by calling a method of the board object
        before passing these to the board objects fire_missile function
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for an automated player

        Args:
            none
        """
        # Initialise board
        self.board = Board(self.board_size, board_is_automated=True)
        super().__init__("Computer")

    def fire_missile(self):
        """
        Override the parent class fire_missile method to automate the turn.
        Create random coordinates by calling a method of the board object
        before passing these to the board objects fire_missile function
        """
        result = False
        # Input validation
        while result is False:
            x_coord, y_coord = self.board.generate_random_coordinates()
            result = self.board.fire_missile(
                self.opponent.board, x_coord, y_coord
            )
