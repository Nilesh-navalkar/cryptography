from Crypto.Cipher import AES

def encrypt(message,key):
    obj = AES.new(key, AES.MODE_CBC, 'This is an IV456')
    #message = "The answer is no"
    ciphertext = obj.encrypt(message)
    print(ciphertext)
    return ciphertext

def decrypt(ciphertext,key):
    obj2 = AES.new(key, AES.MODE_CBC, 'This is an IV456')
    pt=obj2.decrypt(ciphertext)
    print(pt)
    return pt