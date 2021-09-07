#Do not use for malicious purposes and do not interfere with somebody's privacy. Meant for education purposes only
# below is script to capture packets from a specific computer on a network and see the traffic and the websites visited by that computer.


#!/usr/bin/env python

from scapy.all import *  #import everything from scapy
def findDNS(p):
 if p.haslayer(DNS): #check whether the given packet has a DNS packet or not 
   if p[IP].src == "10.0.2.5" or p[IP].dst=="10.0.2.5" :  #enter the target's ip
   
    print p[IP].dst  
    print p[IP].src,p[DNS].summary() #print the packet summary
   
sniff(prn=findDNS) # run sniff ,capture the packe and run the function findDNS on every packets
