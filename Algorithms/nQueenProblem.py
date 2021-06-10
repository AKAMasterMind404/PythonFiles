def printBoard(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def prevCheck(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, col):
    if col >= N:
        return True

    for i in range(N):

        if prevCheck(board, i, col):

            board[i][col] = 1

            if solve(board, col + 1) == True:
                return True

            board[i][col] = 0

    return False

def main():

    board=[[0 for i in range(N)] for i in range(N)]

    if solve(board, 0) == False:
        print("Solution does not exist")
        return False

    printBoard(board)
    return True

if __name__=='__main__':
    # N = int(input("Enter a value for N:"))
    for N in range(1,10):
        print('#################')
        main()
        # print('#################')