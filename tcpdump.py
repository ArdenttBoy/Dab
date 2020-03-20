#!/usr/bin/python


# follow my socials
# ig - blazing_vpn
# backup ip - blazing.backup
# yt - blazing runs

import subprocess, time, sys, os
os.system('clear')
menu = raw_input("""
this is a TCPdump script enjoy ;)
made by @blazing_runs!
so press enter to start: """)
connlimit = raw_input("\x1b[95mARE U SURE? (y/n): ")
if connlimit == "y":
	time.sleep(1)
if connlimit == "n":
	exit()
print("")
time.sleep(1)
print("\x1b[95m script made by blazing for \x1b[95m")
print("\x1b[95m @your_offline because hes  \x1b[95m")
print("\x1b[95m my bitch but fr much love guys \x1b[95m")
print("\x1b[92m --------------------- \x1b[95m")
print("\x1b[92m                       \x1b[95m")
print("\x1b[92m 1) TCPdump to a file          \x1b[95m")
print("\x1b[92m 2) capture trafic to port 22  \x1b[95m")
print("\x1b[92m 3) capture trafic to port 443 \x1b[95m")
print("\x1b[92m 4) capture ICMP trafic        \x1b[95m")
print("\x1b[92m 5) commands to block trafic   \x1b[95m")
print("\x1b[92m 6) exit                       \x1b[95m")
print("\x1b[92m \x1b[95m")

connlimit = raw_input("\x1b[95mplease choose an option 1,2,3,4: ")
if connlimit == "1":
	print("\x1b[92m crl + c to stop the script (the file is called attack.pcap) \x1b[95m")
	print("starting process...")
	time.sleep(2)
	os.system('clear')
	time.sleep(1)
	print("\x1b[92m3\x1b[95m")
	time.sleep(1)
	print("\x1b[95m2\x1b[92m")
	time.sleep(1)
	print("\x1b[92m1\x1b[95m")
	time.sleep(1)
	os.system('tcpdump -i eth0 -c 100000 -w attack.pcap')
if connlimit == "2":
	print("\x1b[92m crl + c to stop the script \x1b[95m")
	print("starting process...")
	time.sleep(2)
	os.system('clear')
	time.sleep(1)
	print("\x1b[92m3\x1b[95m")
	time.sleep(1)
	print("\x1b[95m2\x1b[92m")
	time.sleep(1)
	print("\x1b[92m1\x1b[95m")
	time.sleep(1)
	os.system('tcpdump port 22')
if connlimit == "3":
	print("\x1b[92m crl + c to stop the script \x1b[95m")
	print("starting process...")
	time.sleep(2)
	os.system('clear')
	time.sleep(1)
	print("\x1b[92m3\x1b[95m")
	time.sleep(1)
	print("\x1b[95m2\x1b[92m")
	time.sleep(1)
	print("\x1b[92m1\x1b[95m")
	time.sleep(1)
	os.system('tcpdump port 443')
if connlimit == "4":
	print("\x1b[92m crl + c to stop the script \x1b[95m")
	print("starting process...")
	time.sleep(2)
	os.system('clear')
	time.sleep(1)
	print("\x1b[92m3\x1b[95m")
	time.sleep(1)
	print("\x1b[95m2\x1b[92m")
	time.sleep(1)
	print("\x1b[92m1\x1b[95m")
	time.sleep(1)
	os.system('tcpdump -nni eth0 icmp')
if connlimit == "5":
	print("\x1b[92m iptables -A INPUT -s THEIP -j DROP - block a captured ip\x1b[95m")
	print("\x1b[92m iptables -A INPUT -p udp -m length --length THELENGTH -j DROP - block a length\x1b[95m")
	print("\x1b[92m iptables -A INPUT -m string --algo bm --string "" -j DROP - block string, advanced add string in the  "" \x1b[95m")
	time.sleep(1)
	exit()
if connlimit == "6":
	os.system('clear')
	time.sleep(1)
	exit()