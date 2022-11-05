import random 

#q=int(input("enter a prime no : "))

def checkdistinct(residue):
    if(len(residue)==len(set(residue))):
        return True
    else:
        return False

def checkprimroot(n):
    residue=[]
    for i in range(1,q):
        residue.append(pow(n,i)%q)

    if(checkdistinct(residue)):
        return True
    else:
        return False

def getprimroot(q):
    for i in range(2,q):
        if(checkprimroot(i)):
            return i

def send(q,alpha,ya):
    #alpha=getprimroot(q)
    #alpha=9
    avail=[]
    for i in range(1,q):
        avail.append(i)
    #print(alpha)
    #ya=random.choice(avail)
    #ya=4
    #print(ya)
    return (pow(alpha,ya)%q,ya,q)

def get(y,q,ya):
    return pow(y,ya)%q

#y=send(23)
#print(send(23))#(6, 4, 23)   (16, 3, 23)
#print(get(16,23,4))