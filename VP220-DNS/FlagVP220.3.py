
# In a Web browser, open this page:
# https://samsclass.info/124/proj14/VP220-3.php
# Monitor the DNS requests. Some of the requests are different from the others, and they contain the flag

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

# DNS Qry "b'ruska9s7w2xflagxisxalsohiddenxqq88rqfnzbc1jrmgeprr5qyon.samsclass.info.'"
