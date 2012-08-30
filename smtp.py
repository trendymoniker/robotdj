from twisted.internet import reactor, protocol, defer, endpoints
from twisted.mail import imap4
from twisted.python import log, failure
from get_username_password import *

SUBJECT_INDEX = 1
CLIENT_ENDPOINT_DESCRIPTION = "ssl:host=imap.gmail.com:port=993"

#TODO: figure out how to find this value in client
last_message_index = 3

@defer.inlineCallbacks
def connect_client(username="alice", password="secret",
                   #domain='imap.gmail.com', strport="ssl:host=%s:port=993"):
                       strport=CLIENT_ENDPOINT_DESCRIPTION):
    endpoint = endpoints.clientFromString(reactor, strport)#strport % domain)
    factory = protocol.Factory()
    factory.protocol = imap4.IMAP4Client
    try:
        client = yield endpoint.connect(factory)
        print 'connected!'
        yield client.login(username, password)
        print 'logged in!'

    except:
        log.err(failure.Failure(), "IMAP4 client connection failed")
    
    defer.returnValue(client)

@defer.inlineCallbacks
def print_emails(client=None, mailbox='INBOX'):
    
    if not client:
        client = connect_client(get_username_password('No client supplied.  Enter credentials to connect one.'))

    try:
        yield client.select(mailbox)
        info = yield client.fetchEnvelope(imap4.MessageSet(1,last_message_index))

        ## print subjects for all new emails
        #print info[1]['ENVELOPE'][SUBJECT_INDEX]
        
        ## print envelope contents for all new emails
        for i in info:
            print '\n'.join(['Envelope %d : %s' % (i,field) for field in info[i]['ENVELOPE']])

    except:
        log.err(failure.Failure(), "IMAP4 client interaction print_emails failed")
 
    reactor.stop()

@defer.inlineCallbacks
def main(username="alice", password="secret",
         strport=CLIENT_ENDPOINT_DESCRIPTION):
    '''
    Twisted's example smtp program.
    '''
    endpoint = endpoints.clientFromString(reactor, strport)
    factory = protocol.Factory()
    factory.protocol = imap4.IMAP4Client

    try:
        client = yield endpoint.connect(factory)
        yield client.login(username, password)
        yield client.select('INBOX')
        info = yield client.fetchEnvelope(imap4.MessageSet(1))
        print info[1]['ENVELOPE'][1]
    except:
        log.err(failure.Failure(), "IMAP4 client interaction failed")
    reactor.stop()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = get_username()
        
    password = get_password()
    
    ''' Run Twisted's example program
    main(username, password)
    reactor.run()
    '''
    connect_client(username, password).addCallback(print_emails)

    reactor.run()
    #reactor.stop()
