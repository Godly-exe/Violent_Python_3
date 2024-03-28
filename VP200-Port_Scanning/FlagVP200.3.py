

# Connect to the target1.bowneconsulting.com server on port 22010.
# Its banner reveals another port to connect to. The next service reveals a flag

import socket

s = socket.socket()
s.settimeout(1)
port = 22010
s.connect(('target1.bowneconsulting.com', port))
print(f"Testing port {port}")
msg = s.recv(1024).decode()
print(msg)
s.close()

next_port = int(msg.split()[7])
s = socket.socket()
s.settimeout(1)
port = 22010
s.connect(('target1.bowneconsulting.com', next_port))
print(f"Testing port {next_port}")
msg = s.recv(1024).decode()
print(msg)
s.close()
# Testing port 22275
# Good work!  The flag is knock-knock
