import pyeapi
from my_funcs import readFromYaml
from getpass import getpass
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint

devices = readFromYaml("arista_devices.yaml")
password = getpass()

for name, device in devices.items():
    device["password"] = password

    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader(".")
    template = env.get_template("ex4_intf.j2")

    my_vars = {
        "intf_name": device["data"]["intf_name"],
        "intf_ip": device["data"]["intf_ip"],
        "intf_mask": device["data"]["intf_mask"],
    }

    config = template.render(**my_vars).splitlines()

    connection = pyeapi.connect(**device)
    node = pyeapi.client.Node(connection)
    node.config(config)
    output = node.enable("show ip interface brief")
    pprint(output[0]["result"])