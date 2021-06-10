import random as r
#INPUT PRIME NO1
#INPUT PRIME NO2

#CHECK IF P AND Q ARE PRIME

#GENERATE RSA MODULUS: P * Q

#EULERS TOTiENT = (P-1)*(Q-1)

#
def GCD2(a,b):return a if not b else GCD2(b,a%b)

def encrypt(pub_key, n_text):
    e, n = pub_key
    x = []
    m = 0
    for i in n_text:
        if (i.isupper()):
            m = ord(i) - 65
            c = (m ** e) % n
            x.append(c)
        elif (i.islower()):
            m = ord(i) - 97
            c = (m ** e) % n
            x.append(c)
        elif (i.isspace()):
            spc = 400
            x.append(400)
    return x

# Decryption
'''DECRYPTION ALGORITHM'''

def decrypt(priv_key, c_text):
    d, n = priv_key
    txt = c_text.split(',')
    x = ''
    m = 0
    for i in txt:
        if (i == '400'):
            x += ' '
        else:
            m = (int(i) ** d) % n
            m += 65
            c = chr(m)
            x += c
    return x

# Python program to demonstrate working of extended
# Euclidean Algorithm

# function for extended Euclidean Algorithm
def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return 0, 1

    x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return x, y

def isPrime(num):
    for i in range(2,int(1 + num/2)):
        if not num%i:
            return False
    return True

p=int(input("Enter value for p:"))

while not isPrime(p):
    print("Entered number is not prime.Try again!\n")
    p=int(input("Enter value for p:"))

q=int(input("Enter value for q:"))
while not isPrime(q):
    print("Entered number is not prime.Try again!\n")
    q=int(input("Enter value for q:"))

RSA_MODULE= p*q
print("*****************************")
print("RSA module is:",RSA_MODULE)
print("*****************************")
totient=(p-1)*(q-1)
print("Totient is:",totient)
print("*****************************")
#### GENERATION OF e ####

## E = [ 1, totient ] and GCD(E,totient) = 1

e=r.randrange(1,totient)
while GCD2(e,totient)!=1:
    e=r.randrange(1,totient)
print("E IS:",e)
print("*****************************")
ab=gcdExtended(e,totient)
d=ab[1]
print("D IS:",d)
print("*****************************")
##EQUATION
# totient*a2 + e*b2 #EQUATION
ip=input("Enter text here:")
list1=[]
public_key=e,totient
private_key=q,totient

ed=int(input("Enter 1 for encryption, 2 for decryption:"))
if ed==1:
    print("Encrypted Value is:")
    print(encrypt(public_key,ip))
else:
    p_k=tuple(map(int,input()))
    i_p=input("Enter encrypted message numbers separated by space:")
    print("Decrypted value is:")
    print(decrypt(p_k,i_p))