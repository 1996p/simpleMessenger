import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GUI.gui import Ui_MainWindow
from twisted.internet.protocol import ServerFactory, connectionDone, ClientFactory
from twisted.protocols.basic import LineOnlyReceiver
import sqlite3


class Client(LineOnlyReceiver):
    factory: 'Connector'

    def connectionMade(self):
        print('Connected to server')
        self.factory.window.protocol = self
        self.sendLine(f'login:{self.factory.window.ui.loginField.text()}'.encode())

    def lineReceived(self, line):
        print(line.decode('utf-8'))
        self.factory.window.ui.chatWindow.appendPlainText(line.decode('utf-8'))


class Connector(ClientFactory):
    window: "Messenger"
    protocol = Client

    def __init__(self, application: "Messenger"):
        self.window = application


class Messenger(QMainWindow):
    protocol: Client
    reactor = None

    def __init__(self):
        super(Messenger, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.is_connected = False
        self.is_authenticated = False
        self.btn_functions()
        self.ui.chatWindow.setReadOnly(True)
        self.ui.chatWindow.appendPlainText('Connection to server...')
        self.set_placeholders()

    def set_placeholders(self):
        self.ui.textMsg.setPlaceholderText('Введите сообщение...')
        self.ui.loginField.setPlaceholderText('Введите логин...')
        self.ui.passwordField.setPlaceholderText('Введите пароль...')

    def btn_functions(self):
        self.ui.sendMsgBtn.clicked.connect(self.send_message)
        self.ui.authBtn.clicked.connect(self.authentication)

    def get_content(self) -> str:
        content = self.ui.textMsg.text()
        return content

    def send_message(self):
        if self.is_connected:
            self.protocol.sendLine(self.get_content().encode())
            self.ui.textMsg.clear()
        else:
            self.ui.chatWindow.appendPlainText('Вы не авторизованы!')

    def authentication(self):
        db = sqlite3.connect('db.sqlite3')
        cursor = db.cursor()
        request = f'SELECT login, password FROM auth_data WHERE login="{self.ui.loginField.text()}"'
        cursor.execute(request)
        if (self.ui.loginField.text(), self.ui.passwordField.text()) == cursor.fetchall()[0]:
            if not self.is_connected:
                if self.ui.loginField.text().strip():
                    self.is_connected = True
                    self.ui.loginField.setReadOnly(True)
                    self.ui.passwordField.setReadOnly(True)
                    reactor.connectTCP('127.0.0.1', 1234, Connector(window))
                    window.reactor = reactor
                    reactor.run()
                else:
                    self.ui.chatWindow.appendPlainText('Вы не ввели логин!')
            else:
                """TODO"""
                pass
        else:
            self.ui.chatWindow.appendPlainText("Неверный логин или пароль...")
        db.close()


    def closeEvent(self, **kwargs) -> None:
        self.reactor.callFromThread(self.reactor.stop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    import qt5reactor

    window = Messenger()
    window.show()
    qt5reactor.install()
    from twisted.internet import reactor

    sys.exit(app.exec_())
