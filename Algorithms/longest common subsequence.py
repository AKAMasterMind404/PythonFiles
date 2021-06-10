def lcs(X, Y, m, n ):
    if not m or not n: # m or n isn't zero
        return 0
    elif X[m - 1] == Y[n - 1]:
        global string
        if X[m-1] not in string:
            string += X[m-1]
        return lcs(X, Y, m - 1, n - 1) + 1

    return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n))

string=''
# X="ABCDGH"
# Y="AEDFHR"

X="AGGTAB"
Y="GXTXAYB"

length=lcs(X, Y, len(X), len(Y))
LCS=string[::-1]
print('String 1: {}\nString 2: {}\n'.format(X,Y))
print('Least common sub sequence is {} having length {}'.format(LCS,length))