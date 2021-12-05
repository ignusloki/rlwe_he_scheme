import Pyfhel
from Pyfhel import PyCtxt, PyPtxt
import tempfile
from pathlib import Path
import faulthandler; faulthandler.enable()
import textwrap



def splitstring(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    return string1, string2



#Alice convertendo um bloco de hex para int - Passo 9
rawBlock = "00000020586dc51cfdb37ad66c8a8e2656375132f759fc008bea42e86ffbd046f80b00001335a52b662f7b40d5c598e5d4cea2276d757e1709ceaa60db89163e616f6ff925549161ffff001f7d5101000101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1902cd025365787461206d696e65726163616f204e3200000000ffffffff0100f2052a010000001976a914591cbe9f5b9dbaf626bf11b2b3592a11262e051588ac00000000"
rawBlock = textwrap.wrap(rawBlock, 15)


#Alice cifrando um bloco convertido para int criando Vetor CP' - Passo 10 e 11
he_alice = Pyfhel.Pyfhel()
localContextBob = "./chaves/context_0"
localChavePKBob = "./chaves/pub0.key"
he_alice.restoreContext(localContextBob)
he_alice.restorepublicKey(localChavePKBob)


for index in range(len(rawBlock)):
    print("")
    print(str(index) + ": " + str(rawBlock[index]))
    rawBlock[index] = int(rawBlock[index], 16)   
    print(str(index) + ": " + str(rawBlock[index]))
    print("")
    y = he_alice.encryptInt(rawBlock[index])
    y.save("./chaves/enc/ctx_01bloco" + str(index))


#Alice aplicando homomorfismo bloco CP * CP'- Passo 12
ctxt_restored1 = PyCtxt()
ctxt_restored2 = PyCtxt()
ctxt_restored1.load("./chaves/enc/ctx_01bloco0", int)
ctxt_restored2.load("./chaves/enc/ctx0", int)
ctxtMul = he_alice.multiply(ctxt_restored1,ctxt_restored2)









