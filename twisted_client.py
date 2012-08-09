from twisted.internet import reactor
from twisted.internet.protocol import Factory, Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint

class Greeter(Protocol):
    def sendMessage(self, msg):
        print 'sent message:'+"MESSAGE %s\n" % msg    
        self.transport.write("MESSAGE %s\n" % msg)

class GreeterFactory(Factory):
    def buildProtocol(self, addr):
        print 'building protocol'    
        return Greeter()

def gotProtocol(p):
    p.sendMessage("Hello")
    reactor.callLater(1, p.sendMessage, "This is sent in a second")
    reactor.callLater(2, p.transport.loseConnection)

point = TCP4ClientEndpoint(reactor, "localhost", 1234)
print 'point is set!'
d = point.connect(GreeterFactory())
d.addCallback(gotProtocol)
print 'about to run reactor:'
reactor.run()
