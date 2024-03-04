def minimax(board, depth, is_maximizing, player, opponent):
    """
    Implements the minimax algorithm to find the best move for the AI player.
    :param board: Instance of TicTacToe
    :param depth: Current depth in the game tree
    :param is_maximizing: Boolean indicating if currently maximizing or minimizing
    :param player: AI player's symbol ('X' or 'O')
    :param opponent: Human player's symbol ('X' or 'O')
    :return: Tuple (best score, best move)
    """
    if board.current_winner == player:
        return (1, None)  # AI wins
    elif board.current_winner == opponent:
        return (-1, None)  # Opponent wins
    elif board.is_full():
        return (0, None)  # Draw

    if is_maximizing:
        best_score = float('-inf')
        best_move = None
        for possible_move in board.available_moves():
            board.make_move(possible_move, player)
            score = minimax(board, depth + 1, False, player, opponent)[0]
            board.board[possible_move] = " "  # Undo the move
            board.current_winner = None  # Reset winner
            if score > best_score:
                best_score = score
                best_move = possible_move
        return (best_score, best_move)
    else:  # Minimizing
        best_score = float('inf')
        best_move = None
        for possible_move in board.available_moves():
            board.make_move(possible_move, opponent)
            score = minimax(board, depth + 1, True, player, opponent)[0]
            board.board[possible_move] = " "  # Undo the move
            board.current_winner = None  # Reset winner
            if score < best_score:
                best_score = score
                best_move = possible_move
        return (best_score, best_move)

def find_best_move(board, player, opponent):
    """
    Finds the best move for the AI player.
    :param board: Instance of TicTacToe
    :param player: AI player's symbol ('X' or 'O')
    :param opponent: Human player's symbol ('X' or 'O')
    :return: Integer representing the best move
    """
    _, best_move = minimax(board, 0, True, player, opponent)
    return best_move
