from nxapi_plumbing import Device
from getpass import getpass
from lxml import etree

device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    transport="https",
    port=8443,
    username="pyclass",
    password=getpass(),
    verify=False
)

output = device.show("show interface Ethernet1/1")
print(etree.tostring(output).decode())

commands = [
    "show system uptime",
    "show system resources"
]

output = device.show_list(commands)

for result in output:
    print(etree.tostring(result).decode())

commands = [
    "interface Loopback87",
    "description loopback87 interface",
    "interface Loopback88",
    "description loopback88 interface"
]

output = device.config_list(commands)
for result in output:
    print(etree.tostring(result).decode())