import Mini_RSA as mr
import User 

# Les différents test qui vont êtres éffectués pour vérifier que le code marche correctement

# Les tests pour la fonction test_premier 
assert(mr.test_prime(11))
assert(mr.test_prime(2))
assert(not mr.test_prime(1))

# On créer des utilisateurs pour les tests et on créer les clées
alice_test = User.User()
bob_test = User.User()
ca_test = User.User()

# On commence par tester la validité des clés
assert(mr.test_prime(alice_test))
assert(mr.test_prime(bob_test))
assert(mr.test_prime(ca_test))
assert(ca_test > 0)
assert(ca_test > 0)
assert(ca_test > 0)

# On test le cryptage et decryptage
alice_test_crypte = alice_test.encrytpion_decryption(alice_test, alice_test[0])
bob_test_crypte = bob_test.encrytpion_decryption(bob_test, bob_test[0])
ca_test_crypte = ca_test.encrytpion_decryption(ca_test[0])

assert(alice_test == alice_test.encrytpion_decryption(alice_test_crypte, alice_test[0]))
assert(bob_test == bob_test.encrytpion_decryption(bob_test_crypte, bob_test[0]))
assert(ca_test == ca_test.encrytpion_decryption(ca_test_crypte, ca_test[0]))

# On test l'empreinte
message = 1200
empreinte_message = alice_test.footprint(message)
message_crypte = alice_test.encryption_decryption(message, alice_test[0])
empreinte_message_crypte = mr.encryption_decryption(empreinte_message, alice_test[0])
message_decrypte = mr.encryption_decryption(message_crypte, alice_test[0])

assert(mr.footprint(message_decrypte) == mr.encryption_decryption(empreinte_message_crypte, alice_test[0]))
# On simule un changement dans la transmission du message crypté
message_decrypte_eronne = message_decrypte + 1
assert(mr.footprint(message_decrypte_eronne) != mr.encryption_decryption(empreinte_message_crypte, alice_test[0]))

# On test les certificats
certificat = mr.gerenrate_certificat(mr,alice_test,)
