"""
Read the contents of the "show_arp.txt" file. Using a for loop, iterate over the lines of this file. Process the lines of the file and separate out the ip_addr and mac_addr for each entry into a separate variable.

Add a conditional statement that searches for '10.220.88.1'. If 10.220.88.1 is found, print out the string "Default gateway IP/Mac" and the corresponding IP address and MAC Address.

Using a conditional statement, also search for '10.220.88.30'. If this IP address is found, then print out "Arista3 IP/Mac is" and the corresponding ip_addr and mac_addr.

Keep track of whether you have found both the Default Gateway and the Arista3 switch. Once you have found both of these devices, 'break' out of the for loop.
"""
from __future__ import print_function, unicode_literals

my_arp_list = []

f = open("/home/zhen/pythoncourse/les3/show_arp.txt")
found_entries = 0

for line in f.readlines(): 
        if line.split()[0] == "Internet":
           ip_addr = line.split()[1]
           mac_addr = line.split()[3]
           arp_entry = (ip_addr, mac_addr)
           my_arp_list.append(arp_entry)
           if ip_addr == "10.220.88.1":
              print("Default gateway IP/Mac: " + ip_addr + "/" + mac_addr)
              found_entries += 1
           elif ip_addr == "10.220.88.30":
              print("Arista3 IP/Mac is: " + ip_addr + "/" + mac_addr)
              found_entries += 1
        if found_entries == 2:
           break 
print(my_arp_list)       
