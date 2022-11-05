import aes
import des
#avalanch message

keya='This is a key123'
keyd='key12345'

message = "123456xxxxxxxxxx"
bitchangedmssg="223456xxxxxxxxxx"
print("\n\navalanch in aes message changed from ",message,"to ",bitchangedmssg," : ")
c1=aes.encrypt(message,keya)
c2=aes.encrypt(bitchangedmssg,keya)

message = "123456xxxxxxxxxx"
bitchangedmssg="223456xxxxxxxxxx"
print("\n\navalanch in des message changed from ",message,"to ",bitchangedmssg," : ")
c1=des.encrypt(message,keyd)
c2=des.encrypt(bitchangedmssg,keyd)
