import os
import User
import CA

'''
def com_CA(empreinte, keypublic, keyprivate, Cpublic):
    a = []
    a.append(signer_message(empreinte,keyprivate,keypublic))
    a.append(encryption_publicKey(keypublic[0],Cpublic))
    return a


def CA(a, ca, ClePublicAlice):
    CAPublic = ca[0]
    CAPrivate = ca [1]
    if decryption_public_key(ClePublicAlice,CAPrivate,a[2]) != ClePublicAlice :
        return False
    else: 
        return False


m = 1200
alice = create_keys()
alicePK = alice[0]
aliceprivK = alice[1]
message  = (encryption_publicKey(m, alicePK),empreinte(m))
messageVerifie = decryption_public_key(alicePK, aliceprivK, message[0])
hachemessageVerifie = empreinte(messageVerifie)
if(hachemessageVerifie == message[1]): print("ça marche")
'''

alice = User.User()
bob = User.User()
ca = CA.CA()
print(alice.publicKey)
#print(bob.publicKey)
#print(ca.publicKey)
message = int(input("Quel est votre message ?"))
encryptMessage, aliceFootprint = User.User.encryption_publicKey(message, bob.publicKey), User.User.footprint(message)
print(encryptMessage)
decryptMessage = User.User.decryption_publicKey(bob.publicKey, bob.privateKey, encryptMessage)
print(decryptMessage)
footprint = User.User.footprint(decryptMessage)
if (footprint == aliceFootprint) :
    print("OK")
'''
aliceCryptFootprint = alice.encryption_footprint(aliceFootprint, alice.publicKey, alice.privateKey)
alice.certificate = ca.generateCertificate(encryptMessage, alice.publicKey, aliceCryptFootprint)
print(alice.certificate)
'''