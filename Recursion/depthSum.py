def depthSum(arr,l,depth):
    for i in arr:
        if type(i)==int:
            l.append(i)
        elif type(i)==list:
            depth+=1
            l,depth=depthSum(i,l,depth)
    return l,depth

l= [1,[2,[3,[4,[5,[6,[7,[8,[9,[10]]]]]]]]]]
print(depthSum(l,[],1))