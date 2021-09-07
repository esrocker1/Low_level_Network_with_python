#several penetesters after gaining access to the network try and create false router advertisements to trick your pc/laptop to connect to it.
#this is simple script checks for the router advertisements (RA) which or IPv6 nature and alerts the user.


#!/usr/bin/env python
from scapy.all import *  # importing everything fromt the scapy module.

def capIPV6(p): 
 if p.haslayer(IPv6): # simply check if the packet has IPv6 components which seems unlikely inside a network.
  print "-------------------------ALERT----------------------------------"
  print "New ipv6 advertisement from; ",p[IPv6].lladdr
  print"_____Check whether such a device exists or not___________________"
sniff(prn=capIPV6) # sniffes the packets and prn tells what function to run on every packet.
