from ciscoconfparse import CiscoConfParse
from pprint import pprint

bgp_config = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""

ip_remote_list = []

conf = CiscoConfParse(bgp_config.splitlines())

bgp_list = []

for neighbor in conf.find_children_w_parents(parentspec=r"router bgp", childspec=r"neighbor"):
    for remote_as in conf.find_children_w_parents(parentspec=neighbor, childspec="remote-as"):
        bgp_list.append((neighbor.split()[1], remote_as.split()[1]))

pprint(bgp_list)