"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/1/2022
https://samsclass.info/124/proj14/VP200.htm
"""


import socket

s = socket.socket()
# Demo Error handling
try:
    s.connect(('nowhere.samsclass.info', 22))
    print(s.recv(1024).decode())
    s.close()
except socket.error as err:
    print(err)
