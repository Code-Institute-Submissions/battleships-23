class Ship:
    def __init__(self, name, symbol, length):
        self.name = name
        self.symbol = symbol
        self.length = length

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name


class Battleship(Ship):
    def __init__(self):
        super().__init__("Battleship", "B", 4)


class Submarine(Ship):
    def __init__(self):
        super().__init__("Submarine", "S", 2)


sub = Submarine()
print(sub.__dict__)
help(sub)
