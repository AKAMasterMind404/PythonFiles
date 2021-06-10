k=0
def search(array,element,k):
    if len(array)==0:return None
    if array[0]==element:
        print("Element:",array[0],k)
    else:
        search(array[1::],element,k+1)
search([1,2,3,4,5],3,k)