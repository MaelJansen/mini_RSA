import random
import Utils

class User :
    publicKey = None
    privateKey = None
    certificate = None

    def __init__(self) :
        self.create_keys()

    def create_keys(self): 
        # on choisis deux grands nombre premier
        isFirst = False
        while (not isFirst):
            p = random.randint(100, 1000)
            isFirst = Utils.test_prime(p) #and pgcd(p,q) == 1
        isFirst = False
        while(not isFirst):
            q = random.randint(p, 5000)
            isFirst = Utils.test_prime(q)

        # calcul pour n et phi(n)
        n = p * q
        phin = (p - 1) * (q - 1)
        # choix de e
        e  = random.randint(2, phin - 1)
        while (Utils.pgcd(e, phin) != 1):
            e = random.randint(2, phin - 1)
        # le calcul de d
        d = 0
        while d < 1 :
            d = pow(e, -1, phin)
        self.publicKey = [e, n]
        self.privateKey = d

    @staticmethod
    def encryption_publicKey(message, publicKey):
        rep = Utils.power(message, publicKey[0], publicKey[1])
        if 1 < rep and rep < publicKey[1]:
            return Utils.power(message, publicKey[0], publicKey[1])
        else:
            return Utils.flatten_list([User.encryption_publicKey(rep/2, publicKey), User.encryption_publicKey(rep/2, publicKey)])

    @staticmethod
    def encryption_footprint(message, publicKey, privateKey):
        return Utils.power(message, privateKey, publicKey[1])

    @staticmethod
    def decryption_publicKey(publicKey, privateKey, message):
        n = publicKey[1]
        a = 0
        if type(message) == list :
            for i in list(message):
                a += i
        else :
            a = message    
        m = Utils.power(a, privateKey, n)
        return m

    @staticmethod
    def footprint(m):
        return m * 17 % 13

    '''
    def sign_message(self, message, privateKey, publicKey):
        return Utils.power(message, privateKey, publicKey[1])
    '''