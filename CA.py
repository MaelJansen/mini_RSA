import User

class CA(User.User) :
    publicKey = None
    privateKey = None

    def __init__(self) :
        User.User.__init__(self)
    
    def generateCertificate(self, mC, publicKey, footprintC) :
        footprintD = self.decryption_publicKey(publicKey, publicKey[1], footprintC)
        mD = self.decryption_publicKey(self.publicKey, self.privateKey, mC)
        footprint = self.footprint(mD)
        if (footprint == footprintD) :
            return self.encryption_publicKey(publicKey, self.publicKey)
        return None