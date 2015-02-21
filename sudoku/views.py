from django.shortcuts import render
import board

# Create your views here.
def sudoku(request):
    loop_range = range(1,10) #Range is exclusive, this gives 1-9
    #import board.py
    #Get input to use as the board
    #Run solve with the input board
    #return solved board and render it
    
    #Get input to use as board
    
    return render(request, "sudoku.html", {'loop_range': loop_range})