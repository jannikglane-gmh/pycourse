from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint

filename = "jinja_ex3.j2"
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")
template = env.get_template(filename)

my_vars = {
    "vrf_name": "blue",
    "rd_number": "100:1",
    "ipv4_enabled": True,
    "ipv6_enabled": True
}

output = template.render(**my_vars)
print(output)