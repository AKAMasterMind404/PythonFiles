# Enter your code here. Read input from STDIN. Print output to STDOUT
stack=[]
inp=input()
l=len(inp)
i=0
while i<l:
    isIncr=False
    ele=inp[i]
    z=0
    while i<l and ele==inp[i]:
        z+=1
        i+=1
        isIncr=True
    if not isIncr:
        i+=1
    stack.append((z,ele))
print(stack)