#!/usr/bin/python2.6
#
import socket
import time

HOST = '127.0.0.1'
PORT = 5038

USER = 'admin'
SECRET = 'efxdsqzeP3'
TRUNK = 'powervoip'

TARGET = 'CELL NUMBER'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

time.sleep(3)

s.send('Action: login\r\n')
s.send('Username: %s\r\n' % USER)
s.send('Secret: %s\r\n\r\n' % SECRET)

time.sleep(3)

s.send('Action: status\r\n')
data = s.recv(1024)

s.send('Events: off\r\n\r\n')

time.sleep(3)

s.send('Action: originate\r\n')
s.send('Channel: Sip/%s/%s\r\n' % (TRUNK, TARGET))
s.send('WaitTime: 10\r\n')
s.send('CallerId: unknown\r\n')
s.send('Application: playback\r\n')
s.send('Data: monkeys\r\n')
s.send('Async: true\r\n')
s.send('Priority: 1\r\n\r\n')

time.sleep(5)

s.send('Action: Logoff\r\n\r\n')
s.close()
