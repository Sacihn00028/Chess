# Pygame Chess ♟️

A classic two-player chess game built from scratch using Python and the Pygame library. This project provides a fully functional chess board with all standard rules implemented, offering a clean and intuitive graphical interface for players.

<img width="932" height="786" alt="Screenshot 2025-08-20 150815" src="https://github.com/user-attachments/assets/3127198e-b7af-46e9-8636-db5efb06b621" />

---

## Features

This chess game includes a wide range of features to ensure a complete and authentic experience:

* **Complete Piece Set:** All standard chess pieces (Pawn, Rook, Knight, Bishop, Queen, King) for both white and black are fully implemented.
* **Valid Move Highlighting:** When a piece is selected, all of its legal moves are highlighted on the board, making gameplay clear and user-friendly.
* **Standard Chess Rules:** The game enforces all fundamental chess rules, including:
    * Piece-specific movements.
    * Capturing opponent's pieces.
* **Special Moves Implemented:**
    * **Pawn Promotion:** Automatically prompts the player to choose a new piece (Queen, Rook, Knight, or Bishop) when a pawn reaches the final rank.
    * **Castling:** Both King-side and Queen-side castling are available for both players, provided the rules for castling are met.
    * **En Passant:** The special "in passing" pawn capture is correctly implemented.
* **Game State Detection:**
    * **Check:** Highlights the King's square in red when it is under threat.
    * **Checkmate:** Detects when a player is in check and has no legal moves, declaring the opponent as the winner.
    * **Stalemate:** Correctly identifies a stalemate scenario, resulting in a draw.
* **Captured Pieces Display:** A sidebar neatly displays all the pieces that have been captured by each player.

---

## 🛠️ Prerequisites & Installation

To run this project on your local machine, you'll need Python 3 and the Pygame library installed.

### 1. Clone the Repository

First, clone this repository to your local machine.

```bash
git clone https://github.com/Sacihn00028/Chess
cd Chess
```

### 2. Install Pygame

If you don't have Pygame installed, you can install it using pip.

```bash
pip install pygame
```

### 3. File Structure

Make sure you have the `assets/images` directory in the same folder as the Python script. This project relies on the piece images being in that specific location. Your file structure should look like this:

```
.
├── chess.py
└── assets/
    └── images/
        ├── black bishop.png
        ├── black king.png
        ├── black knight.png
        ├── ... (all other piece images)
```

---

## ▶️ How to Play

1.  **Run the script** from your terminal:
    ```bash
    python chess.py
    ```
2.  The game window will appear, displaying the starting chess position.
3.  **White moves first.** Click on a white piece to select it.
4.  The board will display blue circles on the squares where the selected piece can legally move.
5.  Click on one of the highlighted squares to move your piece.
6.  The turn then passes to the black player.
7.  The game continues until one player achieves checkmate or the game ends in a stalemate.

---

## 📜 Code Overview

The code is structured to handle game logic, rendering, and player input within a main game loop.

* **Game Initialization:** Sets up the Pygame window, loads all piece images, and initializes game state variables (`turn_step`, piece lists, locations, etc.).
* **`board()`:** Draws the 8x8 chessboard with alternating colors.
* **`pieces()`:** Renders all the pieces on the board based on their current locations in the `white_locations` and `black_locations` lists.
* **`options_<piece>()` functions:** These functions (`options_pawn`, `options_rook`, etc.) calculate all *potential* moves for a given piece based on its movement rules, without considering check safety.
* **`safe_move()`:** A crucial function that filters the potential moves from the `options_` functions. It simulates each move to ensure it does not leave the player's own king in check.
* **`checks()`:** Determines if a specific square (usually the king's) is under attack by any enemy piece.
* **Main Game Loop:**
    * Listens for player input (mouse clicks and keyboard presses for promotion).
    * Manages the game state (`turn_step`) to alternate between players.
    * Calls the drawing functions to update the display.
    * Checks for game-ending conditions like checkmate and stalemate after every move.

---

## 🚀 Future Improvements

This project is a solid foundation. Here are some ideas for future enhancements:

* **AI Opponent:** Implement an AI using an algorithm like Minimax to allow for single-player games.
* **Move History:** Add a display to show the sequence of moves made throughout the game using standard algebraic notation.
* **Sound Effects:** Add sounds for piece movement, captures, and check alerts.
* **UI Enhancements:** Create a main menu, a settings screen, and options for restarting the game or choosing piece themes.

---

Enjoy the game!
