def getRow(r, r_mid):
    if r<r_mid:
        return r*3
    elif r>r_mid:
        diff = r-r_mid
        return getRow(r_mid - diff,r_mid)
        # return getRow(2 * r_mid - r, r_mid)
    return 0

def printDoormat(n,m):
    row_mid=n//2
    column_mid=m//2

    w='WELCOME'

    design='.|.'

    for row in range(n):
        for column in range(m):
            if row==row_mid and column in range(column_mid-3,column_mid+4):
                print(w[abs(-column + column_mid-3)],end='')
                #WELCOME
            else:
                factor=getRow(row,row_mid)

                var1=column_mid - 1 - factor
                var2=column_mid + 1 + factor + 1#upper limit in inclusive

                if column in range(var1,var2):
                    print(design[column%3],end='')
                else:
                    print('-',end='')
        print()

def myEffiecientSolution(n,m):
    [print('-' * (m // 2 - 1 - i * 3) + '.|.' * (2 * i + 1) + '-' * (m // 2 - 1 - i * 3)) for i in range(n // 2)]
    print('-' * ((m - 7) // 2) + 'WELCOME' + '-' * ((m - 7) // 2))
    [print('-' * (m // 2 - 1 - i * 3) + '.|.' * (2 * i + 1) + '-' * (m // 2 - 1 - i * 3)) for i in range(n // 2 - 1, -1, -1)]
if __name__=='__main__':
    n, m = map(int, input().split())
    # printDoormat(n,m)
    myEffiecientSolution(n,m)