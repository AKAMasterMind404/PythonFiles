def digitSum(a1: list, a2: list):
    a = ""
    b = ""
    for i in a1:
        a += str(i)
    # [1, 2, 3] becomes '123'
    for i in a2:
        b += str(i)

    num1 = int(a)
    num2 = int(b)

    final = num1 + num2

    anslist = []

    final = str(final)

    for i in final:
        anslist.append(int(i))

    return anslist


ans = digitSum([9, 9, 9], [1, 1, 1])
print(ans)

'''
We initialize two empty strings and iterate
over each input array. In each iteration we
append the digit to the empty strings by converting
it into strings first. We then convert these
two strings to integers and add them. We now
initialize a stack to append our answer. But
since integers are not iterable, we first convert
it into a string and iterate over it. In Each iteration
we convert the character into integer and append it
to the stack and return it.
'''