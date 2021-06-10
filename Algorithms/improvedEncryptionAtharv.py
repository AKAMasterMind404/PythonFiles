def encr(txt):
    import random as r
    key=r.randint(1,99999999999999999999999999999999999999999999999999999999999)
    # print(key)
    en=''
    for i in txt:
        en += str(ord(i) + key) + ' '
        # if i!=' ':
        #     en+=str(ord(i)+key)+' '
        # else:
        #     en+=str(i)+' '
    # print(en)
    return en,key

def decr(txt,key):
    dr=''
    for j in txt.split(' '):
        if j.isnumeric():
            # print("tru")
            # print("this is j",int(j))
            dr += chr(int(j) - key)
        # for j in i.split():
        #     if j.isnumeric():
        #         dr+=chr(int(j)-key)
            # else:
            #     dr+=' '
        # dr+=' '
    return dr

if __name__=='__main__':
    e,key=encr('My name is Atharv')
    # print(e)
    print(decr(e,key))
    # print(ord('a'))
    # print(chr(ord('a')))
    # myVar = str(ord('y') + 40000000000)
    # print(myVar)
    # print(chr(int(myVar) - 40000000000))
    # print(chr(ord('a') - 20000))