import math
import random
'''
***key generation***
p=int(input("enter 1st prime number : "))
q=int(input("enter 2nd prime number : "))

n=p*q
phi=(p-1)*(q-1)
alle=[]
for i in range(2,phi):
    if(math.gcd(i,phi)==1):
        alle.append(i)
#print(alle)
e=random.choice(alle)
#e=3
#print("e = ",e)
ei=pow(e, -1, phi)
#print("einv = ",ei)
d=ei%phi
#print("d = ",d)

message="p"
'''
def encrypt(message,e,n):
    message=message.replace(" ","")
    m=""
    for i in message:
        if(len(str(ord(i)-ord("a")))==1):
            ele="0"+str(ord(i)-ord("a"))
            m=m+ele
        else:
            ele=str(ord(i)-ord("a"))
            m=m+ele

    #print(m)

    c=pow(int(m),e)%n
    #print("cypertext : ",c)
    return c

def decrypt(c,d,n):
    p=pow(int(c),d)%n
    o=ord("a")+p
    #print("plaintext : " ,p)
    return chr(o)

#c=encrypt(message,e,n)
#d=decrypt(c,d,n)
