from __future__ import print_function, unicode_literals

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"
split_mac1 = mac1.split()
split_mac2 = mac2.split()
split_mac3 = mac3.split()
print('''
             IP ADDR          MAC ADDRESS
-------------------- --------------------
''')
print("{:>20}{:>20}".format(split_mac1[1], split_mac1[3]))
print("{:>20}{:>20}".format(split_mac2[1], split_mac2[3]))
print("{:>20}{:>20}".format(split_mac3[1], split_mac3[3]))