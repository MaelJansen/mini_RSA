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
    '''
    le calcul de d
    d = 0
    while d <= 0:
        d = (int)(1/e)
    '''
    return [e,n],[p,q]

PublicKey,PrivateKey = create_keys()
print(PublicKey)
print(PrivateKey)


def encryptionPublicKey(message,publicKey):
    return 0
