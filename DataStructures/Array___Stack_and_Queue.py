class Array:
    def __init__(self,list1):
        self.array=list1
        self.top=len(list1)
    def length(self):
        return len(self.array)
    def insert(self,element):
        self.array.append(None)
        self.array[self.top]=element
        self.top+=1
        return self.array
    def getArray(self):
        return self.array
    def pop(self):
        if self.top>0:
            element=self.array[self.top-1]
            self.array=self.array[0:len(self.array)-1]
            self.top-=1
            return element
        else:
            print("Stack Underflow")
    def dequeue(self):
        self.top-=1
        element=self.array[0]
        self.array=self.array[1::]
        return element
class xyz:
    def __init__(self):
        self.x=1