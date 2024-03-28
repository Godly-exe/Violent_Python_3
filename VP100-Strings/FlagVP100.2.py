"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/1/2022
https://samsclass.info/124/proj14/VP100.htm
"""

# Connect to the ad.samsclass.info server on port 10203.
# It sends you a number. Add one to that number and send it to the server.
# When you do, you will receive a flag, covered by a green box in the image below.

import socket

# Input
url = 'ad.samsclass.info'
port = 10203

# Process, output
s = socket.socket()
s.connect((url, port))
reply = s.recv(1024).decode()
print(f"Got reply: '{reply}'")

# Get number out of string
num = int(reply.split()[-1])
print(f"Response: '{str((num+1))}'")

# send response and get flag
s.send(str((num+1)).encode())
print(s.recv(1024).decode())
s.close()
