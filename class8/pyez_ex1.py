from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

srx2 = {
    "host": "srx2.lasthop.io",
    "user": "pyclass",
    "password": getpass()
}

device = Device(**srx2)
device.open()
output = device.facts

pprint(output)
pprint(output["hostname"])