
#!/usr/bin/env python3
from scapy.all import *
def print_pkt(pkt):
    pkt.show()
   

#pkt = sniff(iface="br-5f4628793ec9", filter='tcp && src host 10.9.0.5 && dst port 23', prn=print_pkt)
pkt = sniff(iface="br-5f4628793ec9", filter='net 128.230.0.0/16', prn=print_pkt)
