

# Make a Python script that logs in to this page:
# http://target1.bowneconsulting.com/protected/A2.3/index.php
# with these parameters:
# Username: admin
# Password: P@ssw0rd
# User-Agent: python

import socket
import base64

# Input
host = 'target1.bowneconsulting.com'
port = 80
url = '/protected/A2.3/index.php'
username = 'admin'
password = 'P@ssw0rd'
agent = 'python'

# Process, output
cred = f"{username}:{password}"
auth = base64.b64encode(cred.encode())
s = socket.socket()
s.settimeout(2)
s.connect((host, port))

# Build request based on requirements above
req = f"""GET {url} HTTP/1.1\r
User-Agent: {agent}\r
Authorization: Basic {auth.decode()}\r
Host: {host}\r
\r
"""
s.send(req.encode())
reply = s.recv(1024).decode()
print(reply)
s.close()

# HTTP/1.1 200 OK
# Date: Wed, 02 Nov 2022 23:40:20 GMT
# Server: Apache/2.4.29 (Ubuntu)
# Content-Length: 19
# Content-Type: text/html; charset=UTF-8
#
#  The flag is basic
