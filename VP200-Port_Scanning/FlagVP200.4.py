    
# Connect to the target1.bowneconsulting.com server on port 22020.
# Its banner reveals another port to connect to. The next service reveals a flag

import socket
import re

s = socket.socket()
s.settimeout(1)
port = 22020
s.connect(('target1.bowneconsulting.com', port))
print(f"Testing port {port}")
msg = s.recv(1024).decode()
print(msg)
s.close()
    

num_list = re.findall('\d+', msg)
dedup = [*set(num_list)]
print(f"The parsed port list is {dedup}")
print()
# The parsed port list is ['3', '222', '22253', '22', '2']

for port in dedup:
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect(('target1.bowneconsulting.com', int(port)))
        print(f"Testing port {port}")
        msg = s.recv(1024).decode()
        print(msg)
        s.close()
    except socket.error as err:
        print(f"No response on port {port} - {err}")
# No response on port 3 - timed out
# No response on port 222 - timed out
# Testing port 22253
# Good work!  The flag is string-parsing
# Testing port 22
# SSH-2.0-OpenSSH_7.6p1
# No response on port 2 - timed out