from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable
from jnpr_devices import srx2
from pprint import pprint

def check_connected(device):
    return device.connected

def gather_routes(device):
    return RouteTable(device).get()

def gather_arp_table(device):
    return ArpTable(device).get()

def print_output(output):
    pprint(output)

if __name__ == "main":
    device = Device(**srx2)
    device.open()

    print_output(check_connected(device))
    print_output(gather_routes(device).items())
    print_output(gather_arp_table(device).items())
