from typing import Dict, List, Tuple
import math
from tkinter import Tk, Canvas, Label
import random

class SimuladorMemoria:
    CANT_DIRECCIONES: int = 32
    _ultimoAcceso: int = 1
    _paginaActual: int = 0
    _procesos: List[int] = []
    _paginaSize: int = 2
    _memoriaPrincipal: List[Dict[int, int]] = []
    _tabla: List[List[Dict[str, int]]] = []
    _contadorFalloPagina: int = 0
    _root: Tk

    def _getLocalizacionMemoria(self, pid: int, localizacion: int):
        if(localizacion < 0 or localizacion > self._procesos[pid]):
            raise ValueError("Localización de memoria inválida para el proceso")
        return int(int(math.ceil(float(float(localizacion)/float(self._paginaSize)))) - 1)

    def __init__(self, root):
        r = lambda: random.randint(0,255)
        self._root = root
        self._root.minsize(400,600)

        canvas_tabla_height = 23
        canvas_memoria_height = 50
        canvas_width = 1024

        label = Label(root,text='Simulador de Paginación en Memoria')
        label.pack()
        w = Canvas(root, width=(canvas_width + 10), height=canvas_memoria_height)
        w.pack()

        numeroPaginas: int = 0
        contadorProgramas: int = 0
        proArchivo = open("plist.txt", "r")
        for line in proArchivo.readlines():
            item: List[str] = line.strip().split()
            if item:
                pid: int = int(item[0])
                memSize: int = int(item[1])
                self._procesos.insert(pid, memSize)
                numeroPaginas = int(math.ceil(float(memSize)/float(self._paginaSize)))
                proceso: List[Dict[str, int]] = []
                for np in range(numeroPaginas):
                    proceso.insert(np, { 'numPag': self._paginaActual, 'enMemoria': 0, 'ultAcceso': 0 })
                    self._paginaActual += 1
                contadorProgramas += 1
                self._tabla.append(proceso)
        
        proArchivo.close()
        numeroPaginas: int = int(math.ceil(int(self.CANT_DIRECCIONES) / int(self._paginaSize)))
        paginasPorPrograma: int = int(int(numeroPaginas) / int(contadorProgramas))

        for i in range(contadorProgramas):
            for j in range(paginasPorPrograma):
                self._memoriaPrincipal.insert(j + paginasPorPrograma * i, self._tabla[i][j])
                self._tabla[i][j]['enMemoria'] = 1
                self._tabla[i][j]['ultAcceso'] = self._ultimoAcceso
                self._ultimoAcceso += 1
        
        desde = 10
        hasta = int((canvas_width - 200) / numeroPaginas)
        for programa in range(self._tabla.__len__()):
            for pagina in self._tabla[programa]:
                w.create_rectangle(desde, canvas_tabla_height, hasta, 2, fill='green' if pagina['enMemoria'] == 1 else 'red')
                w.create_text(desde + 10, canvas_tabla_height / 2, text=pagina['numPag'], fill='black' if pagina['enMemoria'] == 1 else 'white')
                desde = hasta + 1;
                hasta += int((canvas_width - 200) / numeroPaginas)
        
        desde = 10
        hasta = int((canvas_width) / self._memoriaPrincipal.__len__())
        contador = 0
        for paginaEnMemoria in self._memoriaPrincipal:
            w.create_rectangle(desde, canvas_tabla_height + 4, hasta, canvas_memoria_height, fill='green')
            w.create_text(desde + 30, (canvas_memoria_height + canvas_tabla_height) / 2, text='Pag. {}'.format(paginaEnMemoria['numPag']), fill='black' if paginaEnMemoria['enMemoria'] == 1 else 'white')
            desde = hasta + 1;
            hasta += int((canvas_width) / self._memoriaPrincipal.__len__())
            contador += 1

        numeroPaginas = paginasPorPrograma * contadorProgramas
        #tempSize: int = 0
'''
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

'''
root = Tk()
prueba = SimuladorMemoria(root)
root.mainloop()