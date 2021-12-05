import Pyfhel
from Pyfhel import PyCtxt, PyPtxt
import tempfile
from pathlib import Path
import faulthandler; faulthandler.enable()
import textwrap

#Configuração
caminhoContext = "./imeCoin/bob/chaves/context_"
caminhoCK = "./imeCoin/bob/chaves/pub"
caminhoSK = "./imeCoin/bob/chaves/sec"
caminhoCP2 = "./imeCoin/bob/resp_alice"
block = PyCtxt()
rawBlock = []
rawBlockFinal = ""



#Bob configurando o ambiente
he_bob = Pyfhel.Pyfhel()
he_bob.restoreContext(caminhoContext + "3")
he_bob.restorepublicKey(caminhoCK + "3.key")
he_bob.restoresecretKey("./imeCoin/bob/chaves/sec3.key")
ctxt_restored = PyCtxt()
teste = [1] * 26


#Decifra o bloco que foi quebrado em partes menores - 14
for index in range(len(teste)):
    print("")
        
    block.load(caminhoCP2 + "/CP2_01bloco" + str(index), int)
    rawBlock.append(he_bob.decryptInt(block))
    
    print(str(index) + ": " + str(rawBlock[index]))  


#Boba remonta o blobo - 15

for index in range(len(rawBlock)):
    print("")    
    print(str(index) + ": " + str(rawBlock[index])) 
    
    if (index == 25) and (len(str(rawBlock[25])) < 7):
        #Coloca a parte do bloco no formato original
        print('{:07x}'.format(rawBlock[index]))
        rawBlock[index] = '{:07x}'.format(rawBlock[index])
    else:
        print('{:015x}'.format(rawBlock[index]))
        rawBlock[index] = '{:015x}'.format(rawBlock[index])
    
    rawBlockFinal = rawBlockFinal + str(rawBlock[index])
    
print(str(rawBlockFinal))






