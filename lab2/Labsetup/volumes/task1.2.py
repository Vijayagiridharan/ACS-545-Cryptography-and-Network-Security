#!/usr/bin/env python3
# Task 1.2 ----------------------------------------------------
from scapy.all import *
a = IP()
a.dst = '1.2.3.4'
b = ICMP()
p = a/b
send(p)

ls(a)

send(p,iface='br-c4b0abd7cf91')
