from Algorithms import Greatest_Common_Divisor as g
import random as r

with open('aRough4.py', 'r') as nf:
    outputFile = open('op1.txt', 'w+')
    inputFile = open('ip1.txt','w+')
    c = 0
    for a, b in enumerate(nf):
        # print(a,b.strip())
        if not a % 2:
            # JUMP SIZE
            j1, j2 = map(int, b.strip().split())
            # print(arr)
        else:
            arr = sorted(list(map(int, b.strip().split()))[0:-1:])
            [inputFile.write(str(item) + ' ') for item in arr]
            inputFile.write('-1 \n')

            # outputFile.write(str(j1) + " " + str(j2) + '\n')
            # ARRAY
            dec = g.gcd(j1, j2)
            print(j1,j2,"::",dec)
            inputFile.write(str(j1)+" "+str(j2)+"\n")
            print(arr)
            ans = "Alive"
            for ele in arr:
                if ele and not ele%dec:
                    print(ele)
                    ans = "Dead"
                    break
            print(ans)
            print()
            outputFile.write(ans + '\n')
            c += 1
print(c)
