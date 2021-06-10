def subs(inp):
    occured=[inp]
    for i in range(len(inp)):
        if i not in occured:
            occured.append(inp[i])
            # print(inp[i])
        z=0
        while z<i:
            giv=inp[z:i]
            if giv not in occured:
                occured.append(giv)
                # print(occured)
            z+=1

        z=1
        while z < len(inp):
            giv = inp[z::]
            if giv not in occured:
                occured.append(giv)
                # print(occured)
            z += 1
    return sorted(list(set(occured)))
if __name__=="__main__":
    print(subs(input()))