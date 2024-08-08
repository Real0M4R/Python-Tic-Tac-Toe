import os
import sys  # Import sys to use sys.exit()

class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Please Enter Your Name: ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid Name. Please only use Letters.")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, choose your symbol (A single letter Only): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid Symbol. Please use a Single Letter.")


class Menu:
    def display_main_menu(self):
        print("Welcome to @Real0M4R's Tic Tac Toe game!")
        print("1. Start Game")
        print("2. Quit Game")
        while True:
            choice = input("Enter one of the numbers presented to choose (1 or 2): ")
            if choice in ["1", "2"]:
                print(":" * 50)
                return choice
            print("Invalid choice. Please select 1 or 2.")

    def display_endgame_menu(self):
        menu_text = """
        Game Over!

        1. Restart Game
        2. Quit Game

        Enter Your choice (1 or 2): """
        while True:
            choice = input(menu_text)
            if choice in ["1", "2"]:
                return choice
            print("Invalid choice. Please select 1 or 2.")


class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i + 3]))
            if i < 6:
                print("-" * 5)

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    def is_valid_move(self, choice):
        return self.board[choice - 1].isdigit()

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def clear_screen(self):
        # Clear the screen based on the operating system
        os.system('cls' if os.name == 'nt' else 'clear')

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for index, player in enumerate(self.players):
            print(f"Player {index + 1}, enter your details: ")
            player.choose_name()
            player.choose_symbol()
            print(":" * 50)

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.clear_screen()
        self.play_game()

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]]
        for combo in win_combinations:
            if (self.board.board[combo[0]] == self.board.board[combo[1]] ==
                    self.board.board[combo[2]]):
                print(f"{self.players[self.current_player_index].name} wins!")
                return True
        return False

    def check_draw(self):
        if all(not cell.isdigit() for cell in self.board.board):
            print("The game is a draw!")
            return True
        return False

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid Move, Try Again")
            except ValueError:
                print("Please Enter a Number Between 1 and 9")
        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def quit_game(self):
        print("Quit Game Successfully, Thank You for Playing!")
        sys.exit()  # Exit the program


game = Game()
game.start_game()
