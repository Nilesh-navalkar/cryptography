import socket
import exp1 as e
import exp1tras as t
k=[["r","p","m","l","d"],["s","a","x","i","c"],["h","k","q","u","y"],["e","w","o","z","g"],["b","f","t","v","n"]]
key=[2,0,3,4,1]
#encrypty(p,k)
def Main():

    host='192.168.111.1' #client ip
    port = 4005
    
    server = ('192.168.111.1', 4000)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    
    message = input("-> ")
    m=e.encrypty(message,k)
    m=t.encrypty(m,key)

    s.sendto(m.encode('utf-8'), server)
    s.close()

if __name__=='__main__':
    Main()