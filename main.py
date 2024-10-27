from PySide6.QtWidgets import QApplication

from src import MainController

if __name__ == '__main__':
    app = QApplication([])
    window = MainController()
    window.show()
    app.exec()
