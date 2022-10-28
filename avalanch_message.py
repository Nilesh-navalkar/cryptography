import aes
import des
keya='This is a key123'
keyd='key12345'
print("\n\navalanch in aes message 1 bit changed : ")
message = "The answer is no"
c1=aes.encrypt(message,keya)
bitchangedmssg="The answer in no"
c2=aes.encrypt(bitchangedmssg,keya)

print("\n\navalanch in des message 1 bit changed : ")
message = "The answer is no"
c1=des.encrypt(message,keyd)
bitchangedmssg="The answer in no"
c2=des.encrypt(bitchangedmssg,keyd)
