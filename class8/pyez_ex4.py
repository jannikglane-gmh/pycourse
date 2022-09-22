from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr_devices import srx2
from pyez_ex2 import gather_routes
from pprint import pprint

device = Device(**srx2)
device.open()

routes = gather_routes(device)
print("****** ROUTES BEFORE CHANGE ******\n")
pprint(routes.items())

with Config(device) as cfg:
    cfg.lock()
    cfg.load(path="routes.conf", merge=True)
    cfg.commit()
    cfg.unlock()

routes = gather_routes(device)
print("****** ROUTES AFTER CHANGE ******\n")
pprint(routes.items())

## DELETE ROUTES ADDED BEFORE

print("****** DELETE ROUTES ******\n")

with Config(device) as cfg:
    cfg.lock()
    cfg.load(
        "delete routing-options static route 203.0.113.5/32", format="set", merge=True
    )
    cfg.load(
        "delete routing-options static route 203.0.113.200/32", format="set", merge=True
    )
    pprint(cfg.diff())
    cfg.commit()
    cfg.unlock()