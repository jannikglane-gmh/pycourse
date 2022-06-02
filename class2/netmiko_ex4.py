import os
from netmiko import ConnectHandler
from getpass import getpass

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

commands = [
    "ip name-server 1.1.1.1",
    "ip name-server 1.0.0.1",
    "ip domain-lookup"
]

output = net_connect.send_config_set(commands)

net_connect.disconnect()
