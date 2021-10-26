#connect to our router via SSH using module Netmiko

from netmiko import ConnectHandler

router_mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host':   '103.54.222.93',
    'username': 'api',
    'password': 'password',
    'use_keys' : True,
    'key_file' : '/Users/mankomalsingh/.ssh/id_rsa',
    'port' : 22          # optional, defaults to 22
    #'secret': 'secret',     # optional, defaults to ''
}

net_connect = ConnectHandler(**router_mikrotik)
commands =['/interface print',
           '/ip address print']

for commands in commands:
    output = net_connect.send_command(commands, cmd_verify=True)
    print(output)
    print(type(output))
