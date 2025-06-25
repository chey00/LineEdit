from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QGridLayout, QLineEdit, QLabel, QPushButton


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__username = QLineEdit(self)
        # All input masks: https://doc.qt.io/qt-6/qlineedit.html#inputMask-prop
        # Hier: Zuerst ein beliebiges Zeichen: a-z, A-Z, 0-9, !"§ ...
        #       dann müssen drei Buchstaben folgen: a-z, A-Z
        #       zuletzt könnnen fünf Buchstaben folgen: a-z, A-Z
        self.__username.setInputMask("XAAAaaaaa")

        self.__password = QLineEdit(self)
        self.show_password_released()

        self.__pushButton_password = QPushButton(self)
        self.__pushButton_password.setText("Passwort anzeigen")
        self.__pushButton_password.pressed.connect(self.show_password_pressed)
        self.__pushButton_password.released.connect(self.show_password_released)


        layout = QGridLayout()

        layout.addWidget(QLabel("Benutzername"), 0, 0)
        layout.addWidget(self.__username, 0, 1)

        layout.addWidget(QLabel("Passwort"), 1, 0)
        layout.addWidget(self.__password, 1, 1)
        layout.addWidget(self.__pushButton_password, 1, 2)

        self.setLayout(layout)

    @pyqtSlot()
    def show_password_pressed(self):
        self.__password.setEchoMode(QLineEdit.EchoMode.Normal)

    @pyqtSlot()
    def show_password_released(self):
        self.__password.setEchoMode(QLineEdit.EchoMode.Password)
