import User
import random
import Utils

"""
A class used to represent the CA (authentication committee)

...

Attributes
----------
public_key : [long, long]
    The public key of the CA

private_key : long
    The priavte key of the CA
"""
class CA(User.User) :
    public_key = None
    private_key = None

    def __init__(self) :
        User.User.__init__(self)

    def create_keys(self): 
        """
        Generate a random public_key and private_key
        for the CA
        """
        # on choisis deux grands nombre premier
        isFirst = False
        while (not isFirst) :
            p = random.randint(10**25, 11**25)
            isFirst = Utils.test_prime(p)

        isFirst = False
        while(not isFirst) :
            q = random.randint(p, 5 * 11**25)
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
    
    def generate_certificate(self, user, mC, footprintC) :
        """
        Return the certificate if the footprint is the same as the decrypted version

        Parameters
        ----------
        user : User
            The user who need a certificate

        mC : int
            The crypted messsage

        footprintC : long
            The crypted footprint of the crypted message
        """
        footprintD = (user.encryption_decryption(footprintC[0], user.public_key[0]),
                        user.encryption_decryption(footprintC[1], user.public_key[0]))
        mD = (self.encryption_decryption(mC[0], self.private_key),
                self.encryption_decryption(mC[1], self.private_key))
        footprint = (self.footprint(mD[0]), 
                        self.footprint(mD[1]))
        if (footprint[0] == footprintD[0] and footprint[1] == footprintD[1]) :
            return (self.encryption_decryption(user.public_key[0], self.private_key), 
                    self.encryption_decryption(user.public_key[1], self.private_key))
        return None
