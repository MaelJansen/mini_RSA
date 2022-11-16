import os
import User
import CA

cpt = 0
nb = 100

for i in range(nb) :
    alice = User.User()
    bob = User.User()
    ca = CA.CA()
    while(ca.publicKey[0] < alice.publicKey[0] and ca.publicKey[1] < alice.publicKey[1]) :
        ca = CA.CA()

    print("La clé à certifier : " + str(alice.publicKey))

    cryptMessage = (ca.encryption(alice.publicKey[0], ca.publicKey[0]), 
                    ca.encryption(alice.publicKey[1], ca.publicKey[0]))
    aliceFootprint = (User.User.footprint(alice.publicKey[0]), 
                        User.User.footprint(alice.publicKey[1]))
    cryptAliceFootprint = (alice.encryption(aliceFootprint[0], alice.privateKey), 
                    alice.encryption(aliceFootprint[1], alice.privateKey))

    alice.certificate = ca.generateCertificate(alice, cryptMessage, cryptAliceFootprint)
    print("La clé certifiée : " + str(alice.certificate))

    if (alice.certificate != None) :
        cpt += 1

print(" ")

print("Taux de réussite du décryptage : " + str((cpt / nb) * 100) + "%")