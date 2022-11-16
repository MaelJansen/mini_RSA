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

    def __init__(self, nb1, nb2) :
        self.create_keys(nb1, nb2)

    def create_keys(self, nb1, nb2): 
        """
        Generate a random public_key and private_key
        for the user
        """
        # on choisis deux grands nombre premier
        isFirst = False
        while (not isFirst):
            p = random.randint(nb1, nb2)
            isFirst = Utils.test_prime(p) #and pgcd(p,q) == 1
        isFirst = False
        while(not isFirst):
            q = random.randint(p, 5*10**6)
            isFirst = Utils.test_prime(q)
        # calcul pour n et phi(n)
        n = p * q
        phin = (p - 1) * (q - 1)
        # choix de e
        e  = random.randint(2, phin - 1)
        while (Utils.pgcd(e, phin) != 1):
            e = random.randint(2, phin - 1)
        while d < 1 :
            d = Utils.power(e, -1, phin)
        self.publicKey = [e, n]
        self.privateKey = d

    @staticmethod
    def encryption(message, public_key, private_key):
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
        rep = Utils.power(message, public_key[0], public_key[1])
        if (private_key == None):
            if 1 < rep and rep < public_key[1]:
                return Utils.power(message, public_key[0], public_key[1])
            else:
                return Utils.flatten_list([User.encryption(rep/2, public_key), User.encryption(rep/2, public_key)])
        return Utils.power(message, private_key, public_key[1])

    @staticmethod
    def decryption_message(publicKey, privateKey, message):
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
        """
        Return the footprint

        Parameters
        ----------
        m : int
            The message that wille be hashed 
        """
        h = hashlib.sha1(str(m).encode('utf-8')).hexdigest()
        return int(h, base = 16) % (2**(82589933) - 1)
        
