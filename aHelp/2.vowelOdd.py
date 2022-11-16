def vowelCheck(s: str):
    vow_count = 0

    for char in s:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            vow_count += 1
    return vow_count % 2 == 1


ans = vowelCheck('Week')
print(ans)

'''
We initialize a counter with 0. And iterate over
the string. The current string is normalized using
lower() method. If its a Vowel ie. a,e,i,o or u 
then we increment the counter. Lastly, we return
whether the counter summed up to an odd integer or
not.
'''