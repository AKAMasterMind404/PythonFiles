from SortingAlgorithm import SortingData as s
matrix=[
    [1,0,0,1,0],
    [1,0,1,0,0],
    [0,0,1,0,1],
    [1,0,1,0,1],
    [1,0,1,1,0]
        ]
def function(matrix):
    def adchk(i,j):
        c=[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
        for k in c:
            obj=get(k[0],k[1])
            if obj!=None and obj.activity==True:
                return obj
    def get(i,j):
        x=None
        for k in listofobj:
            if k.i==i and k.j==j:
                x=k
                break
        return x
    class ij:
        def __init__(self,i,j,val,activity):
            self.i=i
            self.j=j
            self.val=val
            self.activity=activity

    def init():
        iv=0
        for i in matrix:
            jv=0
            for j in i:
                ac=True
                if j==0:
                    ac=False
                listofobj.append(ij(iv,jv,j,ac))
                jv+=1
            iv+=1
    listofobj=[]
    listoflengths=[]
    init()
    z=0
    while z<len(listofobj):
        ob=listofobj[z]
        if ob.activity==True:
            riverlength=1
            while True:
                if adchk(ob.i, ob.j) != None:
                    ob.activity=False
                    ob=adchk(ob.i,ob.j)
                    riverlength+=1
                else:
                    ob.activity=False
                    listoflengths.append(riverlength)
                    break
        z+=1
    listoflengths.sort()
    return listoflengths

print(function(matrix))