from .ships import Battleship, Submarine


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
    Class to represent a small collection of ships

    1 x Battleship
    2 x Submarines
    """

    def __init__(self):
        self.ship1 = Battleship()
        self.ship2 = Submarine()
        self.ship3 = Submarine()
        self.fleet = [self.ship1, self.ship2, self.ship3]


class LargeFleet(Fleet):
    """
    Class to represent a large collection of ships
    """

    # TODO Implement large fleet

    def __init__(self):
        pass
