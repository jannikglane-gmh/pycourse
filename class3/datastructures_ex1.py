from pprint import pprint

arp_data = """
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""
arp_data = arp_data.splitlines()
arp_list = []

for entry in arp_data:
    arp_list.append(entry.split())

arp_list = list(filter(None, arp_list))
arp_list.pop(0)

dict_list = []
for entry in arp_list:
   _prot, _address, _age, _mac, _type, _int = entry
   dict_list.append({"mac_addr": _mac, "ip_addr": _address, "interface": _int})
   pprint(dict_list)
