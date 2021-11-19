import Pyfhel
import tempfile
import numpy
from pathlib import Path


# Configuracao
# ----------------------------------------------------------------------------------

tamanhoConsultaPrivada = 5
vetorP = [0,0,0,0,0] 
VK = []


# ----------------------------------------------------------------------------------

# Criando o vetor VK - Passo 4
for index in enumerate(vetorP):
    #1. p (long): Plaintext modulus. All operations are modulo p.
    #2. m (long=2048): Polynomial coefficient modulus.
    #   Higher allows more encrypted operations. In batch mode it is the number of integers per ciphertext.
    #   keyGen() gera as chaves
    he = Pyfhel.Pyfhel()
    he.contextGen(p=1964769281, m=8192, base=2, sec=192, flagBatching=True)
    he.keyGen()
    he.saveContext("./chaves/context_" + str(index))
    he.savepublicKey("./chaves/pub" + str(index) + ".key")
    he.savesecretKey("./chaves/sec" + str(index) + ".key")


# Criando o vetor P - Passo 5 e 6
vetorP = [0,0,0,1,0]


# ----------------------------------------------------------------------------------


# Using a temporary dir as a "secure channel"
# This can be changed into real communication using other python libraries.
secure_channel = tempfile.TemporaryDirectory()
sec_con = Path(secure_channel.name)
pk_file = sec_con / "mypk.pk"
contx_file = sec_con / "mycontx.con"
print(sec_con)


# ----------------------------------------------------------------------------------

# Geração do vetor privado


# ----------------------------------------------------------------------------------
half_the_truth = he.encryptInt(21)
two = he.encryptInt(2)
the_truth = he.multiply(half_the_truth, two)
print(he.decryptInt(the_truth))
print("----------------------------------------------------------------------------------")
#=> prints 42

# ----------------------------------------------------------------------------------

print("----------------------------------------------------------------------------------")
a = 1.5
b = 2.5
ca = he.encryptFrac(a)
cb = he.encryptFrac(b)
ca.to_file(sec_con / "ca.ctxt")
cb.to_file(sec_con / "cb.ctxt")


print("----------------------------------------------------------------------------------")


