class Board:
    """
    Class to represent the game board
    """

    def __init__(self, size):
        # Idea to use 2 boards per player, 1 to hold ships and 1 to hold
        # guesses from David Bowers project.
        # CREDIT: David Bowers
        # URL: https://github.com/dnlbowers/battleships
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
        row_num = 0

        # Idea to use print boards next to each other from David Bowers
        # project.
        # CREDIT: David Bowers
        # URL: https://github.com/dnlbowers/battleships
        combined_boards = list(zip(self.play_board, self.guess_board))

        # Code to use chars the label y axis
        # CREDIT: Pythondex Tutorial
        # URL: https://pythondex.com/python-battleship-game
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alphabet = alphabet[0 : len(combined_boards) + 1]

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
                print("\t", end="")
            row_num += 1
        print("\n")


new_test_board = Board(5)
new_test_board.print_board()
