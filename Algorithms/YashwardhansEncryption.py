import leftrotation as l
import retpyrced as decrypter

###THE SOLVED MESSAGE BY YASHWARDHAN
decryptedText='lobbying is about foresight about anticipating your opponents moves and devising counter measures the winner plots one step ahead of the opposition and plays her trump card just after they play theirs its about making sure you surprise them and they dont surprise you'
decryptionCode=5

myMessage='Lobbying is about foresight about anticipating your opponents moves and devising counter measures the winner plots one step ahead of the opposition:::\nWise words have never been spoken, but be alert whatsoever, for every move played by the opponent can be a misdirection, a decoy that can have the potential to degrade empires, collapse well laid out plans, thus changing a well designed plot, turning it into the demise of the creator. This is a message from the <mASterMiND>! - Not a competitor/rival/enemy XD'
myMessageToggled='LOBbyIng IS About ForeSigHt ABOUT AnTICIPATING yOur OPpoNENTs moVes aNd DEvISiNg cOUNTeR mEASURES THe wiNNEr PLots ONE sTep aheAd of tHe OpPosiTiOn:::WISe WoRds HaVe neVeR bEEN SPOKEN, BuT BE ALErt WHatsOEver, for EVerY MOVe PLAYed by thE oPponenT Can bE A mIsdiREction, a DECoY tHAT CaN hAVE the POTenTIAL tO DEgRAde EmPIREs, CoLLapSe WELl LAid OUT plaNs, THuS cHaNGiNG a wEll DESignED plot, tURNIng iT IntO The DEmIse of ThE crEaTOr. THis IS a MEssAGe FRoM thE <MASTErMiND>! - NOT A CoMPetItor/RivaL/enEMy XD'

myMessageEncrypted='vyllisxq sc klyed pybocsqrd klyed kxdsmszkdsxq iyeb yzzyxoxdc wyfoc kxn nofscsxq myexdob wokceboc dro gsxxob zvydc yxo cdoz krokn yp dro yzzycsdsyx:::xgsco gybnc rkfo xofob loox czyuox, led lo kvobd grkdcyofob, pyb ofobi wyfo zvkion li dro yzzyxoxd mkx lo k wscnsbomdsyx, k nomyi drkd mkx rkfo dro zydoxdskv dy noqbkno owzsboc, myvvkzco govv vksn yed zvkxc, drec mrkxqsxq k govv nocsqxon zvyd, debxsxq sd sxdy dro nowsco yp dro mbokdyb. drsc sc k wocckqo pbyw dro wkcdobwsxn  xyd k mywzodsdyb/bsfkv/oxowi hn'

###MY MESSAGE ORIGINAL AS WELL AS ENCRYPTED

def multiRotate(list1,n):
    for i in range(n):
        list1=l.leftrotate(list1)
    return list1

#PROBLEM TEXT
text='Yboolvat vf nobhg sberfvtug nobhg nagvpvcngvat lbhe bccbaragf zbirf naq qrivfvat pbhagre zrnfherf Gur jvaare cybgf bar fgrc nurnq bs gur bccbfvgvba naq cynlf ure gehzc pneq whfg nsgre gurl cynl gurvef Vgf nobhg znxvat fher lbh fhecevfr gurz naq gurl qbag fhecevfr lbh'

keys=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
characters=['.', ',', '/', '(', ')', ':',' ']
numbers=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
dic={}

for n in range(27): #CONTROLS THE SHIFT OF KEYS AND VALUES SHIFT 0 = {a:a, b:b}
    z=0
    while z<len(keys):
        dic[keys[z]]=multiRotate(keys,n)[z]
        z+=1

    decrypter.decrypter(text,dic) #TEXT TO DECRYPT
    print()
    print('n is:', n)
    print()
    print()