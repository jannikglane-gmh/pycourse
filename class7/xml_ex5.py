from lxml import etree

with open("show_version.xml", "rb") as f:
    xml_data = etree.fromstring(f.read())

print(xml_data.nsmap)

id = xml_data.find(".//{*}proc_board_id")
print(id.tag)