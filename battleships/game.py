"""
Creates a game class to run the logic or flow of the game

Classes:

    Game
"""
from .player import Player, HumanPlayer, ComputerPlayer
from .mixins import Mixins
from itertools import cycle
from time import sleep
import random
import pyfiglet


class Game:
    """
    A Class to represent a Ship

    ...

    Class Properties
    ----------------
    user_choice : int
        Number of times the ship has been hit
    player1 : None / object
        Player object representing player 1
    player2 : None / object
        Player object representing player 2
    player_turn_order : object (itertools.cycle)
        itertools.cycle object to be used to represent turn order
    human_players_only : bool
        Boolean to represent if the game is being player by 2 human players

    Attributes
    ----------
    none

    Methods
    -------
    new_game():
        Prints the welcome screen and prompts for (and validates) input to
        start game
    display_instructions():
        Prints the instructions and prompts for input to return to welcome
        screen
    set_board_size():
        Prompts for (and validates) input which will be used to set the size of
        the board
    set_players():
        Prompts for (and validates) input used to determine the type of players
        and creates instances of the Player class
    request_player_name(player_num):
        Given the number of the player (1 or 2), prompts for, validates and
        returns user input to represent the players name
    set_play_order():
        Prompts for (and validates) input used to simulate a coin toss to
        determine the play order and returns this expressed as an
        itertools.cycle object
    placement_phase():
        Run the ship placement phase of the game and prompts for input before
        starting if their are only human players
    firing_phase():
        Run the firing phase of the game, simulating this if a computer player
        or calling methods from other objects to display the board and
        information to the player
    game_over(winner):
        Prints the name of the passed player object and prompts the player if
        they would like to play again
    """

    user_choice = ""
    player1 = None
    player2 = None
    player_turn_order = None
    human_players_only = False

    def new_game(self):
        """
        Prints the welcome screen and prompts for (and validates) input to
        start game
        """
        Mixins.clear_terminal()
        print(pyfiglet.figlet_format("Welcome to\nBattleships!", font="slant"))
        self.user_choice = ""
        # Input validation
        while self.user_choice not in "PRpr" or self.user_choice == "":
            self.user_choice = input(
                "Type 'p' to start a game or 'r' to read the rules!\n> "
            )
            if self.user_choice.lower() == "r":
                self.display_instructions()
            elif self.user_choice.lower() == "p":
                self.set_board_size()

    def display_instructions(self):
        """
        Prints the instructions and prompts for input to return to welcome
        screen
        """
        Mixins.clear_terminal()
        print(pyfiglet.figlet_format("How to Play\n", font="slant"))
        print("Instructions Page")
        input("\nPress enter to return to the main menu..")
        self.new_game()

    def set_board_size(self):
        """
        Prompts for (and validates) input which will be used to set the size of
        the board
        """
        # Input validation
        while self.user_choice not in "SLsl" or self.user_choice == "":
            self.user_choice = input(
                "\nSelect board size ('s' for small or 'l' for large)\n> "
            )
            self.user_choice = self.user_choice.lower()
            if self.user_choice == "s":
                Player.set_board_size(5)
                break
            elif self.user_choice == "l":
                Player.set_board_size(9)
                break
        self.set_players()

    def set_players(self):
        """
        Prompts for (and validates) input used to determine the type of players
        and creates instances of the Player class
        """
        # Input validation
        while self.user_choice not in "012" or self.user_choice == "":
            self.user_choice = input(
                "\nSelect a number of players (1 or 2)\n> "
            )
            # Debug code left in to demonstrate a Computer vs. Computer game
            if self.user_choice == "0":
                self.player1 = ComputerPlayer()
                self.player2 = ComputerPlayer()
            # Debug code end
            elif self.user_choice == "1" or self.user_choice == "2":
                username = self.request_player_name(1)
                self.player1 = HumanPlayer(username)
                # A 1 player game so player 2 must be the computer
                if self.user_choice.lower() == "1":
                    self.player2 = ComputerPlayer()
                # A 2 player game so ask for the name of player 2
                else:
                    username = self.request_player_name(2)
                    self.player2 = HumanPlayer(username)
                    self.human_players_only = True
        # Set the opponent of each player
        self.player1.set_opponent(self.player2)
        self.player2.set_opponent(self.player1)
        self.set_play_order()

    def request_player_name(self, player_num):
        """
        Given the initian of the player (1 or 2), prompts for, validates and
        returns user input to represent the players name

        Args:
            player_num (int): Number representing the current player

        Returns:
            str: Validated user input to represent chosen player name
        """
        # Input validation
        while True:
            username = input(
                f"\nPlayer {player_num}: Please enter your name..\n> "
            )
            if len(username.strip()) < 3:
                print(
                    "\nPlease enter a name at least 3 characters "
                    "long to proceed."
                )
            else:
                return username

    def set_play_order(self):
        """
        Prompts for (and validates) input used to simulate a coin toss to
        determine the play order and returns this expressed as an
        itertools.cycle object
        """
        Mixins.clear_terminal()
        print("\nTo decide who goes first there will be a coin toss!\n")
        # Input validation
        while True:
            selected_coin_side = input(
                f"{self.player1.get_name()}, "
                "Please choose heads (h) or tails (t)\n> "
            )
            if selected_coin_side in "HTht":
                selected_coin_side = selected_coin_side.lower()
                break
            else:
                print("Invalid input.. ", end="")

        coin_toss_result = random.choice("ht")
        coin_toss_winner, coin_toss_loser = (
            (self.player1, self.player2)
            if coin_toss_result == selected_coin_side
            else (self.player2, self.player1)
        )
        print(f"Coin toss winner = {coin_toss_winner.name}!")
        sleep(2)

        # Set initial play order
        self.player_turn_order = cycle([coin_toss_winner, coin_toss_loser])
        self.placement_phase([self.player1, self.player2])

    def placement_phase(self, player_list):
        """
        Run the ship placement phase of the game and prompts for input before
        starting if their are only human players

        Args:
            player_list (list): list of player objects
        """
        for player in player_list:
            current_player = next(self.player_turn_order)
            print(current_player.get_name())
            current_player.place_ships()
        if self.human_players_only:
            input(
                "Press enter to start the battle, "
                f"{current_player.get_name()} to start!"
            )
        Mixins.clear_terminal()
        self.firing_phase()

    def firing_phase(self):
        """
        Run the firing phase of the game, simulating this if a computer player
        or calling methods from other objects to display the board and
        information to the player
        """
        # Input validation
        while True:
            current_player = next(self.player_turn_order)
            if not current_player.board.board_is_automated:
                print(f"--- {current_player.get_name()} ---\n")
                print("Ship left on board:")
                for ship in current_player.board.fleet.fleet:
                    if ship.get_floatation_status():
                        print(ship.get_name(), end=". ")
                print(
                    "\n\nNumber of opponent's ships remaining = "
                    f"{current_player.opponent.board.fleet.get_num_afloat()}"
                )
                current_player.board.print_board()
                print("Please enter the coordinates to fire upon..\n")
            else:
                print(f"{current_player.get_name()} is thinking..\n")
                sleep(1)
                print(f"Missile fired!..")
                sleep(1)
            current_player.fire_missile()
            Mixins.clear_terminal()
            # Check for game ending condition
            if current_player.opponent.board.fleet.get_num_afloat() == 0:
                break
            # Display blank screen to allow player to swap position before next
            # turn proceeds
            if self.human_players_only:
                input("Press enter to move to next player turn, no peeking!")
                Mixins.clear_terminal()
        self.game_over(current_player)

    def game_over(self, winner):
        """
        Prints the name of the passed player object and prompts the player if
        they would like to play again

        Args:
            winner (object): Player object of the winning player
        """
        print(
            pyfiglet.figlet_format(f"{winner.get_name()} Wins!", font="slant")
        )
        if isinstance(winner, HumanPlayer):
            print("Congratulations on your victory! ", end="")
        print("Would you like to play again?\n")
