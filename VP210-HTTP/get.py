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

# Get request from wireshark
req = '''GET /php/login1.php?u=a&p=b HTTP/1.1\r
Host: target1.bowneconsulting.com\r
Connection: keep-alive\r
Upgrade-Insecure-Requests: 1\r
DNT: 1\r
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r
Referer: http://target1.bowneconsulting.com/php/login1.php\r
Accept-Language: en-US,en;q=0.9\r
\r
'''
s.send(req.encode())
print(s.recv(1024).decode())
s.close()

# HTTP/1.1 200 OK
# Date: Wed, 02 Nov 2022 22:06:46 GMT
# Server: Apache/2.4.29 (Ubuntu)
# Vary: Accept-Encoding
# Content-Length: 490
# Keep-Alive: timeout=5, max=100
# Connection: Keep-Alive
# Content-Type: text/html; charset=UTF-8
#
# <html>
# <head>
# <title>Login Page</title>
# </head>
# <body bgcolor="#cccccc"  style="font-family:Arial">
#
# <h2>Login Rejected!</h2>You sent: <b>a b</b><h2>Welcome!</h2><blockquote><table border=5 cellpadding=10>
#        <tr><td align='center'><form method='GET'>
#        <h2>Please Log In</h2>
#        Username: <input type='text' name='u'><p>
#        Password: <input type='text' name='p'><p>
#        <input type='submit' value='LOG IN'>
#        </form></td></tr></table></blockquote>
#
# </body>
# </html>

