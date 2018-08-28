from __future__ import print_function, unicode_literals

f = open("/home/zhen/pythoncourse/les3/show_lldp_neighbors_detail.txt")
my_sys_name = ""
my_port_id = ""
found_num = 0
for line in f.readlines():
    if "System Name" in line:
        my_sys_name = line.split(": ")[1]
        found_num += 1
    if "Port id" in line:
        my_port_id = line.split(": ")[1] 
        found_num += 1
    if found_num == 2:
       break
print("Port ID is: " + my_port_id)
print("System Name is: " + my_sys_name)