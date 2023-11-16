import mysql.connector
from usuario import Usuario


import datetime



class Conectar():
        
        try:
            def __init__(self):
                self.conexion = mysql.connector.connect(host="localhost",
                                                    user="root",
                                                    password="Sferreyra$2002",
                                                    database="nuevoturnero")
                if self.conexion.is_connected:
                    print("Conexión a la base de datos exitosa.")
        except mysql.connector.Error as error:
            print("No se pudo conectar a la base de datos.", error)


        def insertar(self,a):
            if self.conexion.is_connected:
                try:
                    cursor = self.conexion.cursor()
                    sql = "INSERT INTO usuario values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    valores = (a.getidUsuario(),
                        a.getdni(),
                       a.getnombre(),
                       a.getapellido(),
                       a.getnacimiento(),
                       a.getfallecimiento(),
                        a.getdomicilio(),
                        a.gettelefono(),
                       a.getemail(),
                       a.getestadocivil(),
                       a.getsexo(),
                       a.getobservacion()
                       )
                    cursor.execute(sql, valores)
                    self.conexion.commit()
                    self.conexion.close()
                    print("insert exitoso")
                except mysql.connector.Error as error:
                     print(error)

        
        def verUsuarios(self,a):
             if self.conexion.is_connected:
                    
                    
                    try:
                        
                        cursor = self.conexion.cursor()
                        consulta = "SELECT nombre, apellido FROM usuario where dni = %s" %(int(a))
                        cursor.execute(consulta)
                        resultados = cursor.fetchall()
                        self.nombre = ""
                        if len(resultados) < 1:
                                self.nombre = "DNI INCORRECTO"
                                print("")
                                print("---| no hay datos para mostrar |---")
                        
                                self.conexion.close()
                        else:
                            for i in resultados:
                                self.nombre = "Bienvenid@ " + "\n".join(i) #para que realize un salto de lina en la tupla 
                                print(i)
                                return i
                                self.conexion.close()
                    except mysql.connector.Error() as error:
                         print(error)
            
       
        def insertHistorial(self,a):
             cursor = self.conexion.cursor()
             sql = "INSERT INTO historial_tramites values(%s,%s,%s)"
             valor = (a.get_idHistorial(),
                      a.get_idUsuario(),
                      a.get_idTramite()
                      )
             cursor.execute(sql,valor)
             self.conexion.commit()
             self.conexion.close()
             print ("Registro exitoso")
        #probando lo de abajo
        def verhistorial(self,a):
             cursor = self.conexion.cursor()
             sql = "SELECT idUsuario from usuario where dni = %s" %(int(a))
             cursor.execute(sql)
             resultados = cursor.fetchone()
             self.idUsu = 0
             if resultados is None:
                  print("no existe usuario")
             else:
                for i in resultados:
                                 
                                self.idUsu = i
                                print(i)
                                return i
                                self.conexion.close()
        def verTramite(self,a):
             cursor = self.conexion.cursor()
             self.idTra = 0
             sql = "SELECT idTramite FROM tramite WHERE tipode_tramite = %s"
             valor = a
             
             cursor.execute(sql, (valor,))
             resultados = cursor.fetchone()
             self.idTra = 0
             if resultados is None:
                  print("no existe usuario")
             else:
                for i in resultados:
                                 
                                self.idTra = i
                                print(i)
                                return i
                                self.conexion.close()
        def verUsuarioId(self,a):
             cursor = self.conexion.cursor()
             sql = "select idUsuario from usuario where dni = %s"%(int(a))
             cursor.execute(sql)
             resultados = cursor.fetchone()
             self.idUsu = 0
             if resultados is None:
                  print("no existe usuario")
             else:
                for i in resultados:
                                 
                                self.idUsu = i
                                print(i)
                                return i
                                self.conexion.close()

        def insertarHistorial(self,a):
            try:
                 cursor = self.conexion.cursor()
                 sql = "INSERT INTO historial_tramites values(%s,%s,%s,%s,%s,%s)"
                 valor = (a.get_idHistorial(),
                          a.get_idUsuario(),
                          a.get_idTramite(),
                          a.get_descripcion(),
                          a.get_fecha(),
                          a.get_hora()
                          )
                 cursor.execute(sql,valor)
                 self.conexion.commit()
                 self.conexion.close()
                 print ("Registro exitoso")
            except mysql.connector.Error as error:
                 print(error)
        def insertarTurno(self,a):
              try:
                    cursor = self.conexion.cursor()
                    sql = "INSERT INTO turno VALUES(%s,%s,%s,%s,%s)"
                    valor = (a.get_idTurno(),
                             a.get_idUsuario(),
                             a.get_idTramite(),
                             a.get_descripcion(),
                             a.get_fecha())
                    cursor.execute(sql, valor)
                    self.conexion.commit()
                    self.conexion.close()
                    print("se inserto correcto")
              except mysql.connector.Error as error:
                    print(error)




