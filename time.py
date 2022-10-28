import time
import aes
import des


keya='This is a key123'
keyd='key12345'
message = "The answer is no"
start=time.time()
c=aes.encrypt(message,keya)
stop=time.time()
print("encryption time for aes : ",stop-start)


start1=time.time()
pt=aes.decrypt(c,keya)
stop1=time.time()
print("decryption time for aes : ",stop1-start1)


start=time.time()
c=des.encrypt(message,keyd)
stop=time.time()
print("encryption time for des : ",stop-start)



start1=time.time()
pt=des.decrypt(c,keyd)
stop1=time.time()
print("decryption time for des : ",stop1-start1)
