class Ship:
    """
    Class to represent a Ship
    """

    hit_count = 0

    def __init__(self, name, symbol, length):
        self.name = name
        self.symbol = symbol
        self.length = length

    def get_name(self):
        """Returns the name of the Ship

        Returns:
            str: Ship name
        """
        return self.name

    def get_symbol(self):
        """Returns the character that represents the Ship

        Returns:
            str: Character that represents the Ship
        """
        return self.symbol

    def get_length(self):
        """Returns the character that represents the Ship

        Returns:
            str: Character that represents the Ship
        """
        return self.length

    def increment_hit_counter(self):
        self.hit_count += 1

    def get_floatation_status(self):
        return False if self.hit_count == self.get_length() else True


class Battleship(Ship):
    """
    Class to represent a Battleship, subclass of Ship
    """

    def __init__(self):
        super().__init__("Battleship", "B", 4)


class Submarine(Ship):
    """
    Class to represent a Submarine, subclass of Ship
    """

    def __init__(self):
        super().__init__("Submarine", "S", 2)
