import tdes 

keya='This is a key123'
message = "123456xxxxxxxxxx"
bitchangedmssg="223456xxxxxxxxxx"
bitchangedkey='This is a kfy123'
print("\n\navalanch in 3-des message changed from ",message,"to ",bitchangedmssg," : ")
c1=tdes.encrypt(message,keya)
c2=tdes.encrypt(bitchangedmssg,keya)


print("\n\navalanch in 3-des key changed from ",keya,"to ",bitchangedkey," : ")
c1=tdes.encrypt(message,keya)
c2=tdes.encrypt(message,bitchangedkey)