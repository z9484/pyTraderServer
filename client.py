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

client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 50007))

print pickle.loads(client.recv(1024))

for x in xrange(10):
   client.send('Hey. ' + str (x) + '\n')

for x in xrange(1000000):
    1 + 1
    
client.send("~")

client.close()
