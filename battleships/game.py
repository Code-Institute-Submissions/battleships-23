from .player import Player, HumanPlayer, ComputerPlayer
from .mixins import Mixins
from itertools import cycle
from time import sleep
import pyfiglet, random


class Game:
    user_choice = ""
    player1 = None
    player2 = None
    player_turn_order = None
    human_players_only = False

    def new_game(self):
        Mixins.clear_terminal()
        print("\n\n")
        print(
            pyfiglet.figlet_format("Welcome to\nBattleships!\n", font="slant")
        )
        self.user_choice = ""
        while self.user_choice not in "PRpr" or self.user_choice == "":
            self.user_choice = input(
                "\nType 'p' to start a game or 'r' to read the rules!\n> "
            )
            if self.user_choice.lower() == "r":
                self.display_instructions()
            elif self.user_choice.lower() == "p":
                self.set_board_size()

    def display_instructions(self):
        Mixins.clear_terminal()
        print("\n\n")
        print(pyfiglet.figlet_format("How to Play\n", font="slant"))
        print("Instructions Page")
        input("\nPress enter to return to the main menu..")
        self.new_game()

    def set_board_size(self):
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
        while self.user_choice not in "012" or self.user_choice == "":
            self.user_choice = input(
                "\nSelect a number of players (1 or 2)\n> "
            )
            # DEBUG
            if self.user_choice == "0":
                self.player1 = ComputerPlayer()
                self.player2 = ComputerPlayer()
            # DEBUG END
            elif self.user_choice == "1" or self.user_choice == "2":
                username = self.get_player_name("Player 1")
                self.player1 = HumanPlayer(username)
                if self.user_choice.lower() == "1":
                    self.player2 = ComputerPlayer()
                else:
                    username = self.get_player_name("Player 2")
                    self.player2 = HumanPlayer(username)
                    self.human_players_only = True

        self.player1.set_opponent(self.player2)
        self.player2.set_opponent(self.player1)

        self.set_play_order()

    def get_player_name(self, player_num):
        while True:
            username = input(f"\n{player_num}: Please enter your name..\n> ")
            if len(username.strip()) < 3:
                print(
                    "\nPlease enter a name at least 3 characters "
                    "long to proceed."
                )
            else:
                return username

    def set_play_order(self):
        Mixins.clear_terminal()
        print("\nTo decide who goes first there will be a coin toss!\n")
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

        self.player_turn_order = cycle([coin_toss_winner, coin_toss_loser])
        self.placement_phase([self.player1, self.player2])

    def placement_phase(self, player_list):
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
                    f"{current_player.opponent.board.fleet.ships_remaining()}"
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
            if current_player.opponent.board.fleet.is_fleet_destroyed():
                break
            if self.human_players_only:
                input("Press enter to move to next player turn, no peeking!")
                Mixins.clear_terminal()
        self.game_over(current_player)

    def game_over(self, winner):
        print(
            pyfiglet.figlet_format(f"{winner.get_name()} Wins!", font="slant")
        )
        if isinstance(winner, HumanPlayer):
            print(
                "Congratulations on your victory! "
                "Would you like to play again?"
            )
        else:
            print("Would you like to play again?")
