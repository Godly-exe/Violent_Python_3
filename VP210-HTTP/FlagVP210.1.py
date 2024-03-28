

# Make a Python script that logs in to this page:
# http://target1.bowneconsulting.com/php/login2.php
# with these parameters:
# Username: dumbo
# Password: dumbo
# User-Agent: python

import socket

# Input
target = 'target1.bowneconsulting.com'
port = 80
url = '/php/login2.php'
username = 'dumbo'
password = 'dumbo'
agent = 'python'

# Process, output
s = socket.socket()
s.settimeout(2)
s.connect((target, port))

# Build request based on requirements above
req = f"""GET {url}?u={username}&p={password} HTTP/1.1\r
Host: {target}\r
Connection: keep-alive\r
Upgrade-Insecure-Requests: 1\r
DNT: 1\r
User-Agent: {agent}\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r
Referer: http://{target}{url}\r
Accept-Language: en-US,en;q=0.9\r
\r
"""
s.send(req.encode())
reply = s.recv(1024).decode()
print(reply)
s.close()

# HTTP/1.1 200 OK
# Date: Wed, 02 Nov 2022 22:13:23 GMT
# Server: Apache/2.4.29 (Ubuntu)
# Vary: Accept-Encoding
# Content-Length: 167
# Keep-Alive: timeout=5, max=100
# Connection: Keep-Alive
# Content-Type: text/html; charset=UTF-8
#
#  <html>
# <head>
# <title>Login Page</title>
# </head>
# <body bgcolor="#cccccc"  style="font-family:Arial">
#
# <h2>Successful login!</h2>The flag is http-post
#
#
# </body>
# </html>

