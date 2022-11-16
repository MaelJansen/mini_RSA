import os
import User
import CA

alice = User.User(10**5, 10**6)
ca = CA.CA(10**6, 10**7)

message = alice.publicKey
aliceFootprint = (alice.footprint(message[0]), alice.footprint(message[1]))
print("L'empreinte de la clé publique d'alice : " + str(aliceFootprint))
cryptMessage = (User.User.encryption_publicKey(message[0], ca.publicKey), 
                User.User.encryption_publicKey(message[1], ca.publicKey))
aliceCryptFootprint = (User.User.encryption_footprint(aliceFootprint[0], alice.publicKey,  alice.privateKey), 
                        User.User.encryption_footprint(aliceFootprint[1], alice.publicKey,  alice.privateKey))
alice.certificate = ca.generateCertificate(cryptMessage, alice.publicKey, aliceCryptFootprint)
print(alice.certificate)
