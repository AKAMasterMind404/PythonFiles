def bracketCheck(s):
    stack = []
    comp = {')': '(', '}': '{', ']': '['}

    for c in s:
        if c in ['(', '{', '[']:
            stack.append(c)
        elif c in [')', '}', ']']:
            if len(stack) > 0 and stack[-1] == comp.get(c):
                stack.pop()
            else:
                stack.append(c)
        elif c == ' ':
            pass
        else:
            return False
        print(stack)
    return stack == []


ans = bracketCheck('{{   }}')
print(ans)

'''
We begin by initializing an empty stack in form of python 
list. We now iterate over the string and begin checking for
conditions. If the current character is a left bracket, we 
simply add it to the stack. If its a space we pass and if its
not a right bracket then we return false indicating an invalid
input. If its a right bracket however, we check whether the 
top of the stack contains the complimentary character if the
current character. If it does, then we simply pop the top
element of the stack. 

By the end of the loop, if the stack is empty, then it implies
that every left bracket has a corresponding right bracket
and that the bracket sequence or the input is rightly ordered.
If not then every bracket does not have a corresponding bracket.

A DICTIONARY IS USED TO CHECK IF A COMPLIMENTARY BRACKET
EXISTS AS IT TELLS US THAT IN CONSTANT TIME
'''