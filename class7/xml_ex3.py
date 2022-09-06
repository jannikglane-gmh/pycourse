import xmltodict

def getDictFromXML(filename):
    with open(filename, "r") as f:
        return xmltodict.parse(f.read())

def getDictFromXMLAndForceList(filename, force_list):
    with open(filename, "r") as f:
        return xmltodict.parse(f.read(), force_list=force_list)

szones = getDictFromXML("show_security_zones.xml")
szones_trust = getDictFromXML("show_security_zones_trust.xml")

# The first one is a list, because the xml has multiple elements with the same tag
print(type(szones['zones-information']['zones-security']))
print(type(szones_trust['zones-information']['zones-security']))

# Ex 3c
force_list = {"zones-security":True}
szones = getDictFromXMLAndForceList("show_security_zones.xml", force_list)
szones_trust = getDictFromXMLAndForceList("show_security_zones_trust.xml", force_list)
print(type(szones['zones-information']['zones-security']))
print(type(szones_trust['zones-information']['zones-security']))
