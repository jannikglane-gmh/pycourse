from lxml import etree

with open("show_security_zones.xml", "r") as f:
    xml_data = etree.fromstring(f.read())

# EX 4A
print("Find tag of the first zones-security element")
print("".join("-"*20))
zones_security = xml_data.find("zones-security")
print(zones_security.tag)

print("\n\n\nFind tag of the all children of zones-security element")
print("".join("-"*20))
children = zones_security.getchildren()
for child in children:
    print(child.tag)

# EX 4B
zonename = zones_security.find("zones-security-zonename")
print(f"\n\nTag: {zonename.tag} Text: {zonename.text}\n\n")

# EX 4C
all_zones = xml_data.findall("zones-security")
for zone in all_zones:
    zonename = zone.find("zones-security-zonename")
    print(f"Tag: {zonename.tag} Text: {zonename.text}")
