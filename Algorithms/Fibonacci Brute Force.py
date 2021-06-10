def fibonacci(n):
    if n<=1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def main(n):
    global sum
    for i in range(n):
        print("\nFib{} = {}".format(i,fibonacci(i)))
        sum+=fibonacci(i)


n=int(input("Enter a value for N:"))

sum=0
main(n)

print("\nSum of first {} fibonacci numbers is {}".format(n,sum))
