import pyeapi
from getpass import getpass
from pprint import pprint

connection = pyeapi.client.connect(
    transport="https",
    host="arista3.lasthop.io",
    port="443",
    username="pyclass",
    password=getpass()
)

node = pyeapi.client.Node(connection)

output = node.enable("show ip arp")

ip_mac = []

for entry in output[0]["result"]["ipV4Neighbors"]:
    ip_mac.append({
        "ip": entry["address"],
        "mac": entry["hwAddress"]
    })

pprint(ip_mac)