import socket
import deffieHellman as dh

q=23
alpha=9
a=4

def Main():
    
    host='192.168.111.1' #client ip
    port = 4005
    
    server = ('192.168.111.1', 4000)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    m=dh.send(q,alpha,a)
    m=str(m[0])
    s.sendto(m.encode('utf-8'), server)
    print("sent text : ",m)
    data= 16
    print("key From connected user: " ,dh.get(data,q,a))
    '''
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("cipher text received : ",data)
        data= dh.get(int(data),q,a)
        print("Message from: " + str(addr))
        print("key From connected user: " ,data)
        s.close()
        '''
    

if __name__=='__main__':
    Main()