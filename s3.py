import socket
import deffieHellman as dh

q=23
alpha=9
b=3

def Main():
   
    host = '192.168.111.1' #Server ip
    port = 4000
    ht = ('192.168.111.1', 4000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    print("Server Started")
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("cipher text received : ",data)
        data= dh.get(int(data),q,b)
        print("Message from: " + str(addr))
        print("key From connected user: " ,data)
        m=dh.send(q,alpha,b)
        m=str(m[0])
        s.sendto(m.encode('utf-8'),ht)
        print("sent text : ",m)
        s.close()
        break

if __name__=='__main__':
    Main()
