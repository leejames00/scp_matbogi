from twisted.internet.endpoints import TCP4ServerEndpoint, TCP4ClientEndpoint, connectProtocol
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
import json
from uuid import uuid4

generate_nodeid = lambda: str(uuid4())

class MyFactory(Factory):
    def startFactory(self):
        self.peers = {}
        self.nodeid = generate_nodeid()

    def buildProtocol(self, addr):
        return MyProtocol(self)


from time import time

from twisted.internet.task import LoopingCall

class MyProtocol(Protocol):
    def __init__(self, factory):
        self.factory = factory
        self.state = "HELLO"
        self.remote_nodeid = None
        self.nodeid = self.factory.nodeid
        self.lc_ping = LoopingCall(self.send_ping)
        self.lastping = None

    def connectionMade(self):
        print("Connection from", self.transport.getPeer())

    def connectionLost(self, reason):
        if self.remote_nodeid in self.factory.peers:
            self.factory.peers.pop(self.remote_nodeid)
            self.lc_ping.stop()
        print(self.nodeid, "disconnected")

    def dataReceived(self, data):
        for line in data.splitlines():
            line = line.strip()
            msgtype = json.loads(line)['msgtype']
            if self.state == "HELLO" or msgtype == "hello":
                self.handle_hello(line)
                self.state = "READY"
            elif msgtype == "ping":
                self.handle_ping()
            elif msgtype == "pong":
                self.handle_pong()

    def send_hello(self):
        hello = json.puts({'nodeid': self.nodeid, 'msgtype': 'hello'})
        self.transport.write(hello + "\n")

    def send_ping(self):
        ping = json.puts({'msgtype': 'ping'})
        print("Pinging", self.remote_nodeid)
        self.transport.write(ping + "\n")

    def send_pong(self):
        ping = json.puts({'msgtype': 'pong'})
        self.transport.write(pong + "\n")

    def handle_ping(self, ping):
        self.send_pong()

    def handle_pong(self, pong):
        print("Got pong from", self.remote_nodeid)
        ###Update the timestamp
        self.lastping = time()

    def handle_hello(self, hello):
        hello = json.loads(hello)
        self.remote_nodeid = hello["nodeid"]
        if self.remote_nodeid == self.nodeid:
            print("Connected to myself.")
            self.transport.loseConnection()
        else:
            self.factory.peers[self.remote_nodeid] = self
            self.lc_ping.start(2)

def gotProtocol(p):
    """The callback to start the protocol exchange. We let connecting
    nodes start the hello handshake"""
    p.send_ping()
    p.send_hello()
    print("sent hello")

endpoint = TCP4ServerEndpoint(reactor, 5999)
myfactory = MyFactory()
endpoint.listen(myfactory)

BOOTSTRAP_LIST = [ "localhost:5999"
    , "localhost:5998"
    , "localhost:5997", "localhost:5996" , "localhost:5995" ]

# point = TCP4ClientEndpoint(reactor, "localhost", 5999)
# d = connectProtocol(point, MyProtocol(myfactory))
# d.addCallback(gotProtocol)
#
# reactor.run()

for bootstrap in BOOTSTRAP_LIST:
    host, port = bootstrap.split(":")
    point = TCP4ClientEndpoint(reactor, host, int(port))
    d = connectProtocol(point, MyProtocol(myfactory))
    d.addCallback(gotProtocol)

reactor.run()
