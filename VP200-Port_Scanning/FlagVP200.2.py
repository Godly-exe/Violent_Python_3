

# Find a service running on the target1.bowneconsulting.com server on a port between 21000 and 21030.
# Its banner reveals a flag.

import socket

for port in range(21000, 21031):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect(('target1.bowneconsulting.com', port))
        print(f"Testing port {port}")
        msg = s.recv(1024).decode()
        print(msg)
        s.close()
        break
    except socket.error as err:
        print(f"No response on port {port} - {err}")

# No response on port 21000 - timed out
# No response on port 21001 - timed out
# No response on port 21002 - timed out
# No response on port 21003 - timed out
# No response on port 21004 - timed out
# No response on port 21005 - timed out
# No response on port 21006 - timed out
# No response on port 21007 - timed out
# No response on port 21008 - timed out
# No response on port 21009 - timed out
# No response on port 21010 - timed out
# Testing port 21011
# Good!  The flag is banner-grabbing