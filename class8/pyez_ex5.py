from jnpr.junos import Device
from jnpr_devices import srx2
from lxml import etree
from pprint import pprint
import xmltodict

device = Device(**srx2)
device.open()

print(device.display_xml_rpc("show version", format="text"))

result = device.rpc.get_software_information()
# result_dict = xmltodict.parse(etree.tostring(result).decode())

pprint(result)

print("************************\n")

print(device.display_xml_rpc("show interfaces terse", format="text"))
result = device.rpc.get_interface_information(terse=True)
print(etree.tostring(result, encoding="unicode"))

print("************************\n")

result = device.rpc.get_interface_information(interface_name="fe-0/0/7" ,terse=True, normalize=True)
print(etree.tostring(result, pretty_print=True , encoding="unicode"))
