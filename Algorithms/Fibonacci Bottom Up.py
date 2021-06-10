l=[0,1]

n=int(input("Enter a value for N:"))

print('\nFib{} = {}\n'.format(0,0)) #Initial values
print('Fib{} = {}\n'.format(1,1)) #Initial values

for i in range(n-1):
    print('Fib{} = {}\n'.format(i+2,l[-1]+l[-2]))
    l.append(l[-1]+l[-2])

print("\nSum of first {} fibonacci numbers is {}".format(n,sum(l)))
