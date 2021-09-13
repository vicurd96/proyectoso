from typing import Dict, List, Tuple
import math

class SimuladorMemoria:
    CANT_DIRECCIONES: int = 1024
    _ultimoAcceso: int = 1
    _paginaActual: int = 0
    _procesos: List[int] = []
    _paginaSize: int = 2
    _memoriaPrincipal: List[Dict[int, int]] = []
    _tablaProcesos: List[List[Dict[str, int]]] = []

    def __init__(self):
        numeroPaginas: int = 0
        contadorProgramas: int = 0
        proArchivo = open("plist.txt", "r")
        for line in proArchivo.readlines():
            item: List[str] = line.strip().split()
            if item:
                pid: int = int(item[0])
                size: int = int(item[1])
                self._procesos.insert(pid, size)
                numeroPaginas = int(math.ceil(float(size)/float(self._paginaSize)))
                proceso: List[Dict[str, int]] = []
                for np in range(numeroPaginas):
                    proceso.insert(np, { 'numPag': self._paginaActual, 'enMemoria': 0, 'ultAcceso': 0 })
                    self._paginaActual += 1
                contadorProgramas += 1
                self._tablaProcesos.append(proceso)
        proArchivo.close()
        numeroPaginas: int = int(math.ceil(int(self.CANT_DIRECCIONES) / int(self._paginaSize)))
        paginasPorPrograma: int = int(numeroPaginas) / int(contadorProgramas)
        self._memoriaPrincipal = ({ } for _ in range(numeroPaginas))
        print(self._memoriaPrincipal[0])
        #for i in range(contadorProgramas):
        #    for j in range(paginasPorPrograma):

        #print(self._tablaProcesos[0])
        #simArchivo = open("ptrace.txt", "r")


prueba = SimuladorMemoria()