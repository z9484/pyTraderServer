import re
import socket
from sqlite3 import *
import cPickle as pickle
import threading
from character import *
import sys
        
playersLock = threading.Lock()
players = [Character("1"), Character("2")]
# shouldQuit = False

class ConnectionThread (threading.Thread):
    def run(self):
        HOST = ''                 
        PORT = 50007         
        CLIENTS = 5     
        server = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        server.bind ((HOST, PORT))
        server.listen(CLIENTS)

        while 1:
            channel, addr = server.accept()
            ClientThread(channel, addr).start()
            
            

class ClientThread (threading.Thread):
    def __init__(self, channel, addr):
        self.channel = channel
        self.addr = addr
        # self.playerIndex = -1
        threading.Thread.__init__(self)

    def run(self):
        self.db = Server()
        print 'Received connection:', self.addr[0]
        self.startClient()
        while 1:
            packet = self.channel.recv(1024)
            if not packet: break
            # print "Recieving Packet", packet
            self.recieve(packet)            
        self.channel.close()
        print 'Closed connection:', self.addr[0]

    def recieve(self, data):
        cmds = pickle.loads(data)
        for cmd in cmds:
            print cmd
            self.handle(cmd)
        
    def handle(self, cmd):
        print "parsing command:", cmd
        if cmd[0] == 'm':
            playersLock.acquire()
            players[self.playerIndex].posX = cmd[1]
            players[self.playerIndex].posY = cmd[2]
            print "updated player {0}'s coordinates to {1},{2}".format(players[self.playerIndex].name, players[self.playerIndex].posX, players[self.playerIndex].posY)
            playersLock.release()
        elif cmd[0] == 'b':
            print self.db.getBaseData(cmd[1])
        # elif cmd[0] == 's:'
            
            

    def startClient(self):
        auth = pickle.loads(self.channel.recv(1024))
        print auth
        found = False
        for player in xrange(len(players)):
            if auth[0] == players[player].name and auth[1] == players[player].password:
                # print "found"
                playersLock.acquire()
                self.channel.send("1")
                self.channel.send(pickle.dumps(players[player]))
                found = True
                playersLock.release()
                self.playerIndex = player
        
        outpostData = pickle.dumps(self.db.getTable())
        size = pickle.dumps(sys.getsizeof(outpostData))
        self.channel.send(size)

        packet = self.channel.recv(25)
        # print "yes"
        self.channel.send(outpostData)
        
        
        # if found:
            # self.channel.send(pickle.dumps())

        

class Server(object):
    def __init__(self):
        self.conn = connect('data.db')
        self.curs = self.conn.cursor()
        
   

    def create(self):
       
        self.curs.execute('''create table bases
        (id integer primary key, x integer, y integer, type integer, food_cap integer, food_cur integer,
        mineral_cap integer, mineral_cur integer, 
        equip_cap integer, equip_cur integer)''')
        
        self.curs.execute('''insert into bases values
            (NULL,24,9,2,2600,1300,7000,3500,3500,1750)''')
        self.curs.execute('''insert into bases values    
            (NULL,45,45,4,6800,3400,4300,2150,4300,2150)''')
        self.curs.execute('''insert into bases values
            (NULL,47,28,4,7400,3700,4600,2300,4600,2300)''')
        self.curs.execute('''insert into bases values
            (NULL,10,3,2,3300,1650,8800,4400,4400,2200)''')
        self.curs.execute('''insert into bases values   
            (NULL,12,12,1,6400,3200,1600,800,3200,1600)''')
        self.curs.execute('''insert into bases values
            (NULL,25,35,3,3300,1650,6600,3300,8800,4400)''')
        self.curs.execute('''insert into bases values
            (NULL,2,39,1,5000,2500,1300,650,2500,1250)''')
        self.curs.execute('''insert into bases values
            (NULL,14,38,1,8800,4400,2200,1100,4400,2200)''')
        self.curs.execute('''insert into bases values
            (NULL,37,50,3,3200,1600,6300,3150,8400,4200)''')
        self.curs.execute('''insert into bases values
            (NULL,42,22,2,3700,1850,9800,4900,4900,2450)''')
        self.curs.execute('''insert into bases values
            (NULL,7,29,1,9800,4900,2500,1250,4900,2450)''')
        self.curs.execute('''insert into bases values
            (NULL,25,2,3,2700,1350,5400,2700,7200,3600)''')
        self.curs.execute('''insert into bases values
            (NULL,5,22,2,900,450,2400,1200,1200,600)''')
        self.curs.execute('''insert into bases values
            (NULL,38,50,1,2800,1400,700,350,1400,700)''')
        self.curs.execute('''insert into bases values
            (NULL,5,46,3,3500,1750,6900,3450,9200,4600)''')
        self.curs.execute('''insert into bases values
            (NULL,11,33,4,2800,1400,1800,900,1800,900)''')
        self.curs.execute('''insert into bases values
            (NULL,15,7,3,3500,1750,7100,3550,9400,4700)''')
        self.curs.execute('''insert into bases values
            (NULL,42,35,1,9200,4600,2300,1150,4600,2300)''')
        self.curs.execute('''insert into bases values
            (NULL,6,9,1,8200,4100,2100,1050,4100,2050)''')
        self.curs.execute('''insert into bases values
            (NULL,23,17,1,10000,5000,2500,1250,5000,2500)''')
        self.curs.execute('''insert into bases values
            (NULL,41,41,3,3500,1750,6900,3450,9200,4600)''')
        self.curs.execute('''insert into bases values
            (NULL,12,23,3,3500,1750,6900,3450,9200,4600)''')
        self.curs.execute('''insert into bases values
            (NULL,20,13,1,2800,1400,700,350,1400,700)''')
        self.curs.execute('''insert into bases values
            (NULL,10,7,2,3800,1900,10000,5000,5000,2500)''')
        self.curs.execute('''insert into bases values
            (NULL,44,43,2,3400,1700,9000,4500,4500,2250)''')
        self.conn.commit()

    def transaction(self, base, commodity, amt):
        commodity += "_cur"
        self.curs.execute("UPDATE bases SET {0} = {0} + {1} WHERE id={2}".format(commodity, amt, base))
        self.conn.commit()
  
    def displaytable(self):
        self.curs.execute("SELECT * FROM bases")
        for row in self.curs:
            print row

    def getBaseData(self, args):
        tt = ""
        for i in xrange(len(args)):
            tt += " id = " + str(args[i])
            if i < len(args) - 1:
                tt += " OR"
                
        self.curs.execute("SELECT * FROM bases WHERE" + tt)
        return [row for row in self.curs]

    def getTable(self):
        self.curs.execute("SELECT * FROM bases")
        return [row for row in self.curs]

def runServer(self):
    ConnectionThread().start()
    while (True):
        raw = raw_input(">").strip()
        shouldQuit = re.search(r"q|quit|exit", raw, re.I)
        if shouldQuit:
            break
            
if __name__ == "__main__":
    # cc = Server()
    
    # cc.create()
    # cc.displaytable()
    # cc.transaction(1, "food", 5)
    # cc.displaytable()
    # print cc.getBaseData([1, 3, 22])
    # cc.run()
    
    # print cc.getTable()
    
    ConnectionThread().start()
    
    
    
    
    
    
    
    
    
    
    
