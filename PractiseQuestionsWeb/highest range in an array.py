array=[0,9,19,-1,18,17,2,10,3,12,5,16,4,11,8,13,14]
def largestRange(array):
    unique=[]
    for i in array:
        if i not in unique:
            unique.append(i)
    array=unique
    array=sorted(array)
    print(array)
    class numberinfo:
        def __init__(self,start,end,length):
            self.start=start
            self.end=end
            self.length=length

    largest=numberinfo(0,0,1)
    z=0
    while z<len(array):
        streak=1
        tempz=z
        if tempz!=len(array)-1:
            try:
                while array[tempz]==array[tempz+1]-1 and tempz!=len(array)-1:
                    streak+=1
                    tempz+=1
            except IndexError:
                streak+=0
        if streak>largest.length:
            largest.start=z
            largest.end=tempz
            largest.length=streak
        z+=1

    return [array[largest.start],array[largest.end]]
print(largestRange(array))