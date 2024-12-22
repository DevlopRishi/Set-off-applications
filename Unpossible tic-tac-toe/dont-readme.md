# Evil Tic Tac Toe Game (lacs logic)

## Game Description

This is a Tic Tac Toe game where you play against an AI opponent. However, the AI is designed to be unbeatable through cheating methods.

## Cheating Mechanisms

The AI opponent employs several methods to ensure its victory:

1.  **Strategic Moves**: The AI uses an algorithm to choose the best possible move to win the game or block you from winning.

2.  **Out-of-Bounds Moves**: The AI can place its marks outside the traditional 3x3 grid, making it harder to predict its next move.

3.  **Mark Overwriting**: The AI can overwrite your marks on the board, making winning or even drawing impossible for the player.

4.  **Unpredictable Actions**: The AI can act in unexpected ways, changing how it plays the game.

## Probability of Winning

The chances of the player winning are effectively zero due to the AI's cheating capabilities. The AI is designed to always secure either a win or a draw at a minimum.

## Goal of the Game

The purpose of the game is not to win but to experience how an AI can be programmed to be an impossible opponent. It is designed as an exercise in programming logic and AI concepts.

## Technical Details
The game is built in Python using `tkinter` for the graphical interface. The code utilizes a 5x5 grid structure to handle out of bounds moves. The `find_best_move()` function implements the cheating mechanics.