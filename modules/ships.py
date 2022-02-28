class Ship:
    """
    Class to represent a Ship
    """

    def __init__(self, name, symbol, length):
        self.name = name
        self.symbol = symbol
        self.length = length

    def get_symbol(self):
        """Returns the character that represents the Ship

        Returns:
            str: Character that represents the Ship
        """
        return self.symbol

    def get_name(self):
        """Returns the name of the Ship

        Returns:
            str: Ship name
        """
        return self.name


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


sub = Submarine()
print(sub.__dict__)
help(sub)
