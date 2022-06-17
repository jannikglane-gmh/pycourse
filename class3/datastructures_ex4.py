import json
from pprint import pprint

filename = "arp.json"

with open(filename, "r") as file:
    data = json.load(file)

ips = {}

for ip_neighbor in data["ipV4Neighbors"]:
    ips[ip_neighbor["address"]] = ip_neighbor["hwAddress"]

pprint(ips)
