#!/usr/bin/env python3
from scapy.all import *
def print_pkt(pkt):
    pkt.show()
   
print("Jello")
pkt = sniff(iface="br-5f4628793ec9", filter="icmp", prn=print_pkt)

