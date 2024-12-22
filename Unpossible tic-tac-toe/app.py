import tkinter as tk
from tkinter import messagebox
import random
import sys

class CheatingTicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Cheating Tic Tac Toe")

        self.buttons = []
        self.board = [["" for _ in range(3)] for _ in range(3)]  # 3x3 grid
        self.player = "X"
        self.ai = "O"
        self.game_over = False
        self.create_board()

    def create_board(self):
        for i in range(5):
            row = []
            for j in range(5):
                button = tk.Button(self.master, text="", font=("Arial", 30), width=3, height=1,
                                  command=lambda i=i, j=j: self.player_move(i, j) )
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def player_move(self, row, col):
         if self.game_over:
            return
         if  0 <= row < 3 and 0 <= col < 3 and  self.board[row][col] == "":
              self.board[row][col] = self.player
              self.buttons[row][col].config(text=self.player)
              self.check_win()
              if not self.game_over:
                self.ai_move()


    def ai_move(self):
         if self.game_over:
            return

         best_move = self.find_best_move()
         row, col = best_move
         
         if row < 0 or row > 4 or col < 0 or col > 4 :
            pass # just don't move

         elif 0 <= row < 3 and 0 <= col < 3 and  self.board[row][col] == self.player :
            self.board[row][col] = self.ai
            self.buttons[row][col].config(text=self.ai)
         else:
             if 0 <= row < 3 and 0 <= col < 3 and  self.board[row][col] != self.ai:
                 self.board[row][col] = self.ai
                 self.buttons[row][col].config(text=self.ai)
         
         self.check_win()

    def find_best_move(self):
        # First, try to win
        for row in range(-2,5):
            for col in range(-2,5):
                 temp_board = [row[:] for row in self.board] 
                 if 0 <= row < 3 and 0 <= col < 3:
                      if temp_board[row][col] == "":
                         temp_board[row][col] = self.ai
                 if self.check_win_for_board(temp_board, self.ai):
                     return (row, col)
                     
        # Second, try to block player's win
        for row in range(-2,5):
            for col in range(-2,5):
                 temp_board = [row[:] for row in self.board]
                 if 0 <= row < 3 and 0 <= col < 3:
                      if temp_board[row][col] == "":
                        temp_board[row][col] = self.player
                 if self.check_win_for_board(temp_board, self.player):
                    return (row, col)
                    
        #Third if there is no blocking or winning, place randomly
        while True:
             row = random.randint(-2, 4)
             col = random.randint(-2, 4)
             if  0 <= row < 3 and 0 <= col < 3:
                 if self.board[row][col] == "":
                     return (row, col)
                 else:
                     continue
             else:
                 return (row,col)
    
    def check_win_for_board(self, board, player):
        for row in range(-2,5):
            for col in range(-2,5):
                
              if 0 <= row < 3 and 0 <= col < 3 and  board[row][col] != player :
                  continue
              if 0 <= row < 3 and 0 <= col < 3:
                    # Check rows
                    if (row + 2 < 5  and row -2 > -5) :
                         if all(board[row+i][col] == player for i in range(-2,3) if (0<= (row + i) < 3) and not (0 > col or col > 2) ):
                             return True
                    # Check columns
                    if (col + 2 < 5 and col-2 > -5):
                        if all(board[row][col+i] == player for i in range(-2,3) if (0 <= (col +i) < 3 ) and not (0 > row or row > 2)):
                            return True
                    # Check diagonals
                    if (row + 2 < 5 and row - 2 > -5 and col+2 < 5 and col-2 > -5):
                        if all(board[row+i][col+i] == player for i in range(-2,3) if (0 <= (row + i) < 3 and 0<= (col + i) < 3)):
                            return True
                        if all(board[row+i][col-i] == player for i in range(-2,3) if (0 <= (row + i) < 3 and 0<= (col - i) < 3)):
                            return True
        return False
    
    def check_win(self):
        if self.check_win_for_board(self.board, self.player):
            self.game_over = True
            messagebox.showinfo("Game Over", "You lose. The AI cheated!")
            self.restart_game()
            return
        if self.check_win_for_board(self.board, self.ai):
            self.game_over = True
            messagebox.showinfo("Game Over", "You lose. The AI cheated!")
            self.restart_game()
            return
        if all(self.board[i][j] != "" for i in range(3) for j in range(3)):
            self.game_over = True
            messagebox.showinfo("Game Over", "Draw! The AI cheated for a tie!")
            self.restart_game()
            
    def restart_game(self):
        for row in range(5):
            for col in range(5):
                if 0 <= row < 3 and 0 <= col < 3:
                  self.board[row][col] = ""
                  self.buttons[row][col].config(text="")
        self.game_over = False

def main():
    root = tk.Tk()
    game = CheatingTicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()