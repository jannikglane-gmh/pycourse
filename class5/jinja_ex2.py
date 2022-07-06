from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from netmiko import ConnectHandler
import my_devices

filename = "jinja_ex2.j2"
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")
template = env.get_template(filename)

vars_nxos1 = {
    "interface": "Ethernet1/1",
    "ip_address": "10.1.100.1",
    "netmask": "24",
    "local_as": "22",
    "remote_as": "22",
    "peer_ip": "10.1.100.2"
}
vars_nxos2 = {
    "interface": "Ethernet1/1",
    "ip_address": "10.1.100.2",
    "netmask": "24",
    "local_as": "22",
    "remote_as": "22",
    "peer_ip": "10.1.100.1"
}

### NXOS1
result_nxos1 = template.render(**vars_nxos1).splitlines()
result_nxos1 = list(map(str.strip, result_nxos1))

net_connect = ConnectHandler(**my_devices.nxos1)
output = net_connect.send_config_set(result_nxos1)

### NXOS2
result_nxos2 = template.render(**vars_nxos2).splitlines()
result_nxos2 = list(map(str.strip, result_nxos2))

net_connect = ConnectHandler(**my_devices.nxos2)
output += net_connect.send_config_set(result_nxos2)

print(output)
