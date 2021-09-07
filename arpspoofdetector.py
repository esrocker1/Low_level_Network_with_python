#!/usr/bin/env python 
from scapy.all import *

ipaddr=[] #list to store known ip addresses
macaddr=[] # list to store known mac addresses

def findARP(p):
 if p.haslayer(ARP): # check whether an ARP packet is present in the packet
  n=len(ipaddr) # loop limit based on number of elements based on 
  known=0
  for i in range(n): # loop 
   if p.psrc==ipaddr[i]: # checking if mentioned ip aleady in the last
    print "ip already in the list"
    known =1
    if p.hwsrc!=macaddr[i]: # if the mac associated with ip is different as compared to our list 
     print "Posioning detected: ",ipaddr[i],"was at",macaddr[i],"and the request is coming from: ",p.hwsrc
  if known==0:
    ipaddr.append(p.psrc) # new ip to be added in the list 
    print "new added",ipaddr
    macaddr.append(p.hwsrc)
    print "new added",macaddr # new mac to be added in the list
   
sniff(prn=findARP) # run sniff, capture packets and run each packet through findARP
