from pprint import pprint
import tkinter as tk

# what happens when you submit the puzzle
def on_submit():
    global puzzle
    puzzle = []
    for i in range(9):
        row = []
        for j in range(9):
            entry = entries[i][j]
            # set variable to entered value
            value = entry.get()
            # put the value into the puzzle
            if value.isdigit():
                row.append(int(value))
            # if there is no input, put -1 to represent blank
            else:
                row.append(-1)
            entry.delete(0, tk.END)
        puzzle.append(row)
    # print the puzzle after it is done
    generate_text()

def generate_text():
    pprint(puzzle)

# find empty spaces
def find_empty(puzzle):
    # rows
    for r in range(9):
        # columns
        for c in range(9):
            # if that x and y value (row and column) is blank (-1), return those values
            if puzzle[r][c] == -1:
                return r, c
    # if the spots are not blank, return nothing
    return None, None


def is_valid(puzzle, guess, row, col):
    # set a variable to the row value (row value is determined in solver function.
    row_vals = puzzle[row]

    # if the randomly generated number is one of the row values then it is not valid
    if guess in row_vals:
        return False

    # same thing with columns but you have to do x y values.
    col_vals = [puzzle[i][col] for i in range(9)]

    # if the randomly generated numbers is one of the colummn values ...
    if guess in col_vals:
        return False

    # for checking the 3x3 squares, you have to start the rows and columns every 3 values 3 times
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    # set the range to the start of the row 3 more values of the row (the length of the 3x3 squares)
    for r in range(row_start, row_start + 3):
        # same with range of columns and setting widths
        for c in range(col_start, col_start + 3):
            # if the guess is equal to this spot, then it is not valid
            if puzzle[r][c] == guess:
                return False
    # if all of these checks fail, that means that the guess is valid
    return True


def solver(puzzle):
    # set variables to equal the values of the empty spots
    row, col = find_empty(puzzle)

    # if there are no blank spaces then it is solved!
    if row is None:
        return True

    # set guess variable equal to values between 1-9.
    for guess in range(1, 10):
        # put the variables you have created and check if they are valid
        if is_valid(puzzle, guess, row, col):
            # if it is a valid guess, then set that point to the guess
            puzzle[row][col] = guess
            # recursively call the solver
            if solver(puzzle):
                return True

        # if it is not valid or if it is not returned true, then reset it and backtrack
        puzzle[row][col] = -1
    # if no values can be valid, then the puzzle is unsolvable.
    return False


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Sudoku Puzzle")

    # create board for puzzle
    entries = [[None] * 9 for _ in range(9)]

    for i in range(9):
        for j in range(9):
            # style entry
            entry = tk.Entry(root, width=2, justify="center", font=("Arial", 12, "bold"))
            entry.grid(row=i, column=j)
            entries[i][j] = entry

    # code for button
    submit_button = tk.Button(root, text="Submit", command=on_submit)
    # button style
    submit_button.grid(row=9, columnspan=9, pady=10)

    root.mainloop()



    # example_board = [
    #
    #     # [3, 9, -1, -1, 5, -1, -1, -1, -1],
    #     # [-1, -1, -1, 2, -1, -1, -1, -1, 5],
    #     # [-1, -1, -1, 7, 1, 9, -1, 8, -1],
    #     #
    #     # [-1, 5, -1, -1, 6, 8, -1, -1, -1],
    #     # [2, -1, 6, -1, -1, 3, -1, -1, -1],
    #     # [-1, -1, -1, -1, -1, -1, -1, -1, 4],
    #     #
    #     # [5, -1, -1, -1, -1, -1, -1, -1, -1],
    #     # [6, 7, -1, 1, -1, 5, -1, 4, -1],
    #     # [1, -1, 9, -1, -1, -1, 2, -1, -1]
    #
    #     # [-1, -1, -1, -1, -1, 4, -1, 2, -1],
    #     # [-1, 5, 3, -1, -1, -1, 6, -1, 9],
    #     # [6, -1, 2, -1, 5, -1, -1, -1, -1],
    #     #
    #     # [-1, 9, -1, 1, 4, -1, -1, -1, -1],
    #     # [1, -1, 6, 5, 7, -1, 4, 9, 8],
    #     # [3, 4, 7, 2, 8, -1, -1, 5, 6],
    #     #
    #     # [-1, -1, -1, -1, 9, 7, -1, 6, 1],
    #     # [7, 6, -1, -1, -1, 5, 2, -1, 4],
    #     # [-1, 3, -1, -1, 6, -1, -1, -1, -1]
    #
    #     # [-1, -1, 8, -1, -1, -1, -1, 6, -1],
    #     # [-1, -1, -1, -1, 2, 8, 7, -1, -1],
    #     # [5, 2, -1, 7, -1, 1, -1, -1, -1],
    #     #
    #     # [2, -1, 7, 6, 1, 4, 3, -1, 8],
    #     # [3, 6, 5, -1, 9, 2, 4, -1, 7],
    #     # [-1, -1, -1, 5, -1, -1, 6, -1, 9],
    #     #
    #     # [9, -1, 2, -1, -1, -1, 5, 4, -1],
    #     # [-1, -1, -1, 1, -1, -1, 2, -1, -1],
    #     # [6, 8, -1, -1, 4, -1, -1, 7, -1]
    #
    #     # [-1, -1, 4, -1, -1, 3, -1, 2, -1],
    #     # [-1, -1, 8, -1, 1, -1, -1, -1, -1],
    #     # [2, 1, -1, -1, -1, 7, 9, -1, -1],
    #     #
    #     # [-1, -1, -1, -1, -1, 9, -1, -1, 5],
    #     # [3, 6, -1, -1, 7, -1, -1, 8, -1],
    #     # [-1, -1, 1, -1, -1, -1, -1, -1, -1],
    #     #
    #     # [7, 2, -1, -1, 6, -1, -1, 3, -1],
    #     # [4, -1, -1, -1, -1, -1, -1, -1, -1],
    #     # [-1, -1, -1, 3, -1, -1, 8, -1, -1],
    #
    #     # [4, 1, -1, 7, -1, -1, -1, -1, -1],
    #     #  [-1, -1, 3, -1, -1, 6, 2, 9, -1],
    #     #  [-1, -1, -1, -1, -1, -1, -1, -1, 5],
    #     #
    #     #  [-1, -1, -1, -1, -1, -1, 8, -1, -1],
    #     #  [-1, -1, 9, -1, -1, 2, 3, 4, -1],
    #     #  [2, -1, -1, -1, 6, -1, -1, -1, -1],
    #     #
    #     #  [-1, 3, -1, -1, 1, -1, 4, 5, -1],
    #     #  [-1, -1, -1, -1, -1, 4, -1, -1, 8],
    #     #  [-1, -1, 5, -1, -1, -1, -1, -1, 6]
    #
    #
    #
    # ]

    print(solver(puzzle))
    pprint(puzzle)



