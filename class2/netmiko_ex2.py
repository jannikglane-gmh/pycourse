import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

device = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "global_delay_factor": 2
    #"session_log": "log.txt"
}

net_connect = ConnectHandler(**device)

time_start = datetime.now()
output = net_connect.send_command("show lldp neighbors detail")
time_end = datetime.now()
print(output)
print(f"Time elapsed: {time_end - time_start}")

time_start = datetime.now()
output = net_connect.send_command("show lldp neighbors detail", delay_factor=8)
time_end = datetime.now()
print(output)
print(f"Time elapsed: {time_end - time_start}")
