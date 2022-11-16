import os
import User
import CA

alice = User.User()
bob = User.User()
ca = CA.CA()
while(ca.publicKey[0] < alice.publicKey[0] and ca.publicKey[1] < alice.publicKey[1]) :
    ca = CA.CA()
print(alice.publicKey)
#print(ca.publicKey)

messageAuCA = alice.publicKey
messageAuCA = (ca.encryption(messageAuCA[0], ca.publicKey[0]), 
                ca.encryption(messageAuCA[1], ca.publicKey[0]))
aliceKeyHasher = (User.User.footprint(alice.publicKey[0]), 
                    User.User.footprint(alice.publicKey[1]))
print("L'empreinte du message : " + str(aliceKeyHasher))
messageSigner = (alice.encryption(aliceKeyHasher[0], alice.privateKey), 
                alice.encryption(aliceKeyHasher[1], alice.privateKey))
messageEnvoyer = (messageAuCA, messageSigner)

print("Le message envoyer : " + str(messageEnvoyer))

messageRecu = (ca.decryption(messageEnvoyer[0][0], ca.privateKey), 
                ca.decryption(messageEnvoyer[0][1], ca.privateKey))
EmpreinteDechiffree = (alice.decryption(messageEnvoyer[1][0], alice.publicKey[0]), 
                        alice.decryption(messageEnvoyer[1][1], alice.publicKey[0]))

print("Le message recu est : " + str(messageRecu))
print("L'empreinte dechiffrée : " + str(EmpreinteDechiffree))
print("L'empreinte du message recu : " + str(User.User.footprint(messageRecu[0])) + " " + str(User.User.footprint(messageRecu[1])))
verificationHashage = User.User.footprint(messageRecu[0]) == EmpreinteDechiffree[0] and User.User.footprint(messageRecu[1]) == EmpreinteDechiffree[1]
print(verificationHashage)