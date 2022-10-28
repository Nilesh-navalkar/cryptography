import socket
import rsa as r

def Main():
   
    host = '192.168.111.1' #Server ip
    port = 4000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server Started")
    while True:
        data, addr = s.recvfrom(1024)
        n=33
        d=3
        data = data.decode('utf-8')
        print("cipher text received : ",data)
        data= r.decrypt(int(data),d,n)
        print("Message from: " + str(addr))
        print("decrypted From connected user: " ,data)
    c.close()

if __name__=='__main__':
    Main()
