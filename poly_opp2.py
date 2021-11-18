import numpy as np
from numpy.polynomial import polynomial as poly

def polymul(x, y, modulus, poly_mod):
    """Multiply two polynoms

    Args:
        x, y: two polynoms to be multiplied.
        modulus: coefficient modulus.
        poly_mod: polynomial modulus.

    Returns:
        A polynomial in Z_modulus[X]/(poly_mod).
    """
    return np.int64(
        np.round(poly.polydiv(poly.polymul(x, y) %
                              modulus, poly_mod)[1] % modulus)
    )


def polyadd(x, y, modulus, poly_mod):
    """Add two polynoms

    Args:
        x, y: two polynoms to be added.
        modulus: coefficient modulus.
        poly_mod: polynomial modulus.

    Returns:
        A polynomial in Z_modulus[X]/(poly_mod).
    """
    return np.int64(
        np.round(poly.polydiv(poly.polyadd(x, y) %
                              modulus, poly_mod)[1] % modulus)
    )
    
if __name__ == "__main__":
    # Scheme's parameters
    # polynomial modulus degree
    n = 2**2
    # ciphertext modulus
    p = 101
    # plaintext modulus
    t = 2**8
    # polynomial modulus
    poly_mod = (1,0,0,1)
    print("poly mod:")
    print(np.poly1d(poly_mod))    
    print("====================================================")    
        
    a = (5,0,3)
    print("poly a: ")
    print(np.poly1d(a))
    print("====================================================")
    
    b = (3,4,0,0)
    print("poly b: ")
    print(np.poly1d(b))
    print("====================================================")
    
    # Multiplacação a * b
    result = poly.polymul(a, b)
    result2 = np.poly1d(a) * np.poly1d(b)
    print("poly a*b:")
    print(result % p)
    print(result2)        
    print("====================================================")
    multy = (4,9,9,1,0,0)
    print(np.poly1d(multy))
    print("====================================================")
    
    # Redução a * b / x^4+1
    result = poly.polydiv(multy, poly_mod)
    result2 = np.poly1d(multy) / np.poly1d(poly_mod)
    print("Redução:")
    print(np.floor((result)[1]))
    print((result2)[1])
    print("====================================================")