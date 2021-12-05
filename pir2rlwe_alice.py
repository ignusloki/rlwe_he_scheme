import Pyfhel
from Pyfhel import PyCtxt, PyPtxt
import tempfile
from pathlib import Path
import faulthandler; faulthandler.enable()
import textwrap


#Configuração
localContextBob = "./imeCoin/alice/req_bob/context_3"
localChavePKBob = "./imeCoin/alice/req_bob/pub3.key"
localCPBob = "./imeCoin/alice/req_bob/CP_3"
localBlocosCP = "./imeCoin/alice/blocos"
localCP2 = "./imeCoin/alice/resp_bob"
caminhoBobResp = "./imeCoin/bob/resp_alice"


#Alice convertendo um bloco de hex para int da blockchain - Passo 9
rawBlock = "00000020586dc51cfdb37ad66c8a8e2656375132f759fc008bea42e86ffbd046f80b00001335a52b662f7b40d5c598e5d4cea2276d757e1709ceaa60db89163e616f6ff925549161ffff001f7d5101000101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1902cd025365787461206d696e65726163616f204e3200000000ffffffff0100f2052a010000001976a914591cbe9f5b9dbaf626bf11b2b3592a11262e051588ac00000000"
rawBlock = textwrap.wrap(rawBlock, 15)


#Alice cifrando um bloco convertido para int criando Vetor CP' - Passo 10 e 11
he_alice = Pyfhel.Pyfhel()
he_alice.restoreContext(localContextBob)
he_alice.restorepublicKey(localChavePKBob)


#Encripta o bloco que foi quebrado em partes menores
for index in range(len(rawBlock)):
    
    print("")
    print(str(index) + ": " + str(rawBlock[index]))
    
    rawBlock[index] = int(rawBlock[index], 16)   
    
    print(str(index) + ": " + str(rawBlock[index]))
    print("")
    
    bloco = he_alice.encryptInt(rawBlock[index])
    bloco.save(localBlocosCP + "/ctx_01bloco" + str(index))


#Alice aplicando homomorfismo bloco CP * CP' e enviando o resultado- Passo 12 e 13
ctxt_restored1 = PyCtxt()
ctxt_restored2 = PyCtxt()

for index in range(len(rawBlock)):
    ctxt_restored1.load(localBlocosCP + "/ctx_01bloco" + str(index), int)
    ctxt_restored2.load(localCPBob, int)
    ctxtMul = he_alice.multiply(ctxt_restored1,ctxt_restored2)

    ctxtMul.save(localCP2 + "/CP2_01bloco" + str(index))
    ctxtMul.save(caminhoBobResp + "/CP2_01bloco" + str(index))








