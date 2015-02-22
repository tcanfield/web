import math

class sudoku_board:
    #Initialize the board by passing in a string representing the board
    #positions in order top to bottom, left to right.  Use 0 to represent
    #empty spaces
    #
    #arg board: String representation of the board.
    #Positions listed in order left to right, top to bottom. 0 for empty spaces.
    #
    #arg size: The maximum number of the board.  e.g. size=9 for a 9x9 board
    def __init__(self, board_string, size):
        if len(board_string) != size*size:
            raise ValueError("Number of board positions does not match board size." +str(len(board_string)) +str(size))

        #for i in range(size):
        #   for j in range(size):
        #      self.board_positions[i][j] = board[(i*9)+j]
        #This loop as a list comprehension:
        self.board_positions = [[board_string[(i*9)+j] for j in range(size)]for i in range(size)]
        self.size = size
	

    #Getter/setters:
    def set_cell(self, row, col, val):
        self.board_positions[row][col] = val

    def get_cell(self, row, col):
        return self.board_positions[row][col]

    def get_board(self):
        return self.board_positions
    
    def get_single_string(self):
        string = ""
        for i in range(self.size):
            for j in range(self.size):
                string = string + str((self.board_positions[i][j]))
        return string

    def __str__(self):
        string = ""
        for i in range(self.size):
            string = string + str((self.board_positions[i])) + "\n"
        return string
        
class sudoku_solve:
    #Create a sudoku board to start with
    def __init__(self, board_string, size):
        self.starting_board = sudoku_board(board_string, size)
        self.size = size
        self.stack = []

    def solve(self):
        return self.solve_dfs(self.starting_board, 0, 0)
    
    def solve_dfs(self, board, row=0, col=0):
        #Base Case
        if self.is_solved(board):
            self.solved_board = board
            return self.solved_board
            

        #Find a valid number for a cell and recursively keep going
        if board.get_cell(row, col) == '0':
            for i in range(1, self.size+1):
                if self.valid_cell(board, row, col, str(i)):
                    board.set_cell(row, col, str(i))
                    self.solve_dfs(board, self.next_row(row, col), self.next_col(col))
                    if self.is_solved(board):
                        return self.solved_board 
                    #If we get here we have backtracked, so set this row/col back to 0 and keep trying
                    board.set_cell(row, col, '0')

        else:
            self.solve_dfs(board, self.next_row(row,col), self.next_col(col))
            if self.is_solved(board):
                return self.solved_board
                    
    def next_row(self, row, col):
        if col is 8:
            return row+1
        else:
            return row

    def next_col(self, col):
        if col is 8:
            return 0
        else:
            return col+1

    def prev_row(self, row, col):
        if col is 0:
            return row-1
        else:
            return row
                                          
    def prev_col(self, col):
        if col is 0:
            return 8
        else:
            return col-1
                                          
    def is_solved(self, board):

        rows_solved = True
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(board.get_cell(i,j))
                if j is self.size-1:
                    if not (set(['1','2','3','4','5','6','7','8','9']) <= set(row)):
                        rows_solved = False
                        break

        cols_solved = True
        for i in range(self.size):
            col = []
            for j in range(self.size):
                col.append(board.get_cell(j,i))
                if j is self.size-1:
                    if not (set(['1','2','3','4','5','6','7','8','9']) <= set(col)):
                        rows_solved = False
                        break

        return (rows_solved and cols_solved)
                
    def valid_cell(self, board, row, col, value):
	 
        #Make sure number is not already in this row
        row_values = []
        for i in range(self.size):
            row_values.append(board.get_board()[row][i])
        if value in row_values:
            return False

        #Make sure number is not already in this col
        col_values = []
        for i in range(self.size):
            col_values.append(board.get_board()[i][col])
        if value in col_values:
            return False

        #Makre sure number is not already in this square. (square is sqrt(size) x sqrt(size) square)
        total_squares = self.size
        square_size = int(math.sqrt(total_squares))

        #Find which square the row/col is in
        square_num = (int((row/square_size))*square_size) + int((col/square_size))

        #Check each cell in that square and see if the value is already in it
        for row in range(square_size):
            for col in range(square_size):
                cell = board.get_board()[row + (int((square_num/square_size))*square_size)][col + ((square_num%square_size)*square_size)]
                if value == cell:
                    return False

        #If none of the checks return false return true
        return True
             
#start_time = time.time()
#board_string = "000037600000600090008000004090000001600000009300000040700000800010009000002540000"
#board = sudoku_board(board_string, 9)
#solver = sudoku_solve(board_string, 9)
#print(solver.solve())
        
        
