"""
# Echo client program
import socket

HOST = ''    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('[1]')
data = s.recv(1024)
s.close()
print 'Received', repr(data)
"""

import cPickle as pickle
import socket

HOST = 'localhost'                 
PORT = 50007      
    
client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


size = pickle.loads(client.recv(128))
client.send("1")
print pickle.loads(client.recv(size))

client.send(pickle.dumps([1,3]))

# for x in xrange(10):
   # client.send('Hey. ' + str (x) + '\n')

# client.send("~")

client.close()
