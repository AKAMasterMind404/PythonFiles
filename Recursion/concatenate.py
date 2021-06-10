def concat(string,s):
    for i in string:
        if type(i)==str:
            s+=i
        else:
            s=concat(i,s)
    return s
print(concat(['a','b','c',['d',['g'],'e'],'f'],''))