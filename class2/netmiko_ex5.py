import os
from netmiko import ConnectHandler
from getpass import getpass

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    #"session_log": "log.txt"
}
nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    #"session_log": "log.txt"
}

for device in (nxos1, nxos2):

    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_from_file(config_file="config.txt")
    output += net_connect.save_config();
    print(output)
    net_connect.disconnect()
