from twisted.internet import protocol, reactor
import pyttsx

class Echo(protocol.Protocol):
#    def __init__(self):
#        self.engine = pyttsx.init()
#        self.voices = self.engine.getProperty('voices')

    def dataReceived(self, data):
        self.transport.write(data)
        print data
        self.engine.stop()
        self.engine.say(data)
        self.engine.runAndWait() 

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        out = Echo()
        out.engine = pyttsx.init()
        out.voices = out.engine.getProperty('voices')

        return out



reactor.listenTCP(1234, EchoFactory())
reactor.run()
