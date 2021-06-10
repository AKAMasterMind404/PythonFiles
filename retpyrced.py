def decrypter(text,dict):
    def decrpyt(i,n):
        def rep(i):
            # dict={'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','j':'m','k':'n','l':'o','m':'p','n':'q',
            #       'o':'r','p':'s','q':'t','r':'u','s':'v','t':'w','u':'x','v':'y','w':'z','x':'a','y':'b','z':'c',' ':' ',
            #       '1':'3','2':'4','3':'5','4':'6','5':'7','6':'8','7':'9','8':'0','9':'1','0':'2','.':'.',',':',','/':'/',
            #       '(':'(',')':')',':':':'}
            output=''
            for inputt in i.lower():
                try:
                    output+=dict.get(inputt)
                except TypeError:
                    output+=' '
            return output
        for j in range(0,n):
            i=rep(i)
        return i

    print(decrpyt(text,1))
    # for n in range(0,27):
    #     #n=int(input('Enter decryption code:'))
    #     print(decrpyt(text,n))
#
# s='Yboolvat vf nobhg sberfvtug, nobhg nagvpvcngvat lbhe bccbarag’f zbirf, naq qrivfvat pbhagre zrnfherf. Gur jvaare cybgf bar fgrc nurnq bs gur bccbfvgvba naq cynlf ure gehzc pneq whfg nsgre gurl cynl gurvef. Vg’f nobhg znxvat fher lbh fhecevfr gurz, naq gurl qba’g fhecevfr lbh'
#
#
# decrypter(s)