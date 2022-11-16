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
    
    def generateCertificate(self, mC, footprintC, publicKey) :
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
        print("Le message crypté : " + str(mC))
        footprintD = (self.decryption(publicKey, publicKey[0], footprintC[0]),
                        self.decryption(publicKey, publicKey[0], footprintC[1]))
        print("L'empreinte décryptée : " + str(footprintD))
        mD = (self.decryption(self.publicKey, self.privateKey, mC[0]),
                self.decryption(self.publicKey, self.privateKey, mC[1]))
        print("Le message décrypté : " + str(mD))
        footprint = (self.footprint(mD[0]), 
                        self.footprint(mD[1]))
        print("L'empreinte du message décrypté : " + str(footprint))
        if (footprint[0] == footprintD[0] and footprint[1] == footprintD[1]) :
            return self.encryption(publicKey[0], self.publicKey, self.privateKey)
        else :
            return None
