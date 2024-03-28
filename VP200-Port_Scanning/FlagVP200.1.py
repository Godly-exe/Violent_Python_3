

# There is another service listening on ad.samsclass.info on a port number ending in 000;
# that is, one of these: 1000, 2000, 3000, etc.
# The service you want has a banner starting with "Congratulations! You found the hidden"
# Hunt for it until you find it. It starts with "Congratulations," as shown below.
# The port number is the flag, covered by a green rectangle in the image below.

import socket


for port in range(1000, 65001, 1000):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect(('ad.samsclass.info', port))
        print(f"Testing port {port}")
        msg = s.recv(1024).decode()
        if msg.startswith('Congratulations'):
            print(f"Found flag ==>'{msg}'")
            break
        s.close()
    except socket.error as err:
        print(f"No response on port {port} - {err}")
# No response on port 1000 - timed out
# No response on port 2000 - timed out
# Testing port 3000
# Found flag ==>'Congratulations!  You found the hidden service on port 3000!'


