from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory, connectionDone
from twisted.protocols.basic import LineOnlyReceiver
from twisted.python import failure


class ServerProtocol(LineOnlyReceiver):
    factory: 'Server'
    login: str = None

    def connectionMade(self):
        self.factory.clients.append(self)
        print('new connection')

    def connectionLost(self, reason: failure.Failure = connectionDone):
        self.factory.clients.remove(self)
        if self.login is not None:
            for user in self.factory.clients:
                user.sendLine(f'{self.login} left the chat..'.encode())
        print('connection lost')


    def lineReceived(self, line):
        content = line.decode()
        if self.login is not None:
            content = f'{self.login}: {content}'
            for user in self.factory.clients:
                user.sendLine(content.encode())
        else:
            if content.startswith('login:'):
                self.login = content.replace('login:', '')
                self.sendLine(f'Welcome, {self.login}'.encode())
                for user in self.factory.clients:
                    user.sendLine(f'{self.login} join in chat'.encode())

            else:
                self.sendLine('Invalid login'.encode())


class Server(ServerFactory):
    protocol = ServerProtocol
    clients: list

    def startFactory(self):
        print('Server is alive..')
        self.clients = []

    def stopFactory(self):
        print('Server closed..')


reactor.listenTCP(1234, Server())
reactor.run()
