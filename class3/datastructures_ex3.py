import json
from pprint import pprint

filename = "nxos.json"

with open(filename, "r") as file:
    data = json.load(file)

ipv4_list = []
ipv6_list = []

for interface, ip_dict in data.items():
    for ip_type, ip_addresses_dict in ip_dict.items():
        for ip, prefix_dict in ip_addresses_dict.items():
            if ip_type == "ipv4":
                prefix_lenght = prefix_dict["prefix_length"]
                ipv4_list.append(f"{ip}/{prefix_lenght}")
            if ip_type == "ipv6":
                prefix_lenght = prefix_dict["prefix_length"]
                ipv6_list.append(f"{ip}/{prefix_lenght}")

pprint(ipv4_list)
pprint(ipv6_list)
