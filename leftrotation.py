
###################################
def leftrotate(list1):
    #init
    lenoflist=len(list1)
    empty=[]
    for i in range(0,lenoflist):
        empty.append('')
        if i+1!=lenoflist:
            empty[i]=list1[i+1]
        else:
            empty.append('')
            empty[i]=list1[0]
    r=[]
    for i in empty:
        if i!='':
            r.append(i)
    return r
###################################
# l=[]
# n1=input('Enter numbers separated by spaces:')
# for i in n1:
#     if i!=' ':
#         l.append(int(i))
# print('The list is as follows:',l)
# nor=int(input('Enter number of left rotations you want to perform:'))
# while nor>0:
#     l=leftrotate(l)
#     nor-=1
# print(l)