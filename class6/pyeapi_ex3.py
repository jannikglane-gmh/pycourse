import pyeapi
from getpass import getpass
from my_funcs import readFromYaml
from pprint import pprint

device = readFromYaml("device.yaml")["arista4"]
device["password"] = getpass()

connection = pyeapi.connect(**device)
node = pyeapi.client.Node(connection)
output = node.enable("show ip route")
routes = output[0]["result"]["vrfs"]["default"]["routes"]

for ip, route_dict in routes.items():
    print(f"Route: {ip}")
    if route_dict["routeType"] == "static":
        print(f'Next hop address: {route_dict["vias"][0]["nexthopAddr"]}')
