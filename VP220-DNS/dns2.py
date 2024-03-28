"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/3/2022
https://samsclass.info/124/proj14/VP220.htm
"""

from scapy.all import *


def findDNS(p):
    if p.haslayer(DNS):
        # Avoid "IndexError: Layer [IP] not found"
        try:
            print(p[IP].src, p[DNS].summary())
        except:
            print(p[DNS].summary())


sniff(prn=findDNS)


# DNS Qry "b'server463.samsclass.info.'"
# DNS Qry "b'server463.samsclass.info.'"
# DNS Ans
# DNS Ans
# DNS Qry "b'server710.samsclass.info.'"
# DNS Qry "b'server710.samsclass.info.'"
# DNS Ans
# DNS Ans
# DNS Qry "b'array809.prod.do.dsp.mp.microsoft.com.'"
# DNS Ans
# DNS Qry "b'server401.samsclass.info.'"
# DNS Qry "b'server401.samsclass.info.'"
# DNS Ans
# DNS Ans
# 100.100.100.100 DNS Ans "[b'rpBA=00:00:00:00:00:00', b'rpVr=360.4', b'rpAD=b7f8161752eb']"
# DNS Ans "[b'rpBA=00:00:00:00:00:00', b'rpVr=360.4', b'rpAD=b7f8161752eb']"
# DNS Qry "b'server969.samsclass.info.'"
# DNS Qry "b'server969.samsclass.info.'"