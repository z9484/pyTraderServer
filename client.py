import cPickle as pickle
import socket
from character import *

HOST = 'localhost'                 
PORT = 50007      
    
client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


size = pickle.loads(client.recv(128))
client.send("1")
print pickle.loads(client.recv(size))
# print pickle.loads(client.recv(1024))
client.send(pickle.dumps(("1","tt")))

packet = client.recv(25) #Succesful authentication
print packet
if packet == "1":
    player = pickle.loads(client.recv(1024))
    print player
    
    client.send(pickle.dumps( (("m", 4,5), ("b", (1,3)) ) ))
    # client.send(pickle.dumps( (("b", (1,3)),) ))

# for x in xrange(10):
   # client.send('Hey. ' + str (x) + '\n')

# client.send("~")

client.close()
raw_input()