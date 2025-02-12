from flask import Flask, render_template, request, jsonify
import numpy as np
from tic_tac_toe_ai import TicTacToeAI

app = Flask(__name__)

# Initialize AI
ai = TicTacToeAI()

# Global game state
game_state = {
    'board': [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    'winner': None,
    'winning_path': [],
    'message': ''  # Added message field
}

def check_winner(board):
    np_board = np.array(board)
    
    # Check for AI win
    ai_won, ai_path = ai.is_winner(np_board, -1)
    if ai_won:
        return -1, ai_path, "AI wins!"
        
    # Check for human win
    human_won, human_path = ai.is_winner(np_board, 1)
    if human_won:
        return 1, human_path, "Player wins!"
    
    # Check for draw
    if ai.is_draw(np_board):
        return 0, [], "It's a draw!"
        
    return None, [], ""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/make_move', methods=['POST'])
def make_move():
    global game_state
    data = request.json
    row, col = data['row'], data['col']
    
    if game_state['board'][row][col] == 0:
        game_state['board'][row][col] = 1
        
        # Check if player won
        result, path, message = check_winner(game_state['board'])
        if result is not None:
            game_state['winner'] = 'X' if result == 1 else ('Draw' if result == 0 else 'O')
            game_state['winning_path'] = path
            game_state['message'] = message
            return jsonify(game_state)
            
        # AI move
        np_board = np.array(game_state['board'])
        ai_move = ai.best_move(np_board)
        
        if ai_move:
            ai_row, ai_col = ai_move
            game_state['board'][ai_row][ai_col] = -1
            
            # Check if AI won
            result, path, message = check_winner(game_state['board'])
            if result is not None:
                game_state['winner'] = 'O' if result == -1 else ('Draw' if result == 0 else 'X')
                game_state['winning_path'] = path
                game_state['message'] = message
    
    return jsonify(game_state)

@app.route('/reset', methods=['POST'])
def reset():
    global game_state
    game_state = {
        'board': [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        'winner': None,
        'winning_path': [],
        'message': ''
    }
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)