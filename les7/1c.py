'''
Using Jinja2 templating and a for-loop inside the template, generate the following configuration snippet: 

vlan 501
   name blue501
vlan 502
   name blue502
vlan 503
   name blue503
vlan 504
   name blue504
vlan 505
   name blue505
vlan 506
   name blue506
vlan 507
   name blue507
vlan 508
   name blue508

Your template should be inside your Python program for simplicity.

It is fine for your VLAN IDs to be out of order in the generated configuration (for example, VLAN ID 508 can come before VLAN ID 504).

'''
from __future__ import print_function, unicode_literals
import jinja2

vlan_list = [
    {"id": 501, "name": "blue501"},
    {"id": 502, "name": "blue502"},
    {"id": 503, "name": "blue503"},
    {"id": 504, "name": "blue504"},
    {"id": 505, "name": "blue505"},
    {"id": 506, "name": "blue506"},
    {"id": 507, "name": "blue507"},
    {"id": 508, "name": "blue508"}
]


vlan_vars = {
    "vlan_list" : vlan_list
}

vlan_template = '''
{%- for vlan in vlan_list %}
vlan {{ vlan.id }}
   name {{ vlan.name }}
{%- endfor %} 
'''
t = jinja2.Template(vlan_template)
print(t.render(vlan_vars))
