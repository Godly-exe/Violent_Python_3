
# In a Web browser, open this page:
# https://samsclass.info/124/proj14/VP220-2.php
# Monitor the DNS requests. After a while you'll find the flag.

from scapy.all import *
import sys

def findDNS(p):
    if p.haslayer(DNS):
        msg = p[DNS].summary()
        if 'flag' in msg:
            print(msg)
            sys.exit()


print("Listening on DNS traffic for 'flag'")
sniff(prn=findDNS)

# DNS Qry "b'dk1ngonqdm-flag-is-poorlyhidden-ak0kjpzezzsdzmjrh2.samsclass.info.'"