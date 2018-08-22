from __future__ import print_function, unicode_literals

banner = '-' * 80

f = open("/home/zhen/pythoncourse/les2/show_version.txt")
show_ver = f.read()

print(banner)
print(show_ver)
print(banner)
print(type(show_ver))
print(banner)
f.close()

with open("/home/zhen/pythoncourse/les2/show_version.txt") as f:
    show_ver = f.readlines()

print("\n" + banner)
print(show_ver)
print(banner)
print(type(show_ver))
print(banner + "\n")