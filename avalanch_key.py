import aes
import des

#avalanch key

keya='This is a key123'
bitchangedkey='This is a kfy123'
print("\n\navalanch in aes key changed from ",keya,"to ",bitchangedkey," : ")
message = "123456xxxxxxxxxx"
c1=aes.encrypt(message,keya)
c2=aes.encrypt(message,bitchangedkey)

keyd='key12345'
bitchangedkey='kfy12345'
print("\n\navalanch in des key changed from ",keyd,"to ",bitchangedkey," : ")
message = "123456xxxxxxxxxx"
c1=des.encrypt(message,keyd)
c2=des.encrypt(message,bitchangedkey)
