import User
import CA
import Utils
import unittest as ut

"""
A class used to do all tests

...

Attributes
----------

"""
class Unit_Test(ut.TestCase) :
    
    def test(self):
        # Les différents test qui vont êtres éffectués pour vérifier que le code marche correctement

        # Les tests pour la fonction test_premier 
        self.assertTrue(Utils.test_prime(11))
        self.assertTrue(Utils.test_prime(2))

        # On créer des utilisateurs pour les tests et on créer les clées
        alice_test = User.User()
        bob_test = User.User()
        ca_test = CA.CA()

        # On commence par tester la validité des clés
        self.assertTrue(alice_test.public_key[0] > 0)
        self.assertTrue(bob_test.public_key[0] > 0)
        self.assertTrue(ca_test.public_key[0] > 0)

        # On test le cryptage et decryptage
        alice_test_crypte = alice_test.encryption_decryption(alice_test.public_key[0], alice_test.public_key[0])
        bob_test_crypte = bob_test.encryption_decryption(bob_test.public_key[0], bob_test.public_key[0])
        ca_test_crypte = ca_test.encryption_decryption(ca_test.public_key[0], ca_test.public_key[0])

        self.assertTrue(alice_test.public_key[0] == alice_test.encryption_decryption(alice_test_crypte, alice_test.private_key))
        self.assertTrue(bob_test.public_key[0] == bob_test.encryption_decryption(bob_test_crypte, bob_test.private_key))
        self.assertTrue(ca_test.public_key[0] == ca_test.encryption_decryption(ca_test_crypte, ca_test.private_key))

        # On test l'empreinte
        message = 1200
        empreinte_message = alice_test.footprint(message)
        message_crypte = alice_test.encryption_decryption(message, alice_test.public_key[0])
        empreinte_message_crypte = alice_test.encryption_decryption(empreinte_message, alice_test.public_key[0])
        message_decrypte = alice_test.encryption_decryption(message_crypte, alice_test.private_key)

        self.assertTrue(alice_test.footprint(message_decrypte) == alice_test.encryption_decryption(empreinte_message_crypte, alice_test.private_key))
        # On simule un changement dans la transmission du message crypté
        message_decrypte_eronne = message_decrypte + 1
        self.assertTrue(alice_test.footprint(message_decrypte_eronne) != alice_test.encryption_decryption(empreinte_message_crypte, alice_test.public_key[0]))

        # On test les certificats
        cryptMessage = (ca_test.encryption_decryption(alice_test.public_key[0], ca_test.public_key[0]), 
                    ca_test.encryption_decryption(alice_test.public_key[1], ca_test.public_key[0]))
        footprint = (User.User.footprint(alice_test.public_key[0]), 
                        User.User.footprint(alice_test.public_key[1]))
        cryptFootprint = (alice_test.encryption_decryption(footprint[0], alice_test.private_key), 
                    alice_test.encryption_decryption(footprint[1], alice_test.private_key))

        aliceCertificate = ca_test.generate_certificate(alice_test, cryptMessage, cryptFootprint)
        self.assertNotEqual(aliceCertificate, None)
        cryptPublickey = ca_test.encryption_decryption(alice_test.public_key[0], ca_test.private_key), ca_test.encryption_decryption(alice_test.public_key[1], ca_test.private_key)
        self.assertEqual(aliceCertificate, cryptPublickey)

        cryptMessage = (ca_test.encryption_decryption(bob_test.public_key[0], ca_test.public_key[0]), 
                    ca_test.encryption_decryption(bob_test.public_key[1], ca_test.public_key[0]))
        footprint = (User.User.footprint(bob_test.public_key[0]), 
                        User.User.footprint(bob_test.public_key[1]))
        cryptFootprint = (bob_test.encryption_decryption(footprint[0], bob_test.private_key), 
                    bob_test.encryption_decryption(footprint[1], bob_test.private_key))

        cryptPublickey = ca_test.encryption_decryption(bob_test.public_key[0], ca_test.private_key), ca_test.encryption_decryption(bob_test.public_key[1], ca_test.private_key)
        bobCertificate = ca_test.generate_certificate(bob_test, cryptMessage, cryptFootprint)
        self.assertEqual(bobCertificate, cryptPublickey)

        self.assertNotEqual(aliceCertificate, bobCertificate)

