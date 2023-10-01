# Para cada procesos, o A manteve um valor diferente. Quando A "entra" em cada procesos, ele entra com o valor não alterado, neste caso, A = 1. Como cada processo é isolado, a alteração feita no processo filho não é carregada ao processo pai, de forma que a variável A terá um valor diferente em cada processo, baseado na alteração de cada um.
# No programa, coloquei que o processo filho multiplicará A por 10 e o processo pai por -10, para que seja mais fácil perceber a mudança. Assim, no processo filho, A terminou como 10 e no processo filho, A terminou em -10.

import os
import time

A = 1

pid = os.getpid()
print("PID processo pai %d:"%(pid))

pidFilho = os.fork()
pid = os.getpid()

if pidFilho == 0:
    # ESTÁ NO FILHO
    print("A antes da alteração em %d: %d" %(pidFilho, A))
    A *= 10
    print("A depois da alteração em %d: %d" %(pidFilho, A))
    print("Processo filho %d:"%(pidFilho))
else:
    # ESTÁ NO PAI
    print("A antes da alteração %d: %d" %(pid, A))
    A *= -10
    print("A depois da alteração em %d: %d" %(pid, A))
    print("PID do processo filho visto pelo pai %d:"%(pidFilho))
 

print("Imprimindo A = %d do processo: %d"%(A, pid))
