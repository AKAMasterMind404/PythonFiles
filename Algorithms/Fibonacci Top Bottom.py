def Fibonacci(N):
    global calls
    calls+=1
    if N <= 1:
        return N
    return Fibonacci(N-1) + Fibonacci(N-2)

def fibMain():
    global sum
    sum+=Fibonacci(i)
    print("Fib{} = {}\n".format(i,Fibonacci(i)))
    return 0

sum=0
calls=0

n=int(input("Enter a value for N:"))

for i in range(n+1):
    fibMain()

print("Sum of first {} fibonacci numbers is {}".format(n,sum))
print("Calls:",calls)