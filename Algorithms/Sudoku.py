SIZE = 9
#sudoku problem

matrix=[
[5,1,7,6,0,0,0,3,4],
[2,8,9,0,0,4,0,0,0],
[3,4,6,2,0,5,0,9,0],
[6,0,2,0,0,0,0,1,0],
[0,3,8,0,0,6,0,4,7],
[0,0,0,0,0,0,0,0,0],
[0,9,0,0,0,0,0,7,8],
[7,0,3,4,0,0,5,6,0],
[0,0,0,0,0,0,0,0,0]
]

def sudoku_main():
    row = 0
    col = 0

    a = number_unassigned(row, col)
    if a[2] == 0:
        return True
    row = a[0]
    col = a[1]

    for i in range(1,10):

        if safeCheck(i, row, col):
            matrix[row][col] = i
            #backtracking
            if sudoku_main():
                return True
            #f we can't proceed with this solution
            #reassign the cell
            matrix[row][col]=0
    return False

#function to print sudoku
def sudokuPrinter():
    for i in matrix:
        print(i)

def number_unassigned(row, col):
    num_unassign = 0
    for i in range(SIZE):
        for j in range (SIZE):
            #cell is unassigned
            if matrix[i][j] == 0:
                row = i
                col = j
                num_unassign = 1
                a = [row, col, num_unassign]
                return a
    a = [-1, -1, num_unassign]
    return a

def safeCheck(n, r, c):

    for i in range(SIZE):
        if matrix[r][i] == n:
            return False

    for i in range(SIZE):
        if matrix[i][c] == n:
            return False

    row_start = (r//3)*3
    col_start = (c//3)*3

    for i in range(row_start,row_start+3):
        for j in range(col_start,col_start+3):
            if matrix[i][j]==n:
                return False
    return True

if __name__=='__main__':
    if sudoku_main():
        sudokuPrinter()
    else:
        print("Solution does not exist")