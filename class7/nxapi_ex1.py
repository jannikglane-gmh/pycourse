from nxapi_plumbing import Device
from getpass import getpass

device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    transport="https",
    port=8443,
    username="pyclass",
    password=getpass(),
    verify=False
)

output = device.show("show interface Ethernet1/1")
row_intf = output["TABLE_interface"]["ROW_interface"]
intf = row_intf["interface"]
state = row_intf["state"]
mtu = row_intf["eth_mtu"]
print(f"Interface: {intf}, State: {state}, MTU: {mtu}")