import random

def power(a, e, n) :
    p = 1
    while e > 0 :
        if e % 2 != 0 :
            p = (p * a) % n
        a = (a * a) % n
        e = e // 2
    return p

def test_prime(n) :
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def pgcd(u, v) :
    while v :
        t = u
        u = v
        v = t % v
    if u < 0 :
        return -u
    else :
        return u

def long_bezout(a, b):
  #On sauvegarde les valeurs de a et b.
  a0 = a
  b0 = b

  #On laisse invariant p*a0 + q*b0 = a et  r*a0 + s*b0 = b.
  p = 1
  q = 0
  r = 0
  s = 1
  #La boucle principale.
  while (b != 0):
    c = a % b
    quotient = a//b
    a = b
    b = c
    nouveau_r = p - quotient * r
    nouveau_s = q - quotient * s
    p = r
    q = s
    r = nouveau_r
    s = nouveau_s

  return p #on n'a besoin que de p

def create_keys():
    
    # on choisis deux grands nombre premier
    estPremier = False
    while (not estPremier):
        p = random.randint(100, 1000)
        estPremier = test_prime(p) #and pgcd(p,q) == 1
    estPremier = False
    while(not estPremier):
        q = random.randint(p, 5000)
        estPremier = test_prime(q)

    # calcul pour n et phi(n)
    n = p*q
    phin = (p-1)*(q-1)
    # choix de e
    e  = random.randint(2,phin-1)
    while (pgcd(e, phin) != 1):
        e = random.randint(2, phin-1)
    # le calcul de d
    d = 0
    while d < 1 :
        d = pow(e,-1,phin)
    return [e,n], d


def flatten_list(data,l):
    # iterating over the data
    for element in data:
        # checking for list
        if type(element) == list:
            # calling the same function with current element as new argument
            a = flatten_list(element,l)
        else:
            a = element
        l.append(a)
    return l

def encryption_publicKey(message, publicKey):
    rep = power(message, publicKey[0], publicKey[1])
    if 1 < rep and rep < publicKey[1]:
        return power(message, publicKey[0], publicKey[1])
    else:
        return flatten_list([encryption_publicKey(rep/2, publicKey), encryption_publicKey(rep/2, publicKey)])

def decryption_public_key(publicKey, privateKey, message):
    n = publicKey[1]
    a = 0
    if type(message) == list :
        for i in list(message):
            a += i
    else :
        a = message    
    m = power(a, privateKey, n)
    return m

def signer_message(message, privateKey, publicKey):
    return power(message, privateKey, publicKey[1])

def empreinte(m):
    return m*17%13

m = 1200
alice = create_keys()
alicePK = alice[0]
aliceprivK = alice[1]
message  = (encryption_publicKey(m, alicePK),empreinte(m))
messageVerifie = decryption_public_key(alicePK, aliceprivK, message[0])
hachemessageVerifie = empreinte(messageVerifie)
if(hachemessageVerifie == message[1]): print("ça marche")


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