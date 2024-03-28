

# In a Web browser, open this page:
# https://samsclass.info/124/proj14/VP220-5.php
# Monitor the DNS requests. Some of the requests contain the flag, but they are encoded.
# Hints
# https://python-forum.io/Thread-how-to-convert-a-string-to-hex
# https://stackoverflow.com/questions/3283984/decode-hex-string-in-python-3

from scapy.all import *
import sys

def findDNS(p):
    if p.haslayer(DNS):
        msg = p[DNS].summary()
        if 'samsclass.info' in msg:
            server_name = str(msg).split('"')[1].split('.')[0].split("'")[1]
            decoded = bytes.fromhex(server_name).decode()
            if 'flag' in decoded:
                print(decoded)
                sys.exit()

print("Listening on DNS traffic for 'flag'")
sniff(prn=findDNS)

# dv8sj-flag-is-hexcode-UfW6hCZx
