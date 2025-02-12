import numpy as np
import pandas as pd
import pickle

# Load the Tic-Tac-Toe dataset
df = pd.read_csv('tic-tac-toe.data.csv')  # Ensure correct file name

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Rename target column if needed
if 'Class' in df.columns:
    df.rename(columns={'Class': 'class'}, inplace=True)

# Check if the target column exists
if 'class' not in df.columns:
    raise ValueError("Error: The 'class' column is missing in the dataset!")

# Convert categorical values ('x', 'o', 'b') into numerical values
mapping = {'x': 1, 'o': -1, 'b': 0}
for col in df.columns[:-1]:  # Exclude the target column
    df[col] = df[col].map(mapping)

# Convert target column ('positive' for win, 'negative' for loss) into numerical values
df['class'] = df['class'].map({'positive': 1, 'negative': 0})

# Print first few rows for verification
print(df.head())

# Split features and target
X = df.drop(columns=['class']).values.reshape(-1, 3, 3)
y = df['class'].values


class TicTacToeAI:
    def __init__(self):
        self.human = -1
        self.ai = 1

    def is_winner(self, board, player):
        """Checks if a player has won the game."""
        for row in board:
            if all(s == player for s in row):
                return True
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self, board):
        """Checks if the game is a draw."""
        return all(cell != 0 for row in board for cell in row)

    def minimax(self, board, depth, is_maximizing, alpha, beta):
        """Minimax algorithm with alpha-beta pruning."""
        if self.is_winner(board, self.ai):
            return 10 - depth
        if self.is_winner(board, self.human):
            return depth - 10
        if self.is_draw(board):
            return 0

        if is_maximizing:
            max_eval = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == 0:
                        board[i][j] = self.ai
                        eval = self.minimax(board, depth + 1, False, alpha, beta)
                        board[i][j] = 0
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == 0:
                        board[i][j] = self.human
                        eval = self.minimax(board, depth + 1, True, alpha, beta)
                        board[i][j] = 0
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

    def best_move(self, board):
        """Finds the best move for AI."""
        best_score = -float('inf')
        move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = self.ai
                    score = self.minimax(board, 0, False, -float('inf'), float('inf'))
                    board[i][j] = 0
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move


# Create and save the AI model
ai_model = TicTacToeAI()
with open('tic_tac_toe_ai.pkl', 'wb') as file:
    pickle.dump(ai_model, file)

# Load model from file
with open('tic_tac_toe_ai.pkl', 'rb') as file:
    loaded_ai = pickle.load(file)

# Example test
test_board = np.zeros((3, 3), dtype=int)
print('AI Best Move:', loaded_ai.best_move(test_board))
