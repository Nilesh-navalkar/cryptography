#playfair substitution cipher
#p="hello world"

#print(p)
def find(element, matrix):
    for i, matrix_i in enumerate(matrix):
        for j, value in enumerate(matrix_i):
            if value == element:
                return (i, j)
                
def encrypty(p,key):
    p=p.replace(" ","")
    if(len(p)%2!=0):
        p=p+"z"
    #print(p)
    blocks=[]
    for i in range(2,len(p)+1,2):
        blocks.append(p[ i-2: i])
    cblocks=[]
    for i in range(0,len(blocks)):
        if(blocks[i][1]==blocks[i][0]):
            b1=blocks[i][0]+"z"
            b2=blocks[i][1]+"z"
            cblocks.append(b1)
            cblocks.append(b2)
        else:
            cblocks.append(blocks[i])

    c=""
    for i in cblocks:
            p1=find(i[0],key)
            p2=find(i[1],key)
            if p1[0]==p2[0]:
                if(p1[1]==4):
                    c=c+key[p1[0]][0]
                    c=c+key[p2[0]][p2[1]+1]
                elif(p2[1]==4):
                    c=c+key[p1[0]][p1[1]+1]
                    c=c+key[p2[0]][0]
                else:
                    c=c+key[p1[0]][p1[1]+1]
                    c=c+key[p2[0]][p2[1]+1]
            elif p1[1]==p2[1]:
                if(p1[0]==4):
                    c=c+key[0][p1[1]]
                    c=c+key[p2[0]][p2[1]]
                elif(p2[0]==4):
                    c=c+key[p1[0]][p1[1]]
                    c=c+key[0][p2[1]]
                else:
                    c=c+key[p1[0]+1][p1[1]]
                    c=c+key[p2[0]+1][p2[1]]               
            else:
                c=c+key[p1[0]][p2[1]]
                c=c+key[p2[0]][p1[1]]
    #print(cblocks)
    #print(c)

    return c

    #print(cblocks)

                
def decrypty(p,key):
    print(p)
    blocks=[]
    for i in range(2,len(p)+1,2):
        blocks.append(p[ i-2: i])
    cblocks=blocks
    c=""
    for i in cblocks:
            p1=find(i[0],key)
            p2=find(i[1],key)
            if p1[0]==p2[0]:
                if(p1[1]==0):
                    c=c+key[p1[0]][4]
                    c=c+key[p2[0]][p2[1]-1]
                elif(p2[1]==0):
                    c=c+key[p1[0]][p1[1]-1]
                    c=c+key[p2[0]][4]
                else:
                    c=c+key[p1[0]][p1[1]-1]
                    c=c+key[p2[0]][p2[1]-1]
            elif p1[1]==p2[1]:
                if(p1[0]==0):
                    c=c+key[4][p1[1]]
                    c=c+key[p2[0]][p2[1]]
                elif(p2[0]==0):
                    c=c+key[p1[0]][p1[1]]
                    c=c+key[4][p2[1]]
                else:
                    c=c+key[p1[0]-1][p1[1]]
                    c=c+key[p2[0]-1][p2[1]]               
            else:
                c=c+key[p1[0]][p2[1]]
                c=c+key[p2[0]][p1[1]]
    #print(cblocks)
    #print(c)

    return c

    

#k=[["r","p","m","l","d"],["s","a","x","i","c"],["h","k","q","u","y"],["e","w","o","z","g"],["b","f","t","v","n"]]
#encrypty(p,k)
#decrypty("ebivivzoemdr",k)
