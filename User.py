import random
import Utils

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
    public_key = None
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
        while d < 1 :
            d = pow(e, -1, phin)
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
        if (private_key == null):
            if 1 < rep and rep < publicKey[1]:
                return Utils.power(message, publicKey[0], publicKey[1])
            else:
                return Utils.flatten_list([User.encryption(rep/2, publicKey), User.encryption(rep/2, publicKey)])
        return Utils.power(message, privateKey, publicKey[1])

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
        return m * 17 % 13

    '''
    def sign_message(self, message, privateKey, publicKey):
        return Utils.power(message, privateKey, publicKey[1])
    '''