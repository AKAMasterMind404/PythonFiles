def mergeSort(l1,l2):
    p1 = 0
    p2 = 0
    srtd = []
    while len(srtd)!=len(l1)+len(l2):
        if p1==len(l1):
            srtd.append(l2[p2])
            p2+=1
        elif p2==len(l2):
            srtd.append(l1[p1])
            p1+=1
        else:
            if l1[p1]>l2[p2]:
                srtd.append(l2[p2])
                p2+=1
            else:
                srtd.append(l1[p1])
                p1+=1
    return srtd

def allSort(listOfLists):
    z=0
    while z<len(listOfLists)-1:
        listOfLists[z+1]=mergeSort(listOfLists[z],listOfLists[z+1])
        z+=1
    return listOfLists[len(listOfLists)-1]

l1=[1,2,3,4,5,6,7,9,90,782,8071,80731]
l2=[0,8,9,66,467,9653,1,98]
l3=[65,75764,86,80731,758]
