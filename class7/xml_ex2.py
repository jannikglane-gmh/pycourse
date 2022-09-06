import xmltodict
from pprint import pprint

with open("show_security_zones.xml", "r") as f:
    xml_data = xmltodict.parse(f.read())

print(type(xml_data))
pprint(xml_data)

for index, value in enumerate(xml_data["zones-information"]["zones-security"]):
    name = value["zones-security-zonename"]
    print(f"Security zone {index}: {name}")