from __future__ import print_function, unicode_literals

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
#print(*show_version.split())
split_strings = show_version.split()
print("Is Cisco contained in the model string: " + str('CISCO' in split_strings[1].upper()))
print("Is 881 contained in the model string: " + str('881' in split_strings[1]))
print("Serial number: " + split_strings[2])
print("Model: " + split_strings[1])