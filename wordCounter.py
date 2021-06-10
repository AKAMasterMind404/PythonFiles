with open('thetext.txt', 'r') as fi:
    words = 0
    for i in fi: words += len(i.strip().split())
    print(words)
