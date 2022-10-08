import socket
import playfair as e
import keycoltransposition as t
k=[["r","p","m","l","d"],["s","a","x","i","c"],["h","k","q","u","y"],["e","w","o","z","g"],["b","f","t","v","n"]]
key=[2,0,3,4,1]
#encrypty(p,k)
def Main():
   
    host = '192.168.111.1' #Server ip
    port = 4000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server Started")
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        data= t.decrypty(data,key)
        data= e.decrypty(data,k)
        print("Message from: " + str(addr))
        print("From connected user: " + data)
    c.close()

if __name__=='__main__':
    Main()
