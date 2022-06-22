import textfsm
from pprint import pprint

with open("textfsm_ex1_data.txt", "r") as data:
    with open("textfsm_ex2.template", "r") as template:
        fsm_template = textfsm.TextFSM(template)
        result = fsm_template.ParseText(data.read())

list = []

for entry in result:
    list.append({
        "DUPLEX": entry[0],
        "PORT_NAME": entry[1],
        "PORT_TYPE": entry[2],
        "SPEED": entry[3],
        "STATUS": entry[4],
        "VLAN": entry[5]
    })

pprint(list)
