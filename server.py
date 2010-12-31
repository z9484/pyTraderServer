import re
import socket
from sqlite3 import *
import cPickle as pickle
import threading


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
        threading.Thread.__init__(self)

    def run(self):
        self.db = Server()
        print 'Received connection:', self.addr[0]
        self.startClient()
        while 1:
            packet = self.channel.recv(1024)
            if not packet: break
            # print "Recieving Packet", packet
            self.handle(packet)            
        self.channel.close()
        print 'Closed connection:', self.addr[0]

    def handle(self, data):
        d = pickle.loads(data)
        print self.db.getBaseData(d)
        
    def startClient(self):
        outpostData = pickle.dumps(self.db.getTable())
        import sys
        size = pickle.dumps(sys.getsizeof(outpostData))
        
        self.channel.send(size)
        packet = self.channel.recv(25)
        print "yes"
        self.channel.send(outpostData)
        

class Server(object):
    def __init__(self):
        self.conn = connect('data.db')
        self.curs = self.conn.cursor()
        
    def run(self):
        
        while (True):
            raw = raw_input(">").strip()
            
            shouldQuit = re.search(r"q|quit|exit", raw, re.I)
            if shouldQuit:
                break

    def create(self):
       
        self.curs.execute('''create table bases
        (id integer primary key, x integer, y integer, food_cap integer, food_cur integer,
        mineral_cap integer, mineral_cur integer, 
        equip_cap integer, equip_cur integer)''')
        
        self.curs.execute('''insert into bases values
            (NULL,24,9,2600,1300,7000,3500,3500,1750)''')
        self.curs.execute('''insert into bases values    
            (NULL,45,45,6800,3400,4300,2150,4300,2150)''')
        self.curs.execute('''insert into bases values
            (NULL,47,28,7400,3700,4600,2300,4600,2300)''')
        self.curs.execute('''insert into bases values
            (NULL,10,3,3300,1650,8800,4400,4400,2200)''')
        self.curs.execute('''insert into bases values   
            (NULL,12,12,6400,3200,1600,800,3200,1600)''')
        self.curs.execute('''insert into bases values
            (NULL,25,35,3300,1650,6600,3300,8800,4400)''')
        self.curs.execute('''insert into bases values
            (NULL,2,39,5000,2500,1300,650,2500,1250)''')
        self.curs.execute('''insert into bases values
            (NULL,14,38,8800,4400,2200,1100,4400,2200)''')
        self.curs.execute('''insert into bases values
            (NULL,37,50,3200,1600,6300,3150,8400,4200)''')
        self.curs.execute('''insert into bases values
            (NULL,42,22,3700,1850,9800,4900,4900,2450)''')
        self.curs.execute('''insert into bases values
            (NULL,7,29,9800,4900,2500,1250,4900,2450)''')
        self.curs.execute('''insert into bases values
            (NULL,25,2,2700,1350,5400,2700,7200,3600)''')
        self.curs.execute('''insert into bases values
            (NULL,5,22,900,450,2400,1200,1200,600)''')
        self.curs.execute('''insert into bases values
            (NULL,38,50,2800,1400,700,350,1400,700)''')
        self.curs.execute('''insert into bases values
            (NULL,5,46,3500,1750,6900,3450,9200,4600)''')
        self.curs.execute('''insert into bases values
            (NULL,11,33,2800,1400,1800,900,1800,900)''')
        self.curs.execute('''insert into bases values
            (NULL,15,7,3500,1750,7100,3550,9400,4700)''')
        self.curs.execute('''insert into bases values
            (NULL,42,35,9200,4600,2300,1150,4600,2300)''')
        self.curs.execute('''insert into bases values
            (NULL,6,9,8200,4100,2100,1050,4100,2050)''')
        self.curs.execute('''insert into bases values
            (NULL,23,17,10000,5000,2500,1250,5000,2500)''')
        self.curs.execute('''insert into bases values
            (NULL,41,41,3500,1750,6900,3450,9200,4600)''')
        self.curs.execute('''insert into bases values
            (NULL,12,23,3500,1750,6900,3450,9200,4600)''')
        self.curs.execute('''insert into bases values
            (NULL,20,13,2800,1400,700,350,1400,700)''')
        self.curs.execute('''insert into bases values
            (NULL,10,7,3800,1900,10000,5000,5000,2500)''')
        self.curs.execute('''insert into bases values
            (NULL,44,43,3400,1700,9000,4500,4500,2250)''')
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

        
if __name__ == "__main__":
    cc = Server()
    
    # cc.create()
    # cc.displaytable()
    # cc.transaction(1, "food", 5)
    # cc.displaytable()
    # print cc.getBaseData([1, 3, 22])
    # cc.run()
    ConnectionThread().start()
    # print cc.getTable()
    
    
    
    
    
    
    
    
    
    
    
    
