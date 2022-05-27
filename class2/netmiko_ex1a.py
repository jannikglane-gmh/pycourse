import os
from netmiko import ConnectHandler
from getpass import getpass

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

device ={
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    #"session_log": "log.txt"
}

net_connect = ConnectHandler(**device)

output = net_connect.send_command_timing("ping", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("8.8.8.8", strip_prompt=False, strip_command=False)

for i in range (5):
    output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)

print(output)