class Board:
    """
    Class to represent the game board
    """

    def __init__(self, size):
        # Idea to use 2 boards per player, 1 to hold ships and 1 to hold
        # guesses from David Bowers project.
        # CREDIT: David Bowers URL:
        # https://github.com/dnlbowers/battleships
        self.play_board = Board.create_board(size)
        self.guess_board = Board.create_board(size)

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
        for row in self.play_board:
            print(row)


new_test_board = Board(5)
new_test_board.print_board()
