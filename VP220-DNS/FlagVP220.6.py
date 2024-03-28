

# In a Web browser, open this page:
# https://samsclass.info/124/proj14/VP220-6.php
# Monitor the DNS requests. Some of the requests contain the flag, but they are encoded

from scapy.all import *
import sys

def findDNS(p):
    if p.haslayer(DNS):
        msg = p[DNS].summary()
        if 'samsclass.info' in msg:
            # Parse out the server DNS name
            server_name = str(msg).split('"')[1].split('.')[0].split("'")[1]
            # Convert binary to hex
            bin2hex = (hex(int(server_name, 2)))
            # Remove the 0x
            my_str = bin2hex.replace('0x', '')
            # Decode
            decoded = bytes.fromhex(my_str).decode()
            if '-' in decoded:
                print(decoded)
                sys.exit()

print("Listening on DNS traffic for '-'")
sniff(prn=findDNS)

# -8bits-
