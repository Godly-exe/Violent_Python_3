"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/1/2022
https://samsclass.info/124/proj14/VP100.htm
"""

# Connect to the ad.samsclass.info server on port 10202.
# Send it the string "Goodbye".
# When you do, you will receive a flag, covered by a green box in the image below

import socket

# Input
url = 'ad.samsclass.info'
port = 10202
msg = 'Goodbye\n'

# Process, output
s = socket.socket()
s.connect((url, port))
print(s.recv(1024).decode())
s.send(msg.encode())
print(s.recv(1024).decode())
s.close()
