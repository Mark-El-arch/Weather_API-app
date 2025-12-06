import sys, requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QVBoxLayout, QPushButton)
from PyQt5.QtCore import Qt

class Weather_App(QWidget):
    def __init__(self):
        super().__init__()

def main():
    app = QApplication(sys.argv)
    weather_app = Weather_App()
    weather_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()