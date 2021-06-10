import os
def designerPdfViewer(h, word):
    wordDict={}
    begin=97
    for i in h:
        wordDict[chr(begin)]=i
        begin+=1

    l=wordDict[word[0]]

    for i in word:
        if wordDict[i]>l:
            l=wordDict[i]
    return l*len(word)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
    print(result)