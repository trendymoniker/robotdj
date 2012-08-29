from twisted.internet import reactor, protocol, defer, endpoints
from twisted.mail import imap4
from twisted.python import log, failure
from get_username_password import *

@defer.inlineCallbacks
def main(username="alice", password="secret",
         strport="ssl:host=imap.gmail.com:port=993"):
    endpoint = endpoints.clientFromString(reactor, strport)
    factory = protocol.Factory()
    factory.protocol = imap4.IMAP4Client
    try:
        client = yield endpoint.connect(factory)
        yield client.login(username, password)
        yield client.select('INBOX')

        #print subjects for all new emails
        info = yield client.fetchEnvelope(imap4.MessageSet(1))
        print info[1]['ENVELOPE'][1]
    except:
        log.err(failure.Failure(), "IMAP4 client interaction failed")
    reactor.stop()

import sys
username, password = get_username_password()
main(username, password)
reactor.run()
