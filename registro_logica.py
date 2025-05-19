from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from REGISTRO import Ui_MainWindow  # Asumiendo que tienes un archivo REGISTRO.py con la interfaz
from dashboard_logica import DashboardWindow

# Lista de usuarios registrados
usuarios_registrados = [
    {"usuario": "admin", "password": "1234", "nombre": "Administrador", "nivel": "Supervisor"},
    {"usuario": "fabio", "password": "abcd", "nombre": "Fabio Rojo", "nivel": "Inicial"},
    {"usuario": "piero", "password": "5678", "nombre": "Piero Morón", "nivel": "Docente"}
]

class RegistroWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz directamente sobre self

        self.pushButton.clicked.connect(self.registrar_usuario)  # Conectar el botón directamente

    def registrar_usuario(self):
        user = self.lineEdit.text()  # Acceder al campo de texto directamente
        password = self.lineEdit_2.text()  # Acceder al campo de contraseña directamente
        nombre = self.lineEdit_3.text()  # Acceder al campo de nombre
        nivel = self.comboBox.currentText()  # Acceder al nivel seleccionado

        if user and password and nombre and nivel:
            # Simular la "registración" añadiendo a la lista de usuarios
            usuarios_registrados.append({
                "usuario": user,
                "password": password,
                "nombre": nombre,
                "nivel": nivel
            })
            QMessageBox.information(self, "Registro Exitoso", f"Usuario {nombre} registrado correctamente.")
            self.close()  # Cierra la ventana después de registrarse
            self.dashboard = DashboardWindow()
            self.dashboard.show()  # Muestra el dashboard
        else:
            QMessageBox.warning(self, "Error", "Por favor completa todos los campos.")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    registro_window = RegistroWindow()
    registro_window.show()
    sys.exit(app.exec())