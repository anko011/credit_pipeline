import sys

from PyQt6.QtWidgets import QApplication, QWidget


class ApplicationView:
    __app = QApplication(sys.argv)
    __window = QWidget()

    def __init__(self, bank):
        self.__bank = bank

    def init(self):
        self.__window.show()
        self.__app.exec()
