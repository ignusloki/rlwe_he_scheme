import Pyfhel
import tempfile
from pathlib import Path
import faulthandler; faulthandler.enable()


# Configuracao
# ----------------------------------------------------------------------------------

tamanhoConsultaPrivada = 5
vetorP = [0,0,0,0,0] 
VK = []
CP = []

caminhoContext = "./imeCoin/bob/chaves/context_"
caminhoReqContext = "./imeCoin/bob/req_alice/context_"
caminhoReqContextBob = "./imeCoin/alice/req_bob/context_"


caminhoCK = "./imeCoin/bob/chaves/pub"
caminhoReqCK = "./imeCoin/bob/req_alice/pub"
caminhoReqCKBob = "./imeCoin/alice/req_bob/pub"


caminhoSK = "./imeCoin/bob/chaves/sec"

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
    
    he.saveContext(caminhoContext + str(index))
    he.saveContext(caminhoReqContext + str(index))
    he.saveContext(caminhoReqContextBob + str(index))
    
    
    he.savepublicKey(caminhoCK + str(index) + ".key")
    he.savepublicKey(caminhoReqCK + str(index) + ".key")
    he.savepublicKey(caminhoReqCKBob + str(index) + ".key")
    
    
    he.savesecretKey(caminhoSK + str(index) + ".key")


# Criando o vetor P - Passo 5 e 6
vetorP = [0,0,0,1,0]


# ----------------------------------------------------------------------------------

print("Locais do contexto e chaves:")
# Criando o vetor CP - Passo 7 e 8
for index in range(len(vetorP)):
    he_temp = Pyfhel.Pyfhel()
    
    #Restaurando chaves e contexto
    localContexto = caminhoContext + str(index)
    localChavePK = caminhoCK + str(index) + ".key"
    localChaveSK = caminhoSK + str(index) + ".key"
    he_temp.restoreContext(localContexto)    
    he_temp.restorepublicKey(localChavePK)
    he_temp.restoresecretKey(localChaveSK)    
    
    print(str(index) + " : " + localContexto)
    print(str(index) + " : " + localChavePK)
    print(str(index) + " : " + localChaveSK)    
    
    CP.append(he_temp.encryptInt(vetorP[index]))
    print(str(CP[index]))
    
    CP[index].save("./imeCoin/bob/req_alice/CP_" + str(index))
    CP[index].save("./imeCoin/alice/req_bob/CP_" + str(index))

# ----------------------------------------------------------------------------------

