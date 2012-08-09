import pyttsx

from gi.repository import RB, Peas, GObject
class RobotDJPlugin (GObject.Object, Peas.Activatable):
    object = GObject.property(type=GObject.Object)

    def __init__(self):
        super(RobotDJPlugin, self).__init__()

    def do_activate(self):
        print "Hello World"
        self.shell = self.object
        self.player = self.shell.props.shell_player
        self.psc_id = self.player.connect('playing-song-changed', self.song_change)
        self.engine = pyttsx.init()
        self.voices = self.engine.getProperty('voices')
#        self.engine.setProperty('voice', self.voices[3].id)
        self.engine.say("I am alive!")
        self.engine.runAndWait() 

    def do_deactivate(self):
        print "Goodbye World"
        self.engine.endLoop()
        self.engine = None
        self.player = None
        self.voices = None

    def song_change(self, player, entry):
        if entry is None:
            return
        
        artist = entry.get_string(RB.RhythmDBPropType.ARTIST)
        title = entry.get_string(RB.RhythmDBPropType.TITLE)

        print 'new song!'
        
        print '    playing ' + title + ' by ' + artist
        self.engine.stop()
        self.engine.say('Now playing: '+ title + ', by: ' + artist)
        self.engine.runAndWait()
d

