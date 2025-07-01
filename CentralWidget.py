from PyQt6.QtCore import pyqtSlot, Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QWidget, QGridLayout, QLineEdit, QLabel, QPushButton


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__username = QLineEdit(self)
        # All input masks: https://doc.qt.io/qt-6/qlineedit.html#inputMask-prop
        # Hier: Zuerst ein beliebiges Zeichen: a-z, A-Z, 0-9, !"§ ...
        #       dann müssen drei Buchstaben folgen: a-z, A-Z
        #       zuletzt könnnen fünf Buchstaben folgen: a-z, A-Z
        #self.__username.setInputMask("XAAAaaaaa")
        #self.__username.setInputMask("X" + "AAA" + "aaaaa")
        #self.__username.setInputMask("X" + "." + 3 * "A" + "-" + 5 * "a")
        #self.__username.setPlaceholderText("Username")
        self.__username.setToolTip("Halllooooo")

        self.__password = QLineEdit(self)
        # An das Kennwort sind folgende Anforderungen gestellt:
        # Zuerst müssen vier Ziffern eingegeben werden,
        # danach folgen zwei beliebige Zeichen (inlusive Sonderzeichen)
        # zuletzt kommen sechs Hexadezimale.
        self.__password.setInputMask(4 * "9" + 2 * "X" + 6 * "H")
        self.__password.setPlaceholderText("Password")

        self.show_password_released()

        # Erweitern Sie die GUI um zwei weitere Eingabefelder für
        # IP-Adresse: vier Blöcke mit je drei Ziffern,
        #             welche durch einen Punkt getrennt sind.
        self.__ip = QLineEdit(self)
        self.__ip.setInputMask(3 * "009." + "009" + ";_")

        # und
        # MAC-Adresse: sechs Blöcke mit je zwei Hexadezimalen,
        #              welche durch einen Bindestrich getrennt sind.
        self.__mac = QLineEdit(self)
        self.__mac.setInputMask(5 * "hH-" + "hH" + ";_")

        self.__max_length = QLineEdit(self)
        self.__max_length.setMaxLength(5)

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

        layout.addWidget(QLabel("IP"), 2, 0)
        layout.addWidget(self.__ip, 2, 1)

        layout.addWidget(QLabel("MAC"), 3, 0)
        layout.addWidget(self.__mac, 3, 1)

        layout.addWidget(QLabel("Eingabelänge"), 4, 0)
        layout.addWidget(self.__max_length, 4, 1)


        self.setLayout(layout)

    @pyqtSlot()
    def show_password_pressed(self):
        self.__password.setEchoMode(QLineEdit.EchoMode.Normal)

    @pyqtSlot()
    def show_password_released(self):
        self.__password.setEchoMode(QLineEdit.EchoMode.Password)
