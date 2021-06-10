with open('aRough1.py','a') as file:
    file.write("\n")
    i=list(input())
    j=0
    while j<len(i):
        if i[j]==" ":
            i[j]=','
        j+=1
    newlist=("".join(i))
    file.write("\n")
    file.write("l=[{}]\n".format(newlist))
    file.write("for i in l:\n"
               "    print(i)")
    file.write("\n")