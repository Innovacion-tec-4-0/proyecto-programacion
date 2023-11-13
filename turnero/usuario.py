import datetime

class Usuario():
    idUsuario = 0
    dni = 0
    nombre = ""
    apellido = ""
    nacimiento = ""
    fallecimiento = ""
    domicilio = ""
    telefono = 0
    email = ""
    estadocivil = ""
    sexo = ""
    observacion = ""
    def __init__(self, idUsuario, dni, nombre, apellido, nacimiento, fallecimiento, domicilio, telefono, email, estadocivil, sexo, observacion):
        self.idUsuario = idUsuario
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.fallecimiento = fallecimiento
        self.domicilio = domicilio
        self.telefono = telefono
        self.email = email
        self.estadocivil = estadocivil
        self.sexo = sexo
        self.observacion = observacion


    def getidUsuario (self):
        return self.idUsuario
        
    def getdni (self):
        return self.dni
        
    def getnombre (self):
        return self.nombre
        
    def getapellido (self):
        return self.apellido
        
    def getnacimiento (self):
        return self.nacimiento
        
    def getfallecimiento (self):
        return self.fallecimiento
        
    def getdomicilio (self):
        return self.domicilio
        
    def gettelefono (self):
        return self.telefono
        
    def getemail (self):
        return self.email
        
    def getestadocivil (self):
        return self.estadocivil
        
    def getsexo (self):
        return self.sexo
        
    def getobservacion (self):
        return self.observacion
        
    

    def setidUsuario (self, idUsuario):
        self.idUsuario = idUsuario

    def setdni (self, dni):
        self.dni = dni

    def setnombre (self, nombre):
        self.nombre = nombre

    def setapellido(self, apellido):
        self.apellido = apellido

    def setnacimiento (self, nacimiento):
        self.nacimiento = nacimiento

    def setfallecimiento (self, fallecimiento):
        self.fallecimiento = fallecimiento

    def setdomicilio (self, domicilio):
        self.domicilio = domicilio

    def settelefono (self, telefono):
        self.telefono = telefono

    def setemail (self, email):
        self.email = email

    def setestadocivil (self, estadocivil):
        self.estadocivil = estadocivil

    def setsexo (self, sexo):
        self.sexo = sexo

    def setobservacion (self, observacion):
        self.observacion = observacion
        