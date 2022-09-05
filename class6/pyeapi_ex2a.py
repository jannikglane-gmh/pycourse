import pyeapi
from getpass import getpass
import yaml

with open('device.yaml', 'r') as file:
    devices = yaml.safe_load(file)

device = devices["arista4"]
device["password"] = getpass()

connection = pyeapi.connect(**device)
node = pyeapi.client.Node(connection)
output = node.enable("show ip arp")

ip_mac = []
for entry in output[0]["result"]["ipV4Neighbors"]:
    ip_mac.append({
        "ip": entry["address"],
        "mac": entry["hwAddress"]
    })

print(ip_mac)