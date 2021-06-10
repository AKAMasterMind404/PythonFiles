# Complete the solve function below.
def solve(s):
    s=' '+s
    for i in range(len(s)):
        if s[i-1]==' ' and s[i]!=' ':
                albhabet=s[i].upper()
                temp=list(s)
                temp[i]=albhabet
                s=''.join(temp)
    return s[1::]

if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result)