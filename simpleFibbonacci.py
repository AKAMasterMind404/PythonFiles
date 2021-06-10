a=[0.0,1.0]

k=float(input())
z=0
while True:
    if z<k:
        n=a[z]+a[z+1]
        a.append(n)
        z+=1
        print(n)
    else:
        break