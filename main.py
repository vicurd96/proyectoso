from typing import Dict, List


class SimuladorMemoria:
    CANT_DIRECCIONES: int = 1024
    _ultimoAcceso: int = 1
    _paginaActual: int = 0
    _procesos: List[Dict[int, int]] = []
    _paginaSize: int = 2
    _memoriaPrincipal: List[Dict[int, int]] = []
    _tablaProcesos: List[Dict[int, int]] = []

    def __init__(self):
        proArchivo = open("plist.txt", "r")
        simArchivo = open("ptrace.txt", "r")


prueba = SimuladorMemoria()