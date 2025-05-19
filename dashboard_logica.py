from PyQt6.QtWidgets import QApplication, QMainWindow
from dashboard import Ui_MainWindow  # Interfaz del Dashboard (generada desde el .ui)

class DashboardWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la UI del Dashboard
        # Puedes añadir más lógica aquí si lo deseas para el Dashboard

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)  # Asegúrate de tener QApplication importado
    dashboard_window = DashboardWindow()  # Instancia del dashboard
    dashboard_window.show()  # Mostrar la ventana del dashboard
    sys.exit(app.exec())  # Ejecutar la aplicación