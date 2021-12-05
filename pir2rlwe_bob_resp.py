import Pyfhel
from Pyfhel import PyCtxt, PyPtxt
import tempfile
from pathlib import Path
import faulthandler; faulthandler.enable()
import textwrap



#Bob recuperanco o bloco int
he_bob = Pyfhel.Pyfhel()
he_bob.restoreContext(localContextBob)
he_bob.restorepublicKey(localChavePKBob)
he_bob.restoresecretKey("./imeCoin/bob/chaves/sec3.key")
ctxt_restored = PyCtxt()


#ctxt_restored.load("./chaves/enc/ctx_01bloco0", int)
rawBlock1 = he_bob.decryptInt(ctxtMul)

#Coloca a parte do bloco no formato original
print('{:015x}'.format(rawBlock1))





