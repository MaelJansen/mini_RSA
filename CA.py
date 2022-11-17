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
    
    def generateCertificate(self, user, mC, footprintC) :
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
        print("La clé cryptée : " + str(mC))
        footprintD = (user.encryption_decryption(footprintC[0], user.publicKey[0]),
                        user.encryption_decryption(footprintC[1], user.publicKey[0]))
        print("L'empreinte décryptée : " + str(footprintD))
        mD = (self.encryption_decryption(mC[0], self.privateKey),
                self.encryption_decryption(mC[1], self.privateKey))
        print("La clé décrypté : " + str(mD))
        footprint = (self.footprint(mD[0]), 
                        self.footprint(mD[1]))
        print("L'empreinte de la clé décryptée : " + str(footprint))
        if (footprint[0] == footprintD[0] and footprint[1] == footprintD[1]) :
            return (self.encryption_decryption(user.publicKey[0], self.privateKey), 
                    self.encryption_decryption(user.publicKey[1], self.privateKey)) 
        else :
            return None
