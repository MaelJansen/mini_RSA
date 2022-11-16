import User

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
    publicKey = None
    privateKey = None

    def __init__(self) :
        User.User.__init__(self)
    
    def generateCertificate(self, mC, publicKey, footprintC) :
        """
        Return the certificate if the footprint is the same as the decrypted version

        Parameters
        ----------
        mC : int
            The crypted messsage
        
        public_key : long
            The public key of the one who ask for a certificate

        footprintc : long
            The footprint of the crypted messages
        """
        footprintD = self.decryption_message(publicKey, publicKey[1], footprintC)
        mD = self.decryption_message(self.publicKey, self.privateKey, mC)
        footprint = self.footprint(mD)
        if (footprint == footprintD) :
            return self.encryption(publicKey, self.publicKey)
        return None