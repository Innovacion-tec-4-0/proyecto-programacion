import mysql.connector #importamos la libreria
from tablas import Ciudadanos
class BaseDeDatos():
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = "localhost",
                user = "root",
                port = 3306,
                password = "pancho1677",
                database = "ciudadanos"
            )
            if self.conexion.is_connected:
                print("conexion exitosa") 
        except mysql.connector.Error as error:
            print("ah ocurrido este error: ", error)
    
    def insertar_usuario(self, a):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sentenciaSql = "INSERT INTO ciudadanos values(%s, %s, %s, %s, %s, %s, %s, %s)"               
                data = (a.getdni(),
                        a.getnombre(),
                        a.getapellido(),
                        a.getsexo(),
                        a.getfecha_nacimiento(),
                        a.getfecha_fallecimiento(),
                        a.getestado_civil(),
                        a.getnacionalidad()
                        )
                
                
                cursor.execute(sentenciaSql, data)
                self.conexion.commit()
                self.conexion.close()
            except mysql.connector.Error as error:
                print("ah ocurrido este error: ", error)


datos = Ciudadanos(33293178, "gaston", "trejo", "masculino", "02/06/1988", "no", "casado", "argentino")
a = BaseDeDatos()
a.insertar_usuario(datos)