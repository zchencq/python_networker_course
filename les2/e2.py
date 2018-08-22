from __future__ import print_function, unicode_literals

my_ip_list = []
my_ip_list.append("1.1.1.1")
my_ip_list.extend(["2.2.2.2", "3.3.3.3"])
print(my_ip_list)
my_ip_list2 = ["4.4.4.4", "5.5.5.5"]
my_ip_list = my_ip_list + my_ip_list2
print(my_ip_list)
print("the first IP address of the list is " + str(my_ip_list[0]))
print("the last IP address of the list is " + str(my_ip_list[4]))