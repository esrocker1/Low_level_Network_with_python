#!/usr/bin/env python 
import sys 
from scapy.all import *

def findSYN(p):
 print "Honey pot started, packet received begining deception"
 flags=p.sprintf("%TCP.flags%")
 if flags=="S":              #Cheking for the SYN flag
  print "Detected the SYN flag packt from an attacker"
  incoming_ip=p[IP]          #storing the ip layed information of the incoming packet
  incoming_tcp=p[TCP]        #storing the tcp layed information of the incoming packet
  fool_ip=IP()               # creating an ip packet to send data to the scanner's ip
  fool_ip.dst=incoming_ip.src 
  fool_ip.src=incoming_ip.dst
  fool_tcp=TCP()             # creating a tcp layer packet over ip packet to send to the scanner' ip
  fool_tcp.flags="SA"        #setting the SYN/ACK FLAG on the packets
  fool_tcp.dport=incoming_tcp.sport
  fool_tcp.sport=incoming_tcp.dport
  fool_tcp.ack=incoming_tcp.seq+1 #increasing the sequence number by 1 to complete the TCP handshake
  fool_tcp.seq=incoming_tcp.ack # Since the seq number has to be randomly generated large number it is easy to use the previous ack number
  print "Fooling the nmap by sending SYN/ACK to", fool_ip.dst,":",fool_tcp.dport
  send(fool_ip/fool_tcp)
  
sniff(prn=findSYN) # sniff sniffes on the network for incoming packet and prn tell what function to run on any packet received.
