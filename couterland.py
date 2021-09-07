#!/usr/bin/env python
from scapy.all import *

 
def cap12(p):
  conf.L3socket #raw packets 
  conf.L3socket=L3RawSocket #enable raw packets
  if p.haslayer(TCP): #check the presence of TCP packets in p to distinguish it udp 
   if p[IP].src==p[IP].dst: # primary condition of land attacks
    print" Some one tring to land attack check the following netwrok packet information for in depth analysis"
    print p.display()
sniff(prn=cap12) # run sniff and prn tells what function to run on every packet captured
