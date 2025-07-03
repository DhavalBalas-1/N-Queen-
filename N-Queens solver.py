import tkinter as tk
from tkinter import messagebox, ttk
import time


class NQueensGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("N-Queens Solver")
        self.master.geometry("600x650")
        self.master.resizable(False, False)

        # State variables
        self.board = None
        self.n = 0
        self.queen_positions = []
        self.is_animating = False

        # GUI Elements
        self.setup_ui()

    def setup_ui(self):
        # Main frame
        self.main_frame = ttk.Frame(self.master, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        ttk.Label(self.main_frame, text="N-Queens Solver", font=("Arial", 16, "bold")).pack(pady=10)

        # Input frame
        input_frame = ttk.Frame(self.main_frame)
        input_frame.pack(pady=5)

        # Board size selection
        ttk.Label(input_frame, text="Board Size:").pack(side=tk.LEFT, padx=5)
        self.size_var = tk.StringVar(value="8")
        self.size_menu = ttk.Combobox(input_frame, textvariable=self.size_var, values=[4, 5, 6, 7, 8, 9, 10, 11, 12],
                                      width=5)
        self.size_menu.pack(side=tk.LEFT, padx=5)

        # Animation speed
        ttk.Label(input_frame, text="Animation Speed:").pack(side=tk.LEFT, padx=5)
        self.speed_var = tk.DoubleVar(value=0.2)
        self.speed_scale = ttk.Scale(input_frame, from_=0.05, to=0.5, orient=tk.HORIZONTAL, variable=self.speed_var,
                                     length=100)
        self.speed_scale.pack(side=tk.LEFT, padx=5)

        # Buttons frame
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=10)

        self.solve_button = ttk.Button(button_frame, text="Solve", command=self.start_solve)
        self.solve_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = ttk.Button(button_frame, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        # Canvas for board
        self.canvas = tk.Canvas(self.main_frame, width=500, height=500, bg="white", highlightthickness=1,
                                highlightbackground="black")
        self.canvas.pack(pady=10)

        # Status label
        self.status_var = tk.StringVar(value="Enter board size and click Solve")
        ttk.Label(self.main_frame, textvariable=self.status_var, font=("Arial", 10)).pack(pady=5)

    def start_solve(self):
        if self.is_animating:
            return

        try:
            self.n = int(self.size_var.get())
            if self.n < 4:
                raise ValueError("Board size must be at least 4")
            self.solve_button.config(state="disabled")
            self.reset_button.config(state="normal")
            self.status_var.set("Solving...")
            self.master.update()
            self.solve_n_queens()
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
            self.reset()

    def reset(self):
        self.canvas.delete("all")
        self.board = None
        self.queen_positions = []
        self.is_animating = False
        self.solve_button.config(state="normal")
        self.reset_button.config(state="disabled")
        self.status_var.set("Enter board size and click Solve")

    def solve_n_queens(self):
        def is_safe(board, row, col):
            # Check row and diagonals
            for i in range(col):
                if board[row][i]:
                    return False
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j]:
                    return False
            for i, j in zip(range(row, self.n), range(col, -1, -1)):
                if board[i][j]:
                    return False
            return True

        def solve_util(col):
            if col >= self.n:
                return True

            for row in range(self.n):
                if is_safe(self.board, row, col):
                    self.board[row][col] = 1
                    self.queen_positions.append((row, col))
                    self.draw_board(animate=True)
                    self.master.update()
                    time.sleep(self.speed_var.get())

                    if solve_util(col + 1):
                        return True

                    self.board[row][col] = 0
                    self.queen_positions.pop()
                    self.draw_board(animate=True)
                    self.master.update()
                    time.sleep(self.speed_var.get())
            return False

        self.board = [[0] * self.n for _ in range(self.n)]
        self.queen_positions = []
        self.is_animating = True

        if solve_util(0):
            self.status_var.set(f"Solution found for {self.n}-Queens!")
        else:
            messagebox.showinfo("No Solution", f"No solution exists for {self.n} queens.")
            self.reset()
        self.is_animating = False
        self.solve_button.config(state="normal")

    def draw_board(self, animate=False):
        self.canvas.delete("all")
        size = 500 // self.n

        for i in range(self.n):
            for j in range(self.n):
                color = "#ffffff" if (i + j) % 2 == 0 else "#cccccc"
                self.canvas.create_rectangle(j * size, i * size, (j + 1) * size, (i + 1) * size, fill=color,
                                             outline="black")

                if self.board[i][j] == 1:
                    queen_size = max(12, size // 2)
                    self.canvas.create_text(
                        j * size + size // 2,
                        i * size + size // 2,
                        text="♕",
                        font=("Arial", queen_size, "bold"),
                        fill="red" if animate else "black"
                    )


def main():
    root = tk.Tk()
    app = NQueensGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()