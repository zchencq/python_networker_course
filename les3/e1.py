"""
Read the "show_vlan.txt" file into your program. Loop through the lines in this file and extract
all of the VLAN_ID, VLAN_NAME combinations. From these VLAN_ID and VLAN_NAME construct a new list
where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). Print this data
structure to the screen. Your output should look as follows:
[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
"""
from __future__ import print_function, unicode_literals

my_vlan_list = []
f = open("/home/zhen/pythoncourse/les3/show_vlan.txt")
i = 0
while i <= 7:
    line = f.readline().split()
    i += 1
    if line[0] == "VLAN" or line[0] == "-----" or line[0] == "Et6,":
       continue
    print(line)
    tuple = (line[0], line[1])
    my_vlan_list.append(tuple)

print(my_vlan_list)
    