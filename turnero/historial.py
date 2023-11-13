from conexion import Conectar
from datetime import *

class historial_tramites:
    idHistorial = 0
    idUsuario = 0
    idTramite = 0
    descripcion = ""
    fecha = date.today()
    hora = datetime.now().time()
    def __init__(self, idHistorial, idUsuario, idTramite, descripcion, fecha=None, hora=None):
        self.idHistorial = idHistorial
        self.idUsuario = idUsuario
        self.idTramite = idTramite
        self.descripcion = descripcion
        self.fecha = fecha if fecha else date.today()
        self.hora = hora if hora else datetime.now().time()

    def get_idHistorial(self):
        return self.idHistorial

    def set_idHistorial(self, idHistorial):
        self.idHistorial = idHistorial

    def get_idUsuario(self):
        return self.idUsuario

    def set_idUsuario(self, idUsuario):
        self.idUsuario = idUsuario

    def get_idTramite(self):
        return self.idTramite

    def set_idTramite(self, idTramite):
        self.idTramite = idTramite
    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_fecha(self):
        return str(self.fecha)

    def set_fecha(self, fecha):
        self.fecha = fecha

    def get_hora(self):
        return str(self.hora)
    def set_hora(self,hora):
        self.hora = hora
        