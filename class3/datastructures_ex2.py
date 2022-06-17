import yaml

devices =[
    {
    "host": "cisco3.lasthop.io",
    "username": "mupersan",
    "password": "test123",
    "device_type": "cisco_ios",
    },
    {
    "host": "cisco4.lasthop.io",
    "username": "mupersan",
    "password": "test123",
    "device_type": "cisco_ios",
    },
    {
    "host": "nxos1.lasthop.io",
    "username": "mupersan",
    "password": "test123",
    "device_type": "cisco_ios",
    },
    {
    "host": "nxos2.lasthop.io",
    "username": "mupersan",
    "password": "test123",
    "device_type": "cisco_ios",
    }
]

filename = "devices.yml"

with open(filename, "w") as f:
    yaml.dump(devices, f, default_flow_style=False)
