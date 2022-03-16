"""
Creates a fleet of ships imported from the ships module

Classes:

    Fleet,
    Small_Fleet,
    Large_Fleet
"""
from .ships import *


class Fleet:
    """
    A Class to represent a fleet


    Attributes
    ----------
    fleet : None
        Variable to contain a fleet

    Methods
    -------
    get_ships_in_fleet():
        Returns the fleet variable

    get_num_ships_remaining():
        Returns the number of ship objects in fleet still afloat
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for a fleet
        """
        self.fleet = None

    def get_ships_in_fleet(self):
        """Gets all ship objects in fleet

        Returns:
            list: List of Ship objects
        """
        return self.fleet

    def get_num_ships_remaining(self):
        """Gets the number of ship objects in fleet still afloat

        Returns:
            int: Number of Ship objects
        """
        number_of_ships = 0
        for ship in self.fleet:
            if ship.get_floatation_status() is True:
                number_of_ships += 1
        return number_of_ships


class SmallFleet(Fleet):
    """
    Class to represent a small fleet of ships

    1 x Battleship
    2 x Submarines
    1 x PatrolBoat
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for a small fleet
        """
        self.ship1 = Battleship()
        self.ship2 = Submarine()
        self.ship3 = Submarine()
        self.ship4 = PatrolBoat()
        self.fleet = [self.ship1, self.ship2, self.ship3, self.ship4]


class LargeFleet(Fleet):
    """
    Class to represent a large fleet of ships

    1 x Aircraft Carrier
    1 x Battleship
    2 x Cruisers
    2 x Submarines
    1 x PatrolBoat
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for a large fleet
        """
        self.ship1 = AircraftCarrier()
        self.ship2 = Battleship()
        self.ship3 = Cruiser()
        self.ship4 = Cruiser()
        self.ship5 = Submarine()
        self.ship6 = Submarine()
        self.ship7 = PatrolBoat()
        self.fleet = [
            self.ship1,
            self.ship2,
            self.ship3,
            self.ship4,
            self.ship5,
            self.ship6,
            self.ship7,
        ]
