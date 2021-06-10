class Warehouse:
    def setNumberOfEachProductType(self,numbers):
        self.numOfEachProduct=[]
        for i in list(numbers):
            self.numOfEachProduct.append(numbers[i])
        return self.numOfEachProduct
    def setLocation(self,row,column):
        self.location=(row,column)

# class Order:
#     def __init__(self):

r,c,drones,turns,max_payload=map(int, input().split())
number_of_product_types=int(input())
product_corresponding_weights=list(map(int, input().split()))
number_of_warehouses=int(input())

warehouses=[]
for warehouse in range(number_of_warehouses):
    enthWarehouse=Warehouse()
    r,c=map(int, input().split())
    enthWarehouse.setLocation(r,c)
    enthWarehouse.setNumberOfEachProductType(list(map(int,input().split())))
    warehouses.append(enthWarehouse)

number_of_orders=int(input())

for order in range(number_of_orders):
    rd,cd=map(int,input().split())
    numofitems=int(input())
    product_types_in_order=map(int,input())