# ruta para degnier
#.\venv\Lib\site-packages\qt6_applications\Qt\bin\designer.exe

#Entorno virtual
# .\venv\Scripts\Activate 

#crear entorno virtual 

#Se debe crear un app con esta estructura para poder correrlo con este comando
# python main.py

#pyuic6 -o REGISTRO.py REGISTRO.ui

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from LOGIN import Ui_MainWindow
from dashboard_logica import DashboardWindow

# Lista de usuarios registrados con más datos
usuarios_registrados = [
    {"usuario": "admin", "password": "1234", "nombre": "Administrador", "nivel": "Supervisor"},
    {"usuario": "fabio", "password": "abcd", "nombre": "Fabio Rojo", "nivel": "Inicial"},
    {"usuario": "piero", "password": "5678", "nombre": "Piero Morón", "nivel": "Docente"}
]

class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)

        self.intentos_fallidos = 0

    def buscar_usuario(self, usuario, contrasena):
        for u in usuarios_registrados:
            if u["usuario"] == usuario and u["password"] == contrasena:
                return u  # Devuelve el diccionario completo del usuario
        return None

    def login(self):
        user = self.lineEdit.text()
        password = self.lineEdit_2.text()

        usuario_encontrado = self.buscar_usuario(user, password)

        if usuario_encontrado:
            nombre = usuario_encontrado["nombre"]
            nivel = usuario_encontrado["nivel"]
            QMessageBox.information(self, "Bienvenido", f"Hola {nombre}, nivel: {nivel}")
            
            self.dashboard = DashboardWindow()
            self.dashboard.show()
            self.close()
        else:
            self.intentos_fallidos += 1
            intentos_restantes = 3 - self.intentos_fallidos

            if intentos_restantes > 0:
                QMessageBox.critical(
                    self,
                    "Error de Login",
                    f"Usuario o contraseña incorrectos.\nIntentos restantes: {intentos_restantes}"
                )
            else:
                QMessageBox.critical(
                    self,
                    "Acceso bloqueado",
                    "Has excedido el número de intentos.\nInténtalo más tarde."
                )
                self.close()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())

        