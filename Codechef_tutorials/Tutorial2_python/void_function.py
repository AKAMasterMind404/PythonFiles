def removeTattoo():
    global skin
    skin='regular skin'

skin='tattooed skin'

print('value of skin before using the function:',skin)

removeTattoo()

print('value of skin after using the function:', skin)

arr=[1,2,3,4,5,6,7]

# def printMiddleElement():
#     global arr
#     length=len(arr) # 7
#
#     middleIndex=length//2 # Floor divide
#
#     element=arr[middleIndex]
#
#     print(element)
#
#
# printMiddleElement()