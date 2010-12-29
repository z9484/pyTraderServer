import re
from sqlite3 import *

class Server(object):
    def run(self):
        while (True):
            raw = raw_input(">").strip()
            
            shouldQuit = re.search(r"q|quit|exit", raw, re.I)
            if shouldQuit:
                break

    def create(self):
        conn = connect('data.db')
        curs = conn.cursor()
       
        curs.execute('''create table bases
        (id integer primary key, x integer, y integer,  food_cur integer,
        food_cap integer, mineral_cur integer, mineral_cap integer, 
        equip_cur integer, equip_cap integer)''')
        
        curs.execute('''insert into bases values
            (NULL,24,9,2600,1300,7000,3500,3500,1750)''')
        curs.execute('''insert into bases values    
            (NULL,45,45,6800,3400,4300,2150,4300,2150)''')
        curs.execute('''insert into bases values
            (NULL,47,28,7400,3700,4600,2300,4600,2300)''')
        curs.execute('''insert into bases values
            (NULL,10,3,3300,1650,8800,4400,4400,2200)''')
        curs.execute('''insert into bases values   
            (NULL,12,12,6400,3200,1600,800,3200,1600)''')
        curs.execute('''insert into bases values
            (NULL,25,35,3300,1650,6600,3300,8800,4400)''')
        curs.execute('''insert into bases values
            (NULL,2,39,5000,2500,1300,650,2500,1250)''')
        curs.execute('''insert into bases values
            (NULL,14,38,8800,4400,2200,1100,4400,2200)''')
        curs.execute('''insert into bases values
            (NULL,37,50,3200,1600,6300,3150,8400,4200)''')
        curs.execute('''insert into bases values
            (NULL,42,22,3700,1850,9800,4900,4900,2450)''')
        curs.execute('''insert into bases values
            (NULL,7,29,9800,4900,2500,1250,4900,2450)''')
        curs.execute('''insert into bases values
            (NULL,25,2,2700,1350,5400,2700,7200,3600)''')
        curs.execute('''insert into bases values
            (NULL,5,22,900,450,2400,1200,1200,600)''')
        curs.execute('''insert into bases values
            (NULL,38,50,2800,1400,700,350,1400,700)''')
        curs.execute('''insert into bases values
            (NULL,5,46,3500,1750,6900,3450,9200,4600)''')
        curs.execute('''insert into bases values
            (NULL,11,33,2800,1400,1800,900,1800,900)''')
        curs.execute('''insert into bases values
            (NULL,15,7,3500,1750,7100,3550,9400,4700)''')
        curs.execute('''insert into bases values
            (NULL,42,35,9200,4600,2300,1150,4600,2300)''')
        curs.execute('''insert into bases values
            (NULL,6,9,8200,4100,2100,1050,4100,2050)''')
        curs.execute('''insert into bases values
            (NULL,23,17,10000,5000,2500,1250,5000,2500)''')
        curs.execute('''insert into bases values
            (NULL,41,41,3500,1750,6900,3450,9200,4600)''')
        curs.execute('''insert into bases values
            (NULL,12,23,3500,1750,6900,3450,9200,4600)''')
        curs.execute('''insert into bases values
            (NULL,20,13,2800,1400,700,350,1400,700)''')
        curs.execute('''insert into bases values
            (NULL,10,7,3800,1900,10000,5000,5000,2500)''')
        curs.execute('''insert into bases values
            (NULL,44,43,3400,1700,9000,4500,4500,2250)''')
        conn.commit()

    def query(self):
        conn = connect('data.db')
        curs = conn.cursor()
       
        curs.execute("select * from bases")
        for row in curs:
            print row

if __name__ == "__main__":
    cc = Server()
    # cc.create()
    cc.query()
    