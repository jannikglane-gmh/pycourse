import yaml
from pprint import pprint
from pathlib import Path
from netmiko import ConnectHandler

filepath = f"{Path.home()}/.netmiko.yml"

with open(filepath, "r") as file:
    data = yaml.safe_load(file)

net_connect = ConnectHandler(**data["cisco3"])
output = net_connect.find_prompt()
print(output)
