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

    def __init__(self, nb1, nb2) :
        User.User.__init__(self, nb1, nb2)
    
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
        print("Le message crypté : " + str(mC))
        footprintD = (self.decryption_publicKey(publicKey, publicKey[0], footprintC[0]),
                        self.decryption_publicKey(publicKey, publicKey[0], footprintC[1]))
        print("L'empreinte décryptée : " + str(footprintD))
        mD = (self.decryption_publicKey(self.publicKey, self.privateKey, mC[0]),
                self.decryption_publicKey(self.publicKey, self.privateKey, mC[1]))
        print("Le message décrypté : " + str(mD))
        footprint = (self.footprint(mD[0]), 
                        self.footprint(mD[1]))
        print("L'empreinte du message décrypté : " + str(footprint))
        if (footprint[0] == footprintD[0] and footprint[1] == footprintD[1]) :
            return self.encryption_footprint(publicKey[0], self.publicKey, self.privateKey)
        else :
            return None
