def isPallindrome(text):
    if str(text)==str(text)[::-1]:
        return True
    return False

def isPlainInt(num):
    if int(num)==num:
        return int(num)
    return num

L=int(input())
R=int(input())

sp=0

for i in range(L,R):
    if isPallindrome(i) and isPallindrome(isPlainInt(i**0.5)):
            print(i)
            sp+=1

print(sp)