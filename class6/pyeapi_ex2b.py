import pyeapi
from getpass import getpass
from my_funcs import readFromYaml, printArpData

devices = readFromYaml("device.yaml")

password = getpass()

for key, device in devices.items():
    device["password"] = password
    connection = pyeapi.connect(**device)
    node = pyeapi.client.Node(connection)
    output = node.enable("show ip arp")
    printArpData(output)
