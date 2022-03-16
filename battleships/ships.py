"""
Creates types of ships

Classes:

    Ship,
    AircraftCarrier,
    Battleship,
    Cruiser,
    Submarine,
    PatrolBoat
"""


class Ship:
    """
    A Class to represent a Ship

    ...

    Class Properties
    ---------------
    hit_count : int
        Number of time the ship has been hit

    Attributes
    ----------
    name : str
        Name/type of ship
    symbol : str
        Character symbol of ship
    length : int
        Length of ship

    Methods
    -------
    get_name():
        Returns the name of the Ship
    get_symbol():
        Returns the character that represents the Ship
    get_length():
        Returns the length of the Ship
    increment_hit_counter():
        Increments the hit count class property
    get_floatation_status():
        Returns the floatation status of the ship
    """

    hit_count = 0

    def __init__(self, name, symbol, length):
        """
        Constructs all the necessary attributes for the ship

        Args:
            name (str): Name/type of ship
            symbol (str): Character symbol of ship
            length (int): Length of ship
        """
        self.name = name
        self.symbol = symbol
        self.length = length

    def get_name(self):
        """
        Returns the name of the Ship

        Returns:
            str: Ship name
        """
        return self.name

    def get_symbol(self):
        """
        Returns the character that represents the Ship

        Returns:
            str: Character that represents the Ship
        """
        return self.symbol

    def get_length(self):
        """
        Returns the length of the Ship

        Returns:
            int: Length of the ship
        """
        return self.length

    def increment_hit_counter(self):
        """
        Increments the hit count class property
        """
        self.hit_count += 1

    def get_floatation_status(self):
        """
        Returns the floatation status of the ship

        Returns:
            (bool): Boolean result of equality check between the ship hit count
                    and its length
        """
        return False if self.hit_count == self.get_length() else True


class AircraftCarrier(Ship):
    """
    Class to represent an Aircraft Carrier, subclass of Ship
    """

    def __init__(self):
        super().__init__("Carrier", "A", 5)


class Battleship(Ship):
    """
    Class to represent a Battleship, subclass of Ship
    """

    def __init__(self):
        super().__init__("Battleship", "B", 4)


class Cruiser(Ship):
    """
    Class to represent a Cruiser, subclass of Ship
    """

    def __init__(self):
        super().__init__("Cruiser", "C", 3)


class Submarine(Ship):
    """
    Class to represent a Submarine, subclass of Ship
    """

    def __init__(self):
        super().__init__("Submarine", "S", 2)


class PatrolBoat(Ship):
    """
    Class to represent a Patrol Boat, subclass of Ship
    """

    def __init__(self):
        super().__init__("Patrol Boat", "P", 1)
