import numpy as np
from numpy.polynomial import polynomial as poly

import poly_op.polyOp as op
    
if __name__ == "__main__":
    # Scheme's parameters
    # polynomial modulus degree
    n = 2**2
    # ciphertext modulus
    p = 101
    # plaintext modulus
    t = 2**8
    # polynomial modulus
    poly_mod = [1,0,0,1]
    # k
    k = [20]
    # mensagem
    m = [3]    
    
    
    print("====================================================")
    print("poly mod:")
    print(np.poly1d(poly_mod))    
    print("====================================================")    
    
    #Secret Key
    SK = [1,0,0,1]
    print("poly S:")
    print(np.poly1d(SK))
    
    print("====================================================")
    
    #Error poly
    e = [1,0,1,1]
    print("poly e:") 
    print(np.poly1d(e))
    print("====================================================")
    
    #PK
    a = [83,23,51,77]
    print("poly a: ")
    print(np.poly1d(a))
    print("====================================================")
    
    
    # Multiplacação a * s
    result = poly.polymul(a, SK)
    print("poly a*s:")
    print(np.poly1d(result))
    print("====================================================")
    
    
    # Multiplacação a * s com mod 101
    print("poly a*s mod 101:")
    print(np.poly1d(result%p))    
    print("====================================================")    
    
    
    # Multiplacação a * s com mod 101 sobre x^4+1
    result = np.poly1d(result%p) / np.poly1d(poly_mod)
    print("poly a*s mod 101 / x^4+1:")
    result = [95,-5%p,27,-27%p]
    print(np.poly1d(result))
    print("====================================================")
    
    
    # Multiplacação a * s com mod 101 sobre x^4+1        
    print("poly a*s + e mod 101 / x^4+1:")
    print(np.poly1d(result) + np.poly1d(e))
    b = poly.polyadd(result, e) % p
    print("====================================================")
    
    print("PK (a,b)")
    print("a: {}".format(a))
    print("b: {}".format(b))
    print("====================================================")
    
    #Chave Efemera
    ek = [100,0,0,50]
    
    
    #Erros utilizados Bob
    e1 = [1,0,1,20]
    e2 = [4,1,1,0]
    
    
    #Criação do v = a*EK + e1
    v = np.polyadd(np.polydiv((np.polymul(a,ek) % p), poly_mod)[1],e1) % p
    
    
    #Criação do w = b*EK + e2 + km   
    w = np.polyadd(np.polydiv((np.polymul(b,ek) % p), poly_mod)[1],e2) % p
    
    # +km
    w = np.polyadd(np.polymul(m,k),w) % p
    
    #Cypher Text
    print("Cypher Text: ")
    print("v: {}".format(v))
    print("w: {}".format(w))
    print("====================================================")
    
    
    #Decypher
    # w - vs arredondando para multiplo mais próximo de k
    result = np.polysub(w,np.polydiv(np.polymul(v,SK)% p,poly_mod)[1] % p) % p
    print("Decifrando: w - v*s")
    print(np.poly1d(result))
    print("====================================================")