"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/1/2022
https://samsclass.info/124/proj14/VP200.htm
"""


import socket

# Create a socket object named "s"
s = socket.socket()
# Set the socket timeout in seconds
s.settimeout(2)
# Connect to the server "ad.samsclass.info" on port 80
s.connect(('ad.samsclass.info', 80))
#  Receive and print banner to the console
print(s.recv(1024).decode())
s.close()

