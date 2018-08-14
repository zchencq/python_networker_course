from __future__ import print_function, unicode_literals

ip_addr1 = raw_input("Please enter an IP address:")

print("""
    Octet1         Octet2         Octet3         Octet4     
------------------------------------------------------------
""")
octets = ip_addr1.split(".")
print("{:^15}{:^15}{:^15}{:^15}".format(*octets))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(int(octets[0])), bin(int(octets[1])),bin(int(octets[2])), bin(int(octets[3]))))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(int(octets[0])), hex(int(octets[1])),hex(int(octets[2])), hex(int(octets[3]))))
print("-" * 60)