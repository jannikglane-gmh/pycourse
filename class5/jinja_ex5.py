from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from netmiko import ConnectHandler
from my_devices import cisco3
from pprint import pprint

filename = "jinja_ex5.j2"
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")
template = env.get_template(filename)

my_vars = {
    "ntp_servers": [
        "130.126.24.24",
        "152.2.21.1"
    ],
    "timezone": "PST",
    "timezone_offset": "-8",
    "timezone_dst": "PDT",
}

output = template.render(**my_vars)
print(output)