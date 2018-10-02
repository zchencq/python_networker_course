'''
Using a conditional in a Jinja2 template, generate the following output: 

crypto isakmp policy 10
 encr aes
 authentication pre-share
 group 5
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic

The encryption of aes, and the Diffie-Hellman group should be variables in the template.

Additionally this entire ISAKMP section should only be added 
if the isakmp_enable variable is set to True.

Your template should be inside your Python program for simplicity.

'''
from __future__ import print_function, unicode_literals
import jinja2

isakmp_policy_vars = {
    #True | False
    "isakmp_enable": True,
    "encription_method": "aes",
    "DH_group": 5
}

isakmp_policy_template = '''
{% if isakmp_enable -%}
crypto isakmp policy 10
 encr {{ encription_method }}
 authentication pre-share
 group {{ DH_group }}
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic
{% endif %}
'''

t = jinja2.Template(isakmp_policy_template)
print(t.render(isakmp_policy_vars))