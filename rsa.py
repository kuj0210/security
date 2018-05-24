class RSA:
    def __init__(self,p,q):
        self.m = "non input"
        self.p = p
        self.q = q
        self.n = p*q
        self.tot = (p-1) * (q-1)

        self.e = 0
        self.d =0

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def get_n(self):
        return self.n

    def get_private_key(self, e):
        d = 1
        while (e * d) % self.tot != 1 or d == e:
            d += 1
        self.d = d
        return d

    def get_public_key(self):
        e = 2
        while e < self.tot and self.gcd(e, self.tot) != 1:
            e += 1
        self.e = e
        return e

    def decrypt(self, n, d, ciphertext):
        # Unpack the key into its components
        # Generate the plaintext based on the ciphertext and key using a^b mod m
        plain = [chr((char ** d) % self.n) for char in ciphertext]
        # Return the array of bytes as a string
        return ''.join(plain)

    def encrypt(self, n, e, plaintext):
        # Unpack the key into it's components
        # Convert each letter in the plaintext to numbers based on the character using a^b mod m
        cipher = [(ord(char) ** e) % n for char in plaintext]
        # Return the array of bytes
        return cipher

    def show_all(self):         # 전체 확인용 초기메세지 "non input"사용
        print("\n\ne = ", self.e, "   d = ", self.d)
        print("original msg : ", self.m)
        en_msg = self.encrypt(e, self.m)
        de_msg = self.decrypt(d, en_msg)
        print("encrypt msg : ", en_msg)
        print("decrypt msg : ", de_msg)
        return

    def get_key(self):
        print("\n\nget key\n(p, q, n, e, d) : (", self.p, self.q, self.n, self.e, self.d, ")")
        return self.p, self.q, self.n, self.e, self.d

#아래는 테스트

a = RSA(17, 37)
n = a.get_n()
e = a.get_public_key()
d = a.get_private_key(e)
print("e : ", e, "  d : ", d)
TestMSG = "This is security project"
print("Ori_MSG : ", TestMSG)
testEMSG = a.encrypt(n, e, TestMSG)
print("En_MSG : ", testEMSG)
print("De_MSG : ", a.decrypt(n, d, testEMSG))

show_p, show_q, show_n, show_e, show_d = a.get_key()