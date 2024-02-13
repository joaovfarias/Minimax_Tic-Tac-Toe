import random

class Game:
    def __init__(self, player, computer):
        self.board = list("_" * 9)
        self.player = player
        self.computer = computer
        self.minimax_calls = 0
        self.minimax_alpha_beta_calls = 0

    def print_board(self):
        for i in range(9):
            print(self.board[i], end=" ")
            if i % 3 == 2:
                print()
            else:
                print("|", end=" ")


    def print_helping_board(self):
        for i in range(9):
            print(i, end=" ")
            if i % 3 == 2:
                print()
            else:
                print("|", end=" ")


    def check_winner(self, board):
        for i in range(3):
            if board[i] == board[i + 3] == board[i + 6] != "_":
                return board[i]
            if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != "_":
                return board[i * 3]
        if board[0] == board[4] == board[8] != "_":
            return board[0]
        if board[2] == board[4] == board[6] != "_":
            return board[2]
        return None
    
    def is_full(self, board):
        return "_" not in board
    
    def get_score(self, board):
        winner = self.check_winner(board)
        if winner == self.computer:
            return 1
        if winner == self.player:
            return -1
        return 0
    
    def make_best_move_alpha_beta_minimax(self):
        best_score = -float("inf")
        best_move = -1
        for i in range(9):
            if self.board[i] == "_":
                self.board[i] = self.computer
                score = self.alpha_beta_minimax(self.board, -float("inf"), float("inf"), False)
                self.board[i] = "_"
                if score > best_score:
                    best_score = score
                    best_move = i
        self.board[best_move] = self.computer
        return best_move
        
    def make_best_move_minimax(self):
        best_score = -float("inf")
        best_move = -1
        for i in range(9):
            if self.board[i] == "_":
                self.board[i] = self.computer
                score = self.minimax(self.board, False)
                self.board[i] = "_"
                if score > best_score:
                    best_score = score
                    best_move = i
        self.board[best_move] = self.computer
        return best_move
    
    def make_move(self, move):
        while move < 0 or move > 8 or self.board[move] != "_":
            self.print_board()
            move = int(input("Jogada inválida. Faça sua jogada (0-8): "))
        self.board[move] = self.player

    def alpha_beta_minimax(self, board, alpha, beta, is_maximizing):
        self.minimax_alpha_beta_calls += 1
        if (self.check_winner(board) != None):
            return self.get_score(board)
        if self.is_full(board):
            return 0

        if (is_maximizing):
            best_score = -float("inf")
            for i in range(9):
                if board[i] == "_":
                    board[i] = self.computer
                    score = self.alpha_beta_minimax(board, alpha, beta, False)
                    board[i] = "_"
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if board[i] == "_":
                    board[i] = self.player
                    score = self.alpha_beta_minimax(board, alpha, beta, True)
                    board[i] = "_"
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
            return best_score

    def minimax(self, board, is_maximizing):
        self.minimax_calls += 1
        if (self.check_winner(board) != None):
            return self.get_score(board)
        if self.is_full(board):
            return 0

        if (is_maximizing):
            best_score = -float("inf")
            for i in range(9):
                if board[i] == "_":
                    board[i] = self.computer
                    score = self.minimax(board, False)
                    board[i] = "_"
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if board[i] == "_":
                    board[i] = self.player
                    score = self.minimax(board, True)
                    board[i] = "_"
                    best_score = min(score, best_score)
            return best_score

def main():
    player = input("Escolha 'X' ou 'O': ").upper()
    if player == "X":
        computer = "O"
    else:
        computer = "X"
    game = Game(player, computer)
    option = input("Escolha '1' para Minimax ou '2' para Alpha-Beta Minimax: ")
    begin = random.choice([player, computer])

    while True:
        if begin == player:
            game.print_helping_board()
            print()
            game.print_board()
            print()
            move = int(input("Faça sua jogada (0-8): "))
            game.make_move(move)

            
            if game.check_winner(game.board) == game.player:
                game.print_board()
                print("Você Venceu!")
                break
            if game.is_full(game.board):
                game.print_board()
                print("É um Empate!")
                break

            if option == "1":
                best_move = game.make_best_move_minimax()
            else:
                best_move = game.make_best_move_alpha_beta_minimax()
            print(f"O computador fez a jogada {best_move}")
            if game.check_winner(game.board) == game.computer:
                game.print_board()
                print("Você Perdeu!")
                break
            if game.is_full(game.board):
                game.print_board()
                print("É um Empate!")
                break

        else:
            if option == "1":
                best_move = game.make_best_move_minimax()
            else:
                best_move = game.make_best_move_alpha_beta_minimax()
            print(f"O computador fez a jogada {best_move}")
            if game.check_winner(game.board) == game.computer:
                game.print_board()
                print("Você Perdeu!")
                break
            if game.is_full(game.board):
                game.print_board()
                print("É um Empate!")
                break
            game.print_helping_board()
            print()
            game.print_board()
            print()
            move = int(input("Faça sua jogada (0-8): "))
            game.make_move(move)

            
            if game.check_winner(game.board) == game.player:
                game.print_board()
                print("Você Venceu!")
                break
            if game.is_full(game.board):
                game.print_board()
                print("É um Empate!")
                break

    
    if option == "1":
        print(f"Minimax chamado {game.minimax_calls} vezes")
    else:
        print(f"Alpha-Beta Minimax chamado {game.minimax_alpha_beta_calls} vezes")

   
if __name__ == "__main__":
    main()