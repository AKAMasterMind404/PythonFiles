from collections import Counter

if __name__ == '__main__':
    s = input()
    s=sorted(s)

    trav=[]
    top_counts=sorted(Counter(s).values())[::-1]

    ans=[]
    for i in top_counts:
        for j in s:
            if j not in trav and s.count(j)==i:
                ans.append((j,i))
                trav.append(j)

    for i in range(3):
        print(ans[i][0],ans[i][1])