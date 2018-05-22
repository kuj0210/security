import pyDes
import base64

class DES:
    def __init__(self, iv, key):
        self.iv = iv
        self.key = key
    def encrypt(self, data):
        k = pyDes.des(self.key, pyDes.ECB, self.iv, pad=None, padmode=pyDes.PAD_PKCS5)
        d = k.encrypt(data)
        d = base64.encodebytes(d)
        return d
    def decrypt(self, data):
        k = pyDes.des(self.key, pyDes.ECB, self.iv, pad=None, padmode=pyDes.PAD_PKCS5)
        data = base64.decodebytes(data)
        d = k.decrypt(data)
        return d

if __name__ == '__main__':
    data = "Ya - Ha !"

    iv = '12345678'
    key = '12345678'
    des = DES(iv, key)
    encryptdata = des.encrypt(data.encode('utf-8'))
    print (encryptdata)
    decryptdata = des.decrypt(encryptdata)
    print (decryptdata)