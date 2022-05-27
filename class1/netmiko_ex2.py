from netmiko import ConnectHandler
from getpass import getpass

devices =[{
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
    "session_log": "log.txt"
},
{
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
    "session_log": "log.txt"
}]

for device in devices:
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
