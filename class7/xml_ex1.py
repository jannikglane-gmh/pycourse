from lxml import etree

with open("show_security_zones.xml", "r") as data:
    result = data.read()
    xml_data = etree.fromstring(result)

# Ex 1a
print(xml_data)
print(type(xml_data))

# Ex 1b
print(etree.tostring(xml_data).decode())

# Ex 1c
print(xml_data.tag)
print(len(list(xml_data)))

# Ex 1d
print(xml_data[0].tag)
print(xml_data.getchildren()[0].tag)

# Ex 1e
trust_zone = xml_data[0]
print(trust_zone.find("zones-security-zonename").text)

# Ex 1f
for child in trust_zone:
    print(child.tag)