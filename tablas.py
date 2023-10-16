class Ciudadanos():
    dni = 0
    nombre = ""
    apellido = ""
    sexo = ""
    fecha_nacimiento = ""
    fecha_fallecimiento = ""
    estado_civil = ""
    nacionalidad = ""

    def __init__(self, dni, nombre, apellido, sexo, fecha_nacimiento, fecha_fallecimiento, estado_civil, nacionalidad):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_fallecimiento = fecha_fallecimiento
        self.estado_civil = estado_civil
        self.nacionalidad = nacionalidad
    def getdni(self):
        return self.dni
    def getnombre(self):
        return self.nombre
    def getapellido(self):
        return self.apellido
    def getsexo(self):
        return self.sexo
    def getfecha_nacimiento(self):
        return self.fecha_nacimiento
    def getfecha_fallecimiento(self):
        return self.fecha_fallecimiento
    def getestado_civil(self):
        return self.estado_civil
    def getnacionalidad(self):
        return self.nacionalidad
    def setdni(self, dni):
        self.dni = dni
    def setnombre(self, nombre):
        self.nombre = nombre
    def setapellido(self, apellido):
        self.apellido=apellido
    def setsexo(self, sexo):
        self.sexo = sexo
    def setfecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento
    def setfecha_fallecimiento(self, fecha_fallecimiento):
        self.fecha_fallecimiento = fecha_fallecimiento
    def setestado_civil(self, estdo_civil):
        self.estado_civil = estdo_civil
    def setnacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad

class Contacto():
    def __init__(self, dni, tel_fijo, celular, email):
        self.dni = dni
        self.tel_fijo = tel_fijo
        self.celular = celular
        self.email = email

class Direccion():
    def __init__(self, dni, calle, numero, piso, dpto, torre, barrio, direccincol, localidad, provincia, pais):
        self.dni = dni
        self.calle = calle
        self.numero = numero
        self.piso = piso
        self.dpto = dpto
        self.torre = torre
        self.barrio = barrio
        self.direccioncol = direccincol
        self.localidad = localidad
        self.provincia = provincia
        self.pais = pais
    
class Profesion():
    def __init__(self,dni, profesion):
        self.dni = dni
        self.profesion = profesion
     
        