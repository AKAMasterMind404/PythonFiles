def decimal(num):
    if 'b' in str(num):
        x=str(num)[2::][::-1]
    else:
        x=str(num)[::-1]
    s=0
    for i in range(len(x)):
        if int(x[i]):
            s+=2**i
    return s

def bi(n):
    return int(bin(n)[2::])
