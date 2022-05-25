from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

devices =[{
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    "session_log": "log.txt"
},
{
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    "session_log": "log.txt"
}]

net_connect = ConnectHandler(**devices[1])
result = net_connect.send_command("show version")

f = open("result.txt", "w")
f.write(result)
f.close()
