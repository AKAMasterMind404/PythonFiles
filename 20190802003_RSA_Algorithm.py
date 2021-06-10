#GCD
def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e

#Euclid's Algorithm
def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            # if(b!=0):
            #     print("%d = %d*(%d) + %d"%(r,a,e,b))
            r=e
            e=b

#Extended Euclidean Algorithm
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        # print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)

#Multiplicative Inverse
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
    #     if(s<0):
    #         print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%r))
    #     elif(s>0):
            # print("s=%d."%(s))
        return s%r

def decrypt(priv_key,c_text):
    d,n=priv_key
    txt=c_text.split(',')
    x=''
    m=0
    for i in txt:
        if(i=='400'):
            x+=' '
        else:
            m=(int(i)**d)%n
            m+=65
            c=chr(m)
            x+=c
    return x

def encrypt(pub_key,n_text):
    e,n=pub_key
    x=[]
    m=0
    for i in n_text:
        if i.isupper():
            m = ord(i)-65
            c=(m**e)%n
            # print("c encr",c)
            x.append(c)
        elif i.islower():
            m= ord(i)-97
            c=(m**e)%n
            # print("c encr",c)
            x.append(c)
        elif(i.isspace()):
            spc=400
            x.append(400)
    return x

def isPrime(num):
    for i in range(2,int(1 + num/2)):
        if not num%i:
            return False
    return True

if __name__=="__main__":
    p = int(input("Enter value for p:"))

    while not isPrime(p):
        print("Entered number is not prime.Try again!\n")
        p = int(input("Enter value for p:"))

    q = int(input("Enter value for q:"))
    while not isPrime(q):
        print("Entered number is not prime.Try again!\n")
        q = int(input("Enter value for q:"))

    RSA_MODULE = p * q
    print("*****************************")
    print("RSA module is:", RSA_MODULE)
    print("*****************************")
    totient = (p - 1) * (q - 1)
    print("Totient is:", totient)
    print("*****************************")

    e = 1
    for i in range(1, 1000):
        if (egcd(i, totient) == 1):
            e = i
    print("The value of e is:", e)
    print("*****************************************************")
    eugcd(e, totient)
    d = mult_inv(e, totient)
    print("The value of d is:", d)
    print("*****************************************************")
    public_key = (e, RSA_MODULE)
    private_key = (d, RSA_MODULE)

    print("Private Key is:", private_key)
    print("Public Key is:", public_key)
    print("*****************************************************")
    ip = input("Enter text here:")

    ed = int(input("Enter 1 for encryption, 2 for decryption:"))
    if ed == 1:
        print("Encrypted Value is:")
        print(encrypt(public_key, ip))
    else:
        # p_k = tuple(map(int, input()))
        print("Decrypted value is:")
        print(decrypt(private_key, ip))