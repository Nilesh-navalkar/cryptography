import math
import random

def getkey():
    p=int(input("enter 1st prime number : "))
    q=int(input("enter 2nd prime number : "))

    n=p*q
    phi=(p-1)*(q-1)
    alle=[]
    for i in range(2,phi):
        if(math.gcd(i,phi)==1):
            alle.append(i)
    e=random.choice(alle)
    e=313
    print("e = ",e)
    ei=pow(e, -1, phi)
    print("einv = ",ei)
    d=ei%phi
    print("d = ",d)

    return (n,e,d)


def encrypt(m,e,n):
    c=pow(int(m),e)%n
    #print("cypertext : ",c)
    return c

def decrypt(c,d,n):
    p=pow(int(c),d)%n
    #print("plaintext : " ,p)
    return p
'''
c=encrypt(message,e,n)
d=decrypt(c,d,n)
'''