# transposition cipher
key=[2,0,3,4,1]

p="hello world"

def encrypty(p,key):
    p=p.replace(" ","")
    if(len(p)%len(key)!=0):
        while(len(p)%len(key)!=0):
            p=p+"z"
    #print(p)
    blocks=[]
    for i in range(5,len(p)+1,len(key)):
        blocks.append(p[ i-5: i])
    cwords=[]
    #print(blocks)
    for word in blocks:
        cword=""
        for i in key:
            cword=cword+word[i]
        cwords.append(cword)
    c=""
    for i in cwords:
        c=c+i
    return c

def decrypty(p,key):
    blocks=[]
    for i in range(5,len(p)+1,len(key)):
        blocks.append(p[ i-5: i])
    cwords=[]
    #print(blocks)
    for word in blocks:
        cword=""
        for i in range(0,len(key)):
            cword=cword+word[key.index(i)]
        cwords.append(cword)
    c=""
    for i in cwords:
        c=c+i
    return c

encrypty(p,key)
decrypty("lhloerwldo",key)