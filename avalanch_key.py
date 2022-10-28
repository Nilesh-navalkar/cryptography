import aes
import des

keya='This is a key123'
keyd='key12345'
print("\n\navalanch in aes message 1 bit changed : ")
message = "The answer is no"
c1=aes.encrypt(message,keya)
bitchangedkey='This is a key121'
c2=aes.encrypt(message,bitchangedkey)

print("\n\navalanch in des message 1 bit changed : ")
message = "The answer is no"
c1=des.encrypt(message,keyd)
bitchangedkey='key12346'
c2=des.encrypt(message,bitchangedkey)
