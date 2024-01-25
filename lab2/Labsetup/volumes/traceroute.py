#!/usr/bin/env python3
from scapy.all import *

a = IP()
a.dst =sys.argv[1]

a.ttl=1

while True:
       b=ICMP()
       p=a/b
       resp =sr1(p, timeout =2, verbose =0)
       
       if resp is None:
            print("Reply is none")
       elif resp[ICMP].type ==0:
            print(resp[IP].src, "are %d hops away from" % (a.ttl))
            print("Finally_Reached", resp[IP].src)
            break
       else:
            print(resp[IP].src, "are %d hops away from" % (a.ttl))
       a.ttl +=1
