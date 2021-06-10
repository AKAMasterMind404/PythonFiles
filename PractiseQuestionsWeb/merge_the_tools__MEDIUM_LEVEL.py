def merge_the_tools(string, k):
    string = list(string)
    z=0
    while True:
        sub=string[z:z+k]
        if sub!=[]:
            temp=[]
            for i in sub:
                if i not in temp:
                    temp.append(i)
                    print(i,end='')
            print()
            z+=k
        else:
            break
merge_the_tools("AABCAAADA",3)