for _ in range(int(input())):
    n = int(input())
    _ = input()
    arr = list(map(int, input().split()))
    arr.sort()
    print(sum(arr[_.count('0')::]))