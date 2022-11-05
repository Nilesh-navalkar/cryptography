#digital signatures using rsa
from rsa1 import encrypt,decrypt,getkey


def signing(n,d,m):
    return encrypt(m,d,n)

def verify(n,e,s):
    return decrypt(s,e,n)
    
keys=getkey()  #n e d
m=19070
s=signing(keys[0],keys[2],m)
print("signature : ",s)
print("after verification : ",verify(keys[0],keys[1],s))