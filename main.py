from game import TicTacToe
from minimax import find_best_move
import time

def print_result(winner):
    if winner == 'X' or winner == 'O':
        print(f"{winner} wins!")
    else:
        print("It's a tie!")

def switch_player(player):
    return 'O' if player == 'X' else 'X'

def main():
    game = TicTacToe()
    human_player = input("Choose your side (X/O): ").upper()
    while human_player not in ['X', 'O']:
        human_player = input("Invalid choice. Please choose X or O: ").upper()
    
    ai_player = 'O' if human_player == 'X' else 'X'
    
    current_player = 'X'  # X starts the game
    
    while game.current_winner is None and not game.is_full():
        if current_player == human_player:
            game.print_board_nums()
            square = int(input(f"{current_player}'s turn. Input move (0-8): "))
            while not game.make_move(square, current_player):
                square = int(input("Invalid move. Try again: "))
        else:
            print(f"{current_player}'s (AI's) turn.")
            square = find_best_move(game, ai_player, human_player)
            game.make_move(square, ai_player)
            print(f"AI chooses square {square}")
            time.sleep(1)  # Simulate thinking

        if game.check_winner(square, current_player):
            game.print_board()
            print_result(current_player)
            return

        game.print_board()
        current_player = switch_player(current_player)

        if game.is_full():
            print_result(None)

if __name__ == "__main__":
    main()
