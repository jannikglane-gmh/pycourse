import textfsm
from pprint import pprint

with open("textfsm_ex5_data.txt", "r") as data:
    with open("textfsm_ex5.template", "r") as template:
        fsm_template = textfsm.TextFSM(template)
        result = fsm_template.ParseText(data.read())

pprint(result)
