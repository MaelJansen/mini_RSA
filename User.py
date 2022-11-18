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
    public_key = None
    private_key = None
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

        self.public_key = [e, n]
        self.private_key = d % phin

    def encryption_decryption(self, message, e):
        """ 
        Return the encrypted message or the encrypted footprint

        Parameters
        ----------
        message : int
            The message that will be modified by the function
        
        public_key[e] : long
            The key of the recipient
        """
        return Utils.power(message, e, self.public_key[1])

    @staticmethod
    def verify_certificate(user, ca) :
        """ 
        Return true if the certificate is valid

        Parameters
        ----------
        user : User
            The user who has his certificate tested

        ca : CA
            The CA 
        """
        if (user.certificate != None) :
            decrypt_public_key = (ca.encryption_decryption(user.certificate[0], ca.public_key[0]), 
                                ca.encryption_decryption(user.certificate[1], ca.public_key[0]))
            print("Le certificat décrypté : " + str(decrypt_public_key))
            if (user.public_key[0] == decrypt_public_key[0] and user.public_key[1] == decrypt_public_key[1]) :
                return True
        return False

    @staticmethod
    def footprint(m):
        """
        Return the footprint

        Parameters
        ----------
        m : int
            The message that will be hashed 
        """
        h = hashlib.sha1(str(m).encode()).hexdigest()
        return int(h, base = 16) % (2**31 - 1)

