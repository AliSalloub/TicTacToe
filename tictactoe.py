import tkinter as tk
from tkinter import simpledialog, messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.board = [[None, None, None] for _ in range(3)]
        self.create_widgets()
        self.reset_game()

    def ask_for_player(self):
        return simpledialog.askstring("Input", "Choose your player (X/O)", parent=self.root).upper()

    def create_widgets(self):
        self.label = tk.Label(self.root, font=('consolas', 40))
        self.label.pack(side="top")

        self.reset_button = tk.Button(self.root, text="Restart", font=('consolas', 20), command=self.reset_game)
        self.reset_button.pack(side="top")

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.frame, text="", font=('consolas', 40), width=5, height=2, command=lambda row=i, col=j: self.next_turn(row, col))
                btn.grid(row=i, column=j)
                self.board[i][j] = btn

    def reset_game(self):
        for row in self.board:
            for btn in row:
                btn.config(text="", bg="white")
        self.player_turn = self.ask_for_player()
        self.label.config(text=f"{self.player_turn}'s Turn")

    def color_winner(self, indices, color):
        for (i, j) in indices:
            self.board[i][j].config(bg=color)

    def next_turn(self, row, col):
        if not self.board[row][col]['text'] and not self.check_winner()[0]:
            self.board[row][col]['text'] = self.player_turn.upper()  # Display text as uppercase
            winner, indices = self.check_winner()
            if winner:
                color = "green" if self.player_turn == 'X' else "blue"
                self.color_winner(indices, color)
                self.label.config(text=f"{self.player_turn} Wins!")
                self.ask_restart()
            elif not any(btn['text'] == '' for row in self.board for btn in row):
                self.color_winner([(i, j) for i in range(3) for j in range(3)], "yellow")
                self.label.config(text="It's a Tie!")
                self.ask_restart()
            else:
                self.player_turn = 'O' if self.player_turn == 'X' else 'X'
                self.label.config(text=f"{self.player_turn}'s Turn")

    def check_winner(self):
        for i in range(3):
            if self.board[i][0]['text'] == self.board[i][1]['text'] == self.board[i][2]['text'] != '':
                return True, [(i, 0), (i, 1), (i, 2)]
            if self.board[0][i]['text'] == self.board[1][i]['text'] == self.board[2][i]['text'] != '':
                return True, [(0, i), (1, i), (2, i)]

        if self.board[0][0]['text'] == self.board[1][1]['text'] == self.board[2][2]['text'] != '':
            return True, [(0, 0), (1, 1), (2, 2)]
        if self.board[0][2]['text'] == self.board[1][1]['text'] == self.board[2][0]['text'] != '':
            return True, [(0, 2), (1, 1), (2, 0)]

        return False, []

    def ask_restart(self):
        answer = messagebox.askyesno("New Game", "Would you like to start a new game?")
        if answer:
            self.reset_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
