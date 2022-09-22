from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr_devices import srx2

def lock_configuration(cfg):
    try:
        cfg.lock()
        print("configuration locked")
    except:
        print("configuration already locked")

device = Device(**srx2)
device.open()

cfg = Config(device)
lock_configuration(cfg)
lock_configuration(cfg)

cfg.load("set system host-name python4life", format="set", merge=True)
print(cfg.diff())

input()

cfg.rollback(0)
print(cfg.diff())
