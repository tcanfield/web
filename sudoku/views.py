from django.shortcuts import render
from board import sudoku_solve

# Create your views here.
def sudoku(request):
    board = [""]*81
    size = 9
    #import board.py
    #Get input to use as the board
    #Run solve with the input board
    #return solved board and render it
    
    #string to store the input
    input_cells = ""
    solved_string = ""
    
    #If the form is submitted solve the board
    if request.method == 'POST':
        #Get input to use as board
        for i in range(1, len(board)+1):
            if str(i) in request.POST:
                if (str(request.POST[str(i)]) != "") and (str(request.POST[str(i)]).isdigit()):
                    input_cells = input_cells + str(request.POST[str(i)])
                else:
                    input_cells = input_cells + '0'
            else:
                input_cells = input_cells + '0'
        #Use input to solve board
        solver = sudoku_solve(input_cells, size)
        solved_board = solver.solve()
        solved_string = solved_board.get_single_string()
        #Loop through solved_string to update board[]
        for i, char in enumerate(solved_string):
            board[i] = char
    
    return render(request, "sudoku.html", {'board': board})