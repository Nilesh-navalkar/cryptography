# keyed transposition cipher
#key=[2,0,3,4,1]

#p="enemy attacks tonight"

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
    #print(cwords)
    c=""
    for i in range(0,len(key)):
        for word in cwords:
            c=c+word[i]
    return c

def decrypty(p,key):
    cols=len(p)//len(key)
    #print(len(key))
    blocks=[]
    for i in range(cols,len(p)+1,cols):
        blocks.append(p[ i-cols: i])
    cblocks=[]
    #print(blocks)
    for i in range(0,len(blocks)):
        cblocks.append(blocks[key.index(i)])

    c=""
    for i in range(0,cols):
        for word in cblocks:
            c=c+word[i]
            


    return c

#encrypty(p,key)
#encrypty("lhloerwldozhzzi",key)
#decrypty("isxapocsdswxbar",[3,0,2,4,1])