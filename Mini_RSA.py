import os
import User
import CA
import Mini_RSA_Test as test

t = test.Unit_Test()
t.test()

alice = User.User()
bob = User.User()
ca = CA.CA()

print("La clé à certifier : " + str(alice.public_key))
print("la clé privée de Alice : " + str(alice.private_key))

cryptMessage = (ca.encryption_decryption(alice.public_key[0], ca.public_key[0]), 
                    ca.encryption_decryption(alice.public_key[1], ca.public_key[0]))
aliceFootprint = (User.User.footprint(alice.public_key[0]), 
                        User.User.footprint(alice.public_key[1]))
cryptAliceFootprint = (alice.encryption_decryption(aliceFootprint[0], alice.private_key), 
                    alice.encryption_decryption(aliceFootprint[1], alice.private_key))

alice.certificate = ca.generate_certificate(alice, cryptMessage, cryptAliceFootprint)
print("La clé certifiée : " + str(alice.certificate))

print(bob.verify_certificate(alice, ca))