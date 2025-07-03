#N-Queens Solver

Overview

This project is a graphical user interface (GUI) application that solves the N-Queens problem using Python and Tkinter. The N-Queens problem involves placing N queens on an NxN chessboard such that no two queens threaten each other. This means no two queens can share the same row, column, or diagonal.

Features





Input the number of queens (N) via a text entry field.



Visualize the solution on a chessboard displayed in the GUI.



Displays an error message for invalid inputs (non-positive integers).



Shows a message if no solution exists for the given N.

Requirements





Python 3.x



Tkinter (usually included with standard Python installations)

Installation





Ensure Python 3.x is installed on your system.



Verify that Tkinter is available by running python -m tkinter in your terminal. If it opens a window, Tkinter is installed.



Download or copy the n_queens_gui.py file to your local machine.

Usage





Save the provided code in a file named n_queens_gui.py.



Open a terminal and navigate to the directory containing the file.



Run the script using the command:

python n_queens_gui.py



The GUI window will open:





Enter a positive integer in the text field to specify the number of queens.



Click the "Solve" button to compute and display a solution.



The chessboard will update to show the positions of the queens (represented by ♕).



If no solution exists or the input is invalid, a message box will inform you.

How It Works





The application uses a backtracking algorithm to solve the N-Queens problem.



The solve_n_queens method checks for safe positions to place queens and recursively builds a solution.



The draw_board method renders the chessboard with alternating colors (white and gray) and places queen symbols where applicable.



The GUI is built using Tkinter, with a canvas to display the board and input fields for user interaction.

Notes





The chessboard size adjusts dynamically based on the input N, with a maximum canvas size of 360x360 pixels.



For very large N, the queen symbols may appear small due to scaling.



No solution exists for N = 2 or N = 3, and the application will display a message indicating this.

Example

For N = 4, a possible solution might look like this on the chessboard:





Queens placed at positions such that no two are on the same row, column, or diagonal.



The board alternates between white and gray squares for clarity.

License

This project is open-source and available under the MIT License.
