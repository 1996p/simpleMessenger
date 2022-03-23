import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GUI.gui import Ui_MainWindow
from twisted.internet.protocol import ServerFactory, connectionDone, ClientFactory
from twisted.protocols.basic import LineOnlyReceiver
from twisted.python import failure


class Client(LineOnlyReceiver):
    factory: 'Connector'

    def connectionMade(self):
        print('Connected to server')
        self.factory.window.protocol = self

    def lineReceived(self, line):
        print(line.decode('utf-8'))
        self.factory.window.ui.chatWindow.appendPlainText(line.decode('utf-8'))


class Connector(ClientFactory):
    window: "Messenger"
    protocol = Client

    def __init__(self, application):
        self.window = application


class Messenger(QMainWindow):
    protocol: Client
    reactor = None

    def __init__(self):
        super(Messenger, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.btn_functions()
        self.ui.chatWindow.setReadOnly(True)
        self.ui.chatWindow.appendPlainText('Connection to server...')

    def btn_functions(self):
        self.ui.sendMsgBtn.clicked.connect(self.send_message)

    def get_content(self) -> str:
        content = self.ui.textMsg.text()
        return content

    def send_message(self):
        self.protocol.sendLine(self.get_content().encode())
        self.ui.textMsg.clear()

    def closeEvent(self, **kwargs) -> None:
        self.reactor.callFromThread(self.reactor.stop)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    import qt5reactor
    window = Messenger()
    window.show()
    qt5reactor.install()
    from twisted.internet import reactor
    reactor.connectTCP('127.0.0.1', 1234, Connector(window))
    window.reactor = reactor
    reactor.run()
    sys.exit(app.exec_())
