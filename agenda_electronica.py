import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QPushButton, QListWidget, QLineEdit, QLabel, 
                             QHBoxLayout, QMessageBox, QDialog)
from PyQt6.QtCore import Qt
import json
from datetime import datetime

class AgendaElectronica(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agenda Electrónica")
        self.setGeometry(100, 100, 600, 400)
        
        self.contactos = []
        self.cargar_contactos()
        
        self.inicializar_ui()
    
    def inicializar_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        
        # Botones principales
        btn_registrar = QPushButton("Registrar Contacto")
        btn_registrar.clicked.connect(self.registrar_contacto)
        layout.addWidget(btn_registrar)
        
        btn_listar = QPushButton("Listar Contactos")
        btn_listar.clicked.connect(self.listar_contactos)
        layout.addWidget(btn_listar)
        
        btn_consultar = QPushButton("Consultar Contacto")
        btn_consultar.clicked.connect(self.consultar_contacto)
        layout.addWidget(btn_consultar)
        
        btn_modificar = QPushButton("Modificar Contacto")
        btn_modificar.clicked.connect(self.modificar_contacto)
        layout.addWidget(btn_modificar)
        
        self.lista_contactos = QListWidget()
        layout.addWidget(self.lista_contactos)
        
        central_widget.setLayout(layout)
    
    def cargar_contactos(self):
        try:
            with open("contactos.json", "r") as file:
                self.contactos = json.load(file)
        except FileNotFoundError:
            self.contactos = []
    
    def guardar_contactos(self):
        with open("contactos.json", "w") as file:
            json.dump(self.contactos, file)
    
    def registrar_contacto(self):
        dialog = RegistroContactoDialog(self)
        if dialog.exec():
            nuevo_contacto = dialog.obtener_contacto()
            self.contactos.append(nuevo_contacto)
            self.guardar_contactos()
            QMessageBox.information(self, "Éxito", "Contacto registrado correctamente.")
    
    def listar_contactos(self):
        self.lista_contactos.clear()
        for contacto in self.contactos:
            self.lista_contactos.addItem(f"{contacto['nombre']} {contacto['apellido']}")
    
    def consultar_contacto(self):
        seleccion = self.lista_contactos.currentItem()
        if seleccion:
            indice = self.lista_contactos.row(seleccion)
            contacto = self.contactos[indice]
            mensaje = f"Nombre: {contacto['nombre']} {contacto['apellido']}\n"
            mensaje += f"Teléfonos: {', '.join(contacto['telefonos'])}\n"
            mensaje += f"Correos: {', '.join(contacto['correos'])}\n"
            mensaje += f"Cumpleaños: {contacto['cumpleanos']}"
            QMessageBox.information(self, "Detalles del Contacto", mensaje)
        else:
            QMessageBox.warning(self, "Error", "Por favor, seleccione un contacto.")
    
    def modificar_contacto(self):
        seleccion = self.lista_contactos.currentItem()
        if seleccion:
            indice = self.lista_contactos.row(seleccion)
            dialog = RegistroContactoDialog(self, self.contactos[indice])
            if dialog.exec():
                self.contactos[indice] = dialog.obtener_contacto()
                self.guardar_contactos()
                self.listar_contactos()
                QMessageBox.information(self, "Éxito", "Contacto modificado correctamente.")
        else:
            QMessageBox.warning(self, "Error", "Por favor, seleccione un contacto.")

class RegistroContactoDialog(QDialog):
    def __init__(self, parent=None, contacto=None):
        super().__init__(parent)
        self.setWindowTitle("Registro de Contacto")
        self.setGeometry(200, 200, 300, 200)
        
        layout = QVBoxLayout()
        
        self.nombre = QLineEdit(contacto['nombre'] if contacto else "")
        layout.addWidget(QLabel("Nombre:"))
        layout.addWidget(self.nombre)
        
        self.apellido = QLineEdit(contacto['apellido'] if contacto else "")
        layout.addWidget(QLabel("Apellido:"))
        layout.addWidget(self.apellido)
        
        self.telefonos = QLineEdit(", ".join(contacto['telefonos']) if contacto else "")
        layout.addWidget(QLabel("Teléfonos (separados por coma):"))
        layout.addWidget(self.telefonos)
        
        self.correos = QLineEdit(", ".join(contacto['correos']) if contacto else "")
        layout.addWidget(QLabel("Correos (separados por coma):"))
        layout.addWidget(self.correos)
        
        self.cumpleanos = QLineEdit(contacto['cumpleanos'] if contacto else "")
        layout.addWidget(QLabel("Fecha de cumpleaños (DD/MM/YYYY):"))
        layout.addWidget(self.cumpleanos)
        
        btn_guardar = QPushButton("Guardar")
        btn_guardar.clicked.connect(self.accept)
        layout.addWidget(btn_guardar)
        
        self.setLayout(layout)
    
    def obtener_contacto(self):
        return {
            "nombre": self.nombre.text(),
            "apellido": self.apellido.text(),
            "telefonos": [t.strip() for t in self.telefonos.text().split(",")],
            "correos": [c.strip() for c in self.correos.text().split(",")],
            "cumpleanos": self.cumpleanos.text()
        }

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = AgendaElectronica()
    ventana.show()
    sys.exit(app.exec())