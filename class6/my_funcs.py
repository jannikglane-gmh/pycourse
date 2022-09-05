import yaml

def readFromYaml(fileName):
    with open(fileName, 'r') as file:
        return yaml.safe_load(file)

def printArpData(arp_data):
    ip_mac = []
    for entry in arp_data[0]["result"]["ipV4Neighbors"]:
        ip_mac.append({
            "ip": entry["address"],
            "mac": entry["hwAddress"]
        })

    print(ip_mac)