URL - https://tic-tac-toe-ai-z0m2.onrender.com

## Tic-Tac-Toe AI Project Description

This project implements a classic game of Tic-Tac-Toe where a human player competes against an AI opponent. The game is built using Python with the Flask framework for the backend and HTML, CSS, and JavaScript for the frontend, providing an engaging and interactive user experience.

### Core Features:

*   **Human vs. AI Gameplay:** Users can play Tic-Tac-Toe against an AI opponent that utilizes the Minimax algorithm with Alpha-Beta pruning to make strategic decisions.
*   **Intelligent AI Opponent:** The AI is designed to be a challenging opponent, employing a combination of strategies:
    *   **Immediate Win/Block:** The AI first checks if it can win in the next move or if it needs to block the player from winning.
    *   **Minimax Algorithm:** The AI uses the Minimax algorithm to evaluate possible moves and choose the optimal one, considering potential future outcomes.
    *   **Alpha-Beta Pruning:** Optimizes the Minimax algorithm by reducing the number of nodes evaluated, improving the AI's decision-making speed.
    *   **Strategic Preferences:** The AI prefers to play in the center if available and prioritizes corners over edges for strategic advantage.
*   **Real-time Updates:** The game board updates in real-time as players make their moves, providing immediate visual feedback.
*   **Win/Draw Detection:** The game accurately detects wins and draws, displaying an appropriate message to the user. The winning path is highlighted on the board.
*   **Scoreboard:** Keeps track of the player's and AI's scores across multiple games.
*   **Restart/New Game Options:** Users can easily restart the current game or start a new game, resetting the board and scores as desired.
*   **Responsive Frontend:** The user interface is designed to be visually appealing and intuitive, with clear indicators for moves and game status.

### Technologies Used:

*   **Backend:**
    *   Python
    *   Flask: A lightweight web framework to handle game logic and API endpoints.
    *   NumPy: Used for efficient board representation and calculations.
*   **Frontend:**
    *   HTML: Structures the web page and its elements.
    *   CSS: Styles the user interface for an appealing visual experience.
    *   JavaScript: Implements the interactive game logic, makes API calls to the backend, and dynamically updates the UI.
*   **Algorithm:**
    *   Minimax with Alpha-Beta Pruning

### How it Works:

1.  **Frontend (index.html):** The HTML file sets up the structure of the Tic-Tac-Toe board, score display, and buttons. CSS styles the elements. JavaScript handles user interactions, such as clicking on a cell to make a move, and sends these moves to the Flask backend.
2.  **Backend (app.py):**
    *   The Flask app receives move requests from the frontend.
    *   It updates the game board state based on the player's move.
    *   It calls the `TicTacToeAI` class to determine the AI's best move using the Minimax algorithm.
    *   It checks for a winner or a draw after each move.
    *   It sends the updated game state back to the frontend as a JSON response.
3.  **AI Logic (tic\_tac\_toe\_ai.py):**
    *   The `TicTacToeAI` class encapsulates the AI logic.
    *   The `minimax` function implements the Minimax algorithm with Alpha-Beta pruning.
    *   The `best_move` function uses the Minimax algorithm to determine the AI's optimal move, also considering immediate win/block opportunities and strategic preferences.

### Potential Enhancements:

*   **Difficulty Levels:** Implement multiple difficulty levels by adjusting the depth of the Minimax algorithm.
*   **User Interface Improvements:** Enhance the UI with animations, sound effects, and customizable themes.
*   **Multiplayer Mode:** Allow two human players to play against each other.
*   **AI Learning:** Implement machine learning techniques to allow the AI to learn from past games and improve its strategy.
