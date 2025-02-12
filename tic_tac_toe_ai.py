import numpy as np

class TicTacToeAI:
    def __init__(self):
        self.human = 1   # Human is 'X' (1)
        self.ai = -1     # AI is 'O' (-1)

    def is_winner(self, board, player):
        """Check if the given player has won and return winning positions."""
        # Check rows
        for i in range(3):
            if np.all(board[i, :] == player):
                return True, [(i, 0), (i, 1), (i, 2)]
        
        # Check columns
        for j in range(3):
            if np.all(board[:, j] == player):
                return True, [(0, j), (1, j), (2, j)]
        
        # Check diagonals
        if np.all(np.diag(board) == player):
            return True, [(0, 0), (1, 1), (2, 2)]
        if np.all(np.diag(np.fliplr(board)) == player):
            return True, [(0, 2), (1, 1), (2, 0)]
        
        return False, []

    def check_two_in_line(self, board, player):
        """Check if there are two pieces in a row/column/diagonal and return the empty spot."""
        # Check rows
        for i in range(3):
            if np.count_nonzero(board[i, :] == player) == 2 and np.count_nonzero(board[i, :] == 0) == 1:
                return i, np.where(board[i, :] == 0)[0][0]
        
        # Check columns
        for j in range(3):
            if np.count_nonzero(board[:, j] == player) == 2 and np.count_nonzero(board[:, j] == 0) == 1:
                return np.where(board[:, j] == 0)[0][0], j
        
        # Check main diagonal
        diag = np.diag(board)
        if np.count_nonzero(diag == player) == 2 and np.count_nonzero(diag == 0) == 1:
            idx = np.where(diag == 0)[0][0]
            return idx, idx
        
        # Check anti-diagonal
        anti_diag = np.diag(np.fliplr(board))
        if np.count_nonzero(anti_diag == player) == 2 and np.count_nonzero(anti_diag == 0) == 1:
            idx = np.where(anti_diag == 0)[0][0]
            return idx, 2 - idx
        
        return None

    def is_draw(self, board):
        """Check if the board is full (draw)."""
        return np.count_nonzero(board == 0) == 0

    def get_empty_cells(self, board):
        """Get list of empty cells."""
        return [(i, j) for i in range(3) for j in range(3) if board[i, j] == 0]

    def minimax(self, board, depth, is_maximizing, alpha, beta):
        """Minimax algorithm with Alpha-Beta Pruning."""
        ai_wins, _ = self.is_winner(board, self.ai)
        human_wins, _ = self.is_winner(board, self.human)
        
        if ai_wins:
            return 100 - depth
        if human_wins:
            return depth - 100
        if self.is_draw(board):
            return 0

        empty_cells = self.get_empty_cells(board)
        
        if is_maximizing:
            best_score = float('-inf')
            for i, j in empty_cells:
                board[i, j] = self.ai
                score = self.minimax(board, depth + 1, False, alpha, beta)
                board[i, j] = 0
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = float('inf')
            for i, j in empty_cells:
                board[i, j] = self.human
                score = self.minimax(board, depth + 1, True, alpha, beta)
                board[i, j] = 0
                best_score = min(best_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return best_score

    def best_move(self, board):
        """Find the best move for AI with improved strategy."""
        board = np.array(board)
        
        # 1. Check if AI can win immediately
        winning_move = self.check_two_in_line(board, self.ai)
        if winning_move:
            return winning_move
        
        # 2. Check if we need to block opponent's win
        blocking_move = self.check_two_in_line(board, self.human)
        if blocking_move:
            return blocking_move
        
        # 3. If no immediate threats, use Minimax for strategic play
        best_score = float('-inf')
        move = None
        empty_cells = self.get_empty_cells(board)
        
        # Prefer center if available
        if board[1, 1] == 0:
            return (1, 1)
        
        for i, j in empty_cells:
            board[i, j] = self.ai
            score = self.minimax(board, 0, False, float('-inf'), float('inf'))
            board[i, j] = 0
            
            # Prefer corners over edges
            if (i, j) in [(0,0), (0,2), (2,0), (2,2)]:
                score += 1
                
            if score > best_score:
                best_score = score
                move = (i, j)
        
        return move