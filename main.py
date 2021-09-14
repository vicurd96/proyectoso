from typing import Dict, List, Tuple
import math

class SimuladorMemoria:
    CANT_DIRECCIONES: int = 1024
    _ultimoAcceso: int = 1
    _paginaActual: int = 0
    _procesos: List[int] = []
    _paginaSize: int = 2
    _memoriaPrincipal: List[Dict[int, int]] = []
    _tabla: List[List[Dict[str, int]]] = []
    _contadorFalloPagina: int = 0

    def _getLocalizacionMemoria(self, pid: int, localizacion: int):
        if(localizacion < 0 or localizacion > self._procesos[pid]):
            raise ValueError("Localización de memoria inválida para el proceso")
        return int(int(math.ceil(float(float(localizacion)/float(self._paginaSize)))) - 1)

    def __init__(self):
        numeroPaginas: int = 0
        contadorProgramas: int = 0
        proArchivo = open("plist.txt", "r")
        for line in proArchivo.readlines():
            item: List[str] = line.strip().split()
            if item:
                pid: int = int(item[0])
                memLocation: int = int(item[1])
                self._procesos.insert(pid, memLocation)
                numeroPaginas = int(math.ceil(float(memLocation)/float(self._paginaSize)))
                proceso: List[Dict[str, int]] = []
                for np in range(numeroPaginas):
                    proceso.insert(np, { 'numPag': self._paginaActual, 'enMemoria': 0, 'ultAcceso': 0 })
                    self._paginaActual += 1
                contadorProgramas += 1
                self._tabla.append(proceso)
        
        proArchivo.close()
        numeroPaginas: int = int(math.ceil(int(self.CANT_DIRECCIONES) / int(self._paginaSize)))
        paginasPorPrograma: int = int(numeroPaginas) / int(contadorProgramas)

        for i in range(contadorProgramas):
            for j in range(paginasPorPrograma):
                self._memoriaPrincipal.insert(j + paginasPorPrograma * i, self._tabla[i][j])
                self._tabla[i][j]['enMemoria'] = 1
                self._tabla[i][j]['ultAcceso'] = self._ultimoAcceso
                self._ultimoAcceso += 1
            
        numeroPaginas = paginasPorPrograma * contadorProgramas
        #tempSize: int = 0

        memArchivo = open("mlist.txt", "r")
        for line in memArchivo.readlines():
            item: List[str] = line.strip().split()
            if item:
                pid: int = int(item[0])
                memLocation: int = int(item[1])
                if(self._tabla[pid][self._getLocalizacionMemoria(pid, memLocation)]['enMemoria'] == 1):
                    self._contadorFalloPagina += 1
                    #FIFO
                    tiempoMinimo = self._ultimoAcceso
                    indiceIntercambio = 0
                    for i in range(numeroPaginas):
                        if(tiempoMinimo > self._memoriaPrincipal[i]['ultAcceso']):
                            indiceIntercambio = i
                            tiempoMinimo = self._memoriaPrincipal[i]['ultAcceso']
                    
                    self._memoriaPrincipal[indiceIntercambio]['enMemoria'] = 0
                    self._memoriaPrincipal[indiceIntercambio] = self._tabla[pid][self._getLocalizacionMemoria(pid, memLocation)]
                    self._memoriaPrincipal[indiceIntercambio]['enMemoria'] = 1
                    self._memoriaPrincipal[indiceIntercambio]['ultAcceso'] = self._ultimoAcceso


prueba = SimuladorMemoria()