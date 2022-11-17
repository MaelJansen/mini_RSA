import random
import Utils
import hashlib

"""
A class used to represent an user

...

Attributes
----------
public_key : [long, long]
private_key : long
certificate : long
"""
class User :
    publicKey = None
    privateKey = None
    certificate = None

    def __init__(self) :
        self.create_keys()

    def create_keys(self): 
        """
        Generate a random public_key and private_key
        for the user
        """
        # on choisis deux grands nombre premier
        isFirst = False
        while (not isFirst) :
            p = random.randint(10**24, 11**24)
            isFirst = Utils.test_prime(p)

        isFirst = False
        while(not isFirst) :
            q = random.randint(p, 5 * 11**24)
            isFirst = Utils.test_prime(q)

        # calcul pour n et phi(n)
        n = p * q
        phin = (p - 1) * (q - 1)

        # choix de e
        e = random.randint(2, phin - 1)
        while (Utils.pgcd(e, phin) != 1):
            e = random.randint(2, phin - 1)
        
        # choix de d
        d = Utils.long_bezout(e, phin)

        self.publicKey = [e, n]
        self.privateKey = d % phin

    def encryption_decryption(self, message, e):
        """ 
        Return the encrypted message or the encrypted footprint

        Parameters
        ----------
        message : int
            The message that will be modified by the function
        
        public_key : [long, long]
            The public_key of the recipient

        private_key : long
            The private_key to encrypt the footprint
        """
        return Utils.power(message, e, self.publicKey[1])

    @staticmethod
    def verifyCertificate(user, ca) :
        if (user.certificate != None) :
            decryptPublickey = (ca.encryption_decryption(user.certificate[0], ca.publicKey[0]), 
                                ca.encryption_decryption(user.certificate[1], ca.publicKey[0]))
            print("Le certificat décrypté : " + str(decryptPublickey))
            if (user.publicKey[0] == decryptPublickey[0] and user.publicKey[1] == decryptPublickey[1]) :
                return True
            else :
                return False
        else :
            return False

    @staticmethod
    def footprint(m):
        """
        Return the footprint

        Parameters
        ----------
        m : int
            The message that wille be hashed 
        """
        h = hashlib.sha1(str(m).encode()).hexdigest()
        return int(h, base = 16) % (2**31 - 1)

