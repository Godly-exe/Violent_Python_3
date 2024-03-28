"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/2/2022
https://samsclass.info/124/proj14/VP210.htm
"""

import socket

# Input
target = 'target1.bowneconsulting.com'
port = 80

# Process, output
s = socket.socket()
s.settimeout(2)
s.connect((target, port))
# The HEAD method grabs only the banner, without getting any pages from the server.
req = 'HEAD / HTTP/1.1\r\nHost: ' + target + '\r\n\r\n'
s.send(req.encode())
print(s.recv(1024).decode())
s.close()
# HTTP/1.1 200 OK
# Date: Wed, 02 Nov 2022 20:45:30 GMT
# Server: Apache/2.4.29 (Ubuntu)
# Last-Modified: Mon, 01 Apr 2019 17:03:07 GMT
# ETag: "ca-5857afe9642b4"
# Accept-Ranges: bytes
# Content-Length: 202
# Vary: Accept-Encoding
# Content-Type: text/html
