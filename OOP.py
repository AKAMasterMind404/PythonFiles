class a:
    def __init__(self):
        a=self.name='Navin'
        b=self.age=20
    def compare(self,other):
        if self.age==other.age:
            print('Same ages')
        elif self.age>other.age:
            print(self.name,' has greater age.')
        else:
            print(other.name,' has greater age.')

c1=a()
c2=a()
c3=a()
c2.age=28
c2.name='Pravin'

c3.name='Akash'
c3.age=28

c2.compare(c3)

class t:
    def largercheck(self,a,b):
        self.number1 = int(a)
        self.number2 = int(b)
        num1=self.number1
        num2=self.number2
        if num1>num2:
            print(num1,' is greater.')
        else:
            print(num2,' is greater')

ob1=t()
ob1.largercheck(6,7)

ob2=t()
ob2.largercheck(10,8)



