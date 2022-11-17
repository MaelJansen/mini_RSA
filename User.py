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

    def encryption(self, message, e):
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

    def decryption(self, message, e):
        """ 
        Return the decrypted message

        Parameters
        ----------
        public_key : [long, long]
            The public_key (just n) to decrypt the message

        private_key : long
            The private_key to decrypt the message
        
        message :
            The message that will be decrypted
        """
        return Utils.power(message, e, self.publicKey[1])


    @staticmethod
    def footprint(m):
        """
        Return the footprint

        Parameters
        ----------
        m : int
            The message that wille be hashed 
        """
        h = hashlib.sha256(str(m).encode()).hexdigest()
        return int(h, base = 16) % (2**31 - 1)

