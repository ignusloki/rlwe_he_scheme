import Pyfhel
from Pyfhel import PyPtxt, PyCtxt

# Exemplo 1
# ----------------------------------------------------------------------------------

he = Pyfhel.Pyfhel()
he.contextGen(p=10000)
he.keyGen()

#1. p (long): Plaintext modulus. All operations are modulo p.
#2. m (long=2048): Polynomial coefficient modulus.
#   Higher allows more encrypted operations. In batch mode it is the number of integers per ciphertext.
#   keyGen() gera as chaves

# ----------------------------------------------------------------------------------
# now everything is initialized
half_the_truth = he.encryptInt(21)
two = he.encryptInt(2)
the_truth = he.multiply(half_the_truth, two)
print(he.decryptInt(the_truth))
print("----------------------------------------------------------------------------------")
#=> prints 42

# ----------------------------------------------------------------------------------

ctxt1 = he.encryptInt(2)
print(he.decryptInt(ctxt1))
#=> prints 2
print(he.noiseLevel(ctxt1))
#=> prints 30
ctxt2 = he.add(ctxt1, two)
print(he.decryptInt(ctxt1))
#=> prints 4
print(he.noiseLevel(ctxt1))
#=> prints 29
ctxt3 = he.multiply(ctxt2, two)
print(he.decryptInt(ctxt2))
#=> prints 8
print(he.noiseLevel(ctxt2))
#=> prints 6
ctxt4 = he.multiply(ctxt3, two)
print(he.decryptInt(ctxt3))
#=> prints -7906467554648178793
print(he.noiseLevel(ctxt3))
#=> prints 0

print("----------------------------------------------------------------------------------")

print("2. Encrypting integers with encryptInt")
integer1 = 94
integer2 = -235
ctxt_i1 = he.encryptInt(integer1)   # Encrypting integer1 in a new PyCtxt with encryptInt
ctxt_i2 = PyCtxt()                  # Empty ciphertexts have no encoding type.
print("    Empty created ctxt_i2: ",   str(ctxt_i2))
he.encryptInt(integer2, ctxt_i2)    # Encrypting integer2 in an existing PyCtxt
print("    int ",integer1,'-> ctxt_i1 ', str(ctxt_i1))
print("    int ",integer2,'-> ctxt_i2 ', str(ctxt_i2))


