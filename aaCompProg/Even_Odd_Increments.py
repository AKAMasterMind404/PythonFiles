for _ in range(int(input())):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    num_odd_nums = 0
    num_even_nums = 0

    sum_odd = 0
    sum_even = 0

    for num in arr:
        if num % 2 == 0:
            num_even_nums += 1
            sum_even += num
        else:
            num_odd_nums += 1
            sum_odd += num

    for __ in range(q):
        i, j = map(int, input().split())

        if i == 0:
            if j % 2 == 0:
                sum_even += j * num_even_nums
            else:
                sum_odd += sum_even + (j * num_even_nums)
                sum_even = 0
                num_odd_nums += num_even_nums
                num_even_nums = 0
        elif i == 1:
            if j % 2 == 0:
                sum_odd += j * num_odd_nums
            else:
                sum_even += sum_odd + (j * num_odd_nums)
                sum_odd = 0
                num_even_nums += num_odd_nums
                num_odd_nums = 0

        print(sum_even + sum_odd)