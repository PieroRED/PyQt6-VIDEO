import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow
from INICIO import Ui_MainWindow

class VentanaInicio(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Carga la interfaz directamente sobre self

        # Conectar botones directamente
        self.pushButton.clicked.connect(self.abrir_login)
        self.pushButton_2.clicked.connect(self.abrir_registro)

    def abrir_login(self):
        self.close()
        subprocess.Popen([sys.executable, "LOGIN_LOGICA.py"])

    def abrir_registro(self):
        self.close()
        subprocess.Popen([sys.executable, "REGISTRO_LOGICA.py"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaInicio()
    ventana.show()
    sys.exit(app.exec())