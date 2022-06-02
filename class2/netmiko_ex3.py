import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    "global_delay_factor": 2
    #"session_log": "log.txt"
}

net_connect = ConnectHandler(**device)

output1 = net_connect.send_command("show version", use_textfsm=True)

output2 = net_connect.send_command("show lldp neighbors", use_textfsm=True)

print(type(output2))
print(output2[0]['local_interface'])

net_connect.disconnect()
