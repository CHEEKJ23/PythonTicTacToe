import sys
class TicTacToe:
    def __init__(self):
        self.board = {
            'top-l': ' ', 'top-c': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-c': ' ', 'mid-r': ' ',
            'bot-l': ' ', 'bot-c': ' ', 'bot-r': ' ',
        }
        self.current_player = 'X'

    def print_board(self):
        print(self.board['top-l'] + ' | ' + self.board['top-c'] + ' | ' + self.board['top-r'])
        print('--+---+--')
        print(self.board['mid-l'] + ' | ' + self.board['mid-c'] + ' | ' + self.board['mid-r'])
        print('--+---+--')
        print(self.board['bot-l'] + ' | ' + self.board['bot-c'] + ' | ' + self.board['bot-r'])

    def check_winner(self, player):
        winning_combinations = [
            ['top-l', 'top-c', 'top-r'],
            ['mid-l', 'mid-c', 'mid-r'],
            ['bot-l', 'bot-c', 'bot-r'],
            ['top-l', 'mid-l', 'bot-l'],
            ['top-c', 'mid-c', 'bot-c'],
            ['top-r', 'mid-r', 'bot-r'],
            ['top-l', 'mid-c', 'bot-r'],
            ['top-r', 'mid-c', 'bot-l']
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == player:
                return True
        return False

    def is_board_full(self):
        for value in self.board.values():
            if value == ' ':
                return False
        return True

    def make_move(self, move):
        if move not in self.board:
            return False, "Invalid move. Position does not exist."
        if self.board[move] != ' ':
            return False, "Invalid move. Position already taken."
        self.board[move] = self.current_player
        return True, ""

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        while True:
            self.print_board()
            move = input(f"Player {self.current_player}, enter your move (e.g., top-l, mid-c): ")
            valid, message = self.make_move(move)
            if not valid:
                print(message)
                continue

            if self.check_winner(self.current_player):
                self.print_board()
                print(f"Congratulations! Player {self.current_player} wins!")
                break
                sys.exit()
            elif self.is_board_full():
                self.print_board()
                print("It's a tie! DRAW!")
                break
                sys.exit()

            self.switch_player()