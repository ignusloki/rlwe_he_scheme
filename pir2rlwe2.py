import Pyfhel
import tempfile
import numpy
from pathlib import Path
import faulthandler; faulthandler.enable()


# Configuracao
# ----------------------------------------------------------------------------------

tamanhoConsultaPrivada = 5
vetorP = [0,0,0,0,0] 
VK = []
CP = []


# ----------------------------------------------------------------------------------

# Criando o vetor VK - Passo 4
for index in range(len(vetorP)):
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

print("Locais do contexto e chaves:")
# Criando o vetor CP - Passo 7 e 8
for index in range(len(vetorP)):
    he_temp = Pyfhel.Pyfhel()
    
    #Restaurando chaves e contexto
    localContexto = "./chaves/context_" + str(index)
    localChavePK = "./chaves/pub" + str(index) + ".key"
    localChaveSK = "./chaves/sec" + str(index) + ".key"
    he_temp.restoreContext(localContexto)    
    he_temp.restorepublicKey(localChavePK)
    he_temp.restoresecretKey(localChaveSK)    
    
    print(str(index) + " : " + localContexto)
    print(str(index) + " : " + localChavePK)
    print(str(index) + " : " + localChaveSK)    
    
    CP.append(he_temp.encryptInt(vetorP[index]))
    print(str(CP[index]))
    
    CP[index].save("./chaves/enc/ctx" + str(index))

# ----------------------------------------------------------------------------------







# ----------------------------------------------------------------------------------

# Using a temporary dir as a "secure channel"
# This can be changed into real communication using other python libraries.
secure_channel = tempfile.TemporaryDirectory()
sec_con = Path(secure_channel.name)
pk_file = sec_con / "mypk.pk"
contx_file = sec_con / "mycontx.con"
print(sec_con)


# ----------------------------------------------------------------------------------
half_the_truth = he.encryptInt(21)
two = he.encryptInt(2)
the_truth = he.multiply(half_the_truth, two)
print(he.decryptInt(the_truth))
print("----------------------------------------------------------------------------------")
#=> prints 42

# ----------------------------------------------------------------------------------



