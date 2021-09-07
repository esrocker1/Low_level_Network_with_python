#!/usr/bin/env python

from scapy.all import *

i=IP()
i.src="10.0.2.15"
i.dst="10.0.2.15"
t=TCP()
t.dport=445
r=sr1(i/t)
t.flags="A"
t.seq=r.ack
t.ack=r.seq+1
send(i/t)
