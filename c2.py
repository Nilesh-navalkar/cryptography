import socket
import rsa as r

def Main():

    host='192.168.111.1' #client ip
    port = 4005
    
    server = ('192.168.111.1', 4000)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    n=33
    e=7
    message = input("-> ")
    m=r.encrypt(message,e,n)
    m=str(m)
    s.sendto(m.encode('utf-8'), server)
    print("sent cipher text : ",m)
    s.close()

if __name__=='__main__':
    Main()