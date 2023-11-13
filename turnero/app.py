import sys
import typing
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QMainWindow , QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from conexion import Conectar
from tramite import Tipotramite
from historial import historial_tramites
class ejemplo(QMainWindow): #creamos una clase y le pasamos como parametro qmainwindows


    def __init__(self) -> None: #inicializamos el constructor
        super().__init__() #iniciamos un super init
        uic.loadUi("tecladoooo.ui", self)
        # Llamamos al método para cargar el valor global de turno
        self.load_global_turno()

        
        # Conecta las señales de clic de los botones a funciones
        self.boton1.clicked.connect(self.agregar_numero)
        self.boton2.clicked.connect(self.agregar_numero)
        self.boton3.clicked.connect(self.agregar_numero)
        self.boton4.clicked.connect(self.agregar_numero)
        self.boton5.clicked.connect(self.agregar_numero)
        self.boton6.clicked.connect(self.agregar_numero)
        self.boton7.clicked.connect(self.agregar_numero)
        self.boton8.clicked.connect(self.agregar_numero)
        self.boton9.clicked.connect(self.agregar_numero)
        self.boton0.clicked.connect(self.agregar_numero)
        self.entrada = self.findChild(QLineEdit, "entrada")  #asignamos a esta variable el valor
        self.enviar.setEnabled(False)
        self.enviar.clicked.connect(self.guardar_numero)
        self.ticket.setVisible(False)
        
        self.limpiar.clicked.connect(self.limpiarTo)
        self.borrar.clicked.connect(self.borrarto)
        self.Caja.setVisible(False)
        self.Licencia_conducir.setVisible(False)
        self.Catastro.setVisible(False)
        self.Otros.setVisible(False)
        self.Comercio.setVisible(False)
        self.Agua.setVisible(False)
        self.Propiedades.setVisible(False)
        self.Automotor.setVisible(False)
        self.Preferencial.setVisible(False)
        self.Caja.clicked.connect(self.guardartramite)
        self.Caja.clicked.connect(self.tickett)
        
        self.Licencia_conducir.clicked.connect(self.guardartramite)
        self.Licencia_conducir.clicked.connect(self.tickett)
        self.Catastro.clicked.connect(self.guardartramite)
        self.Catastro.clicked.connect(self.tickett)
        self.Otros.clicked.connect(self.guardartramite)
        self.Otros.clicked.connect(self.tickett)
        self.Comercio.clicked.connect(self.guardartramite)
        self.Comercio.clicked.connect(self.tickett)
        self.Agua.clicked.connect(self.guardartramite)
        self.Agua.clicked.connect(self.tickett)
        self.Propiedades.clicked.connect(self.guardartramite)
        self.Propiedades.clicked.connect(self.tickett)
        self.Automotor.clicked.connect(self.guardartramite)
        self.Automotor.clicked.connect(self.tickett)
        self.Preferencial.clicked.connect(self.guardartramite)
        self.Preferencial.clicked.connect(self.tickett)
        self.inicio.setVisible(False)
        
    def guardar_numero(self):
        numero = self.entrada.text()
    # Asegúrate de que el número es válido antes de guardarlo en una variable
        try:
            self.numero = int(numero)
            a = Conectar()
            a.verUsuarios(self.numero)
            
            
            if a.nombre == "DNI INCORRECTO":
                    self.label.setText(str(a.nombre))# le decimos que convierta la tupla en str
                    
            else:
                self.label.setText(str(a.nombre))
                self.sacar()
                    
        except ValueError:
            print('No se ha ingresado un valor numérico')


    def load_global_turno(self):
        # Intenta cargar el valor de global_turno desde el archivo
        try:
            with open("global_turno.txt", "r") as file:
                ejemplo.global_turno = int(file.read())
        except FileNotFoundError:
            ejemplo.global_turno = 0

    def save_global_turno(self):
        # Guarda el valor actual de global_turno en el archivo
        with open("global_turno.txt", "w") as file:
            file.write(str(ejemplo.global_turno))

   
    def guardartramite(self):
        ejemplo.global_turno += 1
        selec = self.sender().text()
        a = Conectar()
        a.verUsuarioId(self.numero)
        a.verTramite(selec)
        self.b = historial_tramites(0, a.idUsu, a.idTra, "Gracias por elegirnos su turno es: " + str(ejemplo.global_turno))
        a.insertarHistorial(self.b)
        self.save_global_turno()  # Guarda el valor actualizado en el archivo
        print("Guardado")
          
          #si al leer el archivo txt es igual a 100 vuelve a 0 
        if ejemplo.global_turno  == 100:
        # Reinicia el valor de global_turno a 0
            ejemplo.global_turno = 0
    def tickett(self):
        self.ticket.setVisible(True)
        self.fecha.setVisible(True)
        self.hora.setVisible(True)
        self.ticket.setText("Gracias por elegirnos su turno es: " + str(ejemplo.global_turno))
        self.fecha.setText(str(self.b.fecha))
        self.hora.setText(str(self.b.hora))
        self.boton1.setVisible(False)
        self.boton2.setVisible(False)
        self.boton3.setVisible(False)
        self.boton4.setVisible(False)
        self.boton5.setVisible(False)
        self.boton6.setVisible(False)
        self.boton7.setVisible(False)
        self.boton8.setVisible(False)
        self.boton9.setVisible(False)
        self.boton0.setVisible(False)
        self.limpiar.setVisible(False)
        self.borrar.setVisible(False)
        self.Caja.setVisible(False)
        self.Licencia_conducir.setVisible(False)
        self.Catastro.setVisible(False)
        self.Otros.setVisible(False)
        self.Comercio.setVisible(False)
        self.Agua.setVisible(False)
        self.Propiedades.setVisible(False)
        self.Automotor.setVisible(False)
        self.Preferencial.setVisible(False)
        self.enviar.setVisible(False)
        self.entrada.setVisible(False)
        

    
            
    def sacar(self):
        
        self.boton1.setVisible(False)
        self.boton2.setVisible(False)
        self.boton3.setVisible(False)
        self.boton4.setVisible(False)
        self.boton5.setVisible(False)
        self.boton6.setVisible(False)
        self.boton7.setVisible(False)
        self.boton8.setVisible(False)
        self.boton9.setVisible(False)
        self.boton0.setVisible(False)
        self.limpiar.setVisible(False)
        self.borrar.setVisible(False)
        self.Caja.setVisible(True)
        self.Licencia_conducir.setVisible(True)
        self.Catastro.setVisible(True)
        self.Otros.setVisible(True)
        self.Comercio.setVisible(True)
        self.Agua.setVisible(True)
        self.Propiedades.setVisible(True)
        self.Automotor.setVisible(True)
        self.Preferencial.setVisible(True)
        self.enviar.setVisible(False)
        self.entrada.setVisible(False)    
   
    
    def agregar_numero(self):
        self.enviar.setEnabled(True)
        # Obtiene el número del botón presionado
        numero = self.sender().text()
        # Obtiene el texto actual del cuadro de entrada (input)
        texto_actual = self.entrada.text()
        # Agrega el número al texto actual
        texto_actual += numero
        # Establece el nuevo texto en el cuadro de entrada
        self.entrada.setText(texto_actual)
        #hacemos invisibles los numeros
        

    def limpiarTo(self):
        self.entrada.clear()
        self.enviar.setEnabled(False)
        self.label.setText("INGRESE SU DNI POR FAVOR")
        self.entrada.setVisible(True)

    def borrarto(self):
        valor_actual = self.entrada.text()
        valor_actual = valor_actual[:-1]
        self.entrada.setText(valor_actual)
        if len(valor_actual) == 0:
            self.enviar.setEnabled(False)
            self.label.setText("INGRESE SU DNI POR FAVOR")
 #aqui cargamos nuestra app
                

#-----desde aqui estamos cargando nuestra app
if __name__ == "__main__":
    app = QApplication(sys.argv) #asignamos estos valores de la libreria
    ventana = ejemplo() # aqui vamos a correr nuestra clase
    ventana.show() #decimos que nos muestre la clase
    sys.exit(app.exec_()) # de esta forma cerramos la app