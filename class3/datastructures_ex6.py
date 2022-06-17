import yaml
from pprint import pprint
from pathlib import Path
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

filepath = f"{Path.home()}/.netmiko.yml"

with open(filepath, "r") as file:
    data = yaml.safe_load(file)

net_connect = ConnectHandler(**data["cisco4"])
output = net_connect.send_command("show run")

config = CiscoConfParse(output.splitlines())

interface_ip_list = []

for interface in config.find_parents_w_child(parentspec=r"^interface", childspec=r"^\s+ip address"):
    ip = config.find_children_w_parents(parentspec=interface, childspec=r"^\s+ip address")
    interface_ip_list.append({"interface": interface, "ips": ip})

for entry in interface_ip_list:
    interface = entry["interface"]
    ips = entry["ips"]
    print(f"Interface Line: {interface}\n"
          f"IP Address Line:", end="")
    for ip in ips:
        print(f"{ip}\n")
