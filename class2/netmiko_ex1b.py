import os
from netmiko import ConnectHandler
from getpass import getpass

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    #"session_log": "log.txt"
}

net_connect = ConnectHandler(**device)

output = net_connect.send_command("ping", expect_string=r"Protocol", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Target IP", strip_prompt=False, strip_command=False)
output += net_connect.send_command("8.8.8.8", expect_string=r"Repeat count", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Datagram size",strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Timeout in seconds",strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Extended commands",strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Sweep range of sizes",strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"#",strip_prompt=False, strip_command=False)

print(output)