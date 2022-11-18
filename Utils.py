def power(a, e, n):
    """
    Return a^e mod n (including longint)

    Parameters
    ----------
    a : int

    e : int

    n : int
    """
    p = 1
    while e > 0:
        if e % 2 != 0:
            p = (p * a) % n
        a = (a * a) % n
        e = e // 2
    return p

def test_prime(n):
    """
    Return true if n is a prime number

    Parameters
    ----------
    n : int
        The number that will be tested
    """
    if(n==2 or n==3 or n==5 or n==7 or n ==11 or n== 13):
        return True
    if((power(2, n-1, n)==1) and
        (power(3, n-1, n)==1)and
        (power(5, n-1, n)==1) and
        (power(7, n-1, n)==1) and 
        (power(11, n-1, n)==1) and
        (power(13, n-1, n)==1)) :
        return True
    return False

def pgcd(u, v):
    """
    Return the greatest common divisor between u and v

    Parameters
    ----------
    u : int

    v : int
    """
    while v:
        t = u
        u = v
        v = t % v
    if u < 0:
        return -u
    else:
        return u

def long_bezout(a, b):
    """
    Return the result of bezout's theorem : ax + by = pgcd(a,b)

    Parameters
    ----------
    a : int

    b : int
    """
    # On sauvegarde les valeurs de a et b.
    a0 = a
    b0 = b
    # On laisse invariant p*a0 + q*b0 = a et  r*a0 + s*b0 = b.
    p = 1
    q = 0
    r = 0
    s = 1
    # La boucle principale.
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
    return p  # on n'a besoin que de p