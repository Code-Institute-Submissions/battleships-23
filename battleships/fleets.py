from .ships import *


class Fleet:
    """Class to held metods for fleets"""

    def __init__(self):
        self.fleet = None

    def get_ships_in_fleet(self):
        """Returns all the ship objects from the fleet

        Returns:
            list: List of Ship objects
        """
        return self.fleet

    def is_fleet_destroyed(self):
        for ship in self.fleet:
            if ship.get_floatation_status() == True:
                return False
        return True


class SmallFleet(Fleet):
    """
    Class to represent a small fleet of ships

    1 x Battleship
    2 x Submarines
    1 x PatrolBoat
    """

    def __init__(self):
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
