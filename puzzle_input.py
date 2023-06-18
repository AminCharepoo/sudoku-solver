import tkinter as tk
from pprint import pprint

def on_submit():
    global puzzle
    puzzle = []
    for i in range(9):
        row = []
        for j in range(9):
            entry = entries[i][j]
            value = entry.get()
            if value.isdigit():
                row.append(int(value))
            else:
                row.append(-1)
            entry.delete(0, tk.END)
        puzzle.append(row)
    generate_text()

def generate_text():
    pprint(puzzle)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Sudoku Puzzle")

    entries = [[None]*9 for _ in range(9)]

    for i in range(9):
        for j in range(9):
            entry = tk.Entry(root, width=2, justify="center", font=("Arial", 12, "bold"))
            entry.grid(row=i, column=j)
            entries[i][j] = entry

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.grid(row=9, columnspan=9, pady=10)

    root.mainloop()


pprint(puzzle)