from Crypto.Cipher import DES3

def encrypt(message,key):
    obj = DES3.new(key, DES3.MODE_OFB,'ThiIV456')
    #message = "The answer is no"
    ciphertext = obj.encrypt(message)
    print(ciphertext)
    return ciphertext

def decrypt(ciphertext,key):
    obj2 = DES3.new(key, DES3.MODE_OFB,'ThiIV456')
    pt=obj2.decrypt(ciphertext)
    print(pt)
    return pt