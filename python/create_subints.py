from config import fmc, fwname, subint_map
from utils import print_subints, parse_file, parse_subints

cfg = parse_file("input.conf")
cfg_subints = parse_subints(cfg)
subint_template = {
    "type": "SubInterface",
    "vlanId": 30,
    "subIntfId": 30,
    "enabled": True,
    "MTU": 1500,
    "priority": 0,
    "pathMonitoring": {
        "enable": False,
    },
    "managementOnly": False,
    "enableAntiSpoofing": True,
    "enableSGTPropagate": True,
    "ifname": "",
    "name": "",
    "ipv4": {
        "static": {
        "address": "1.2.3.4",
        "netmask": "25"
        },
    },
}

for subint in cfg_subints:
    id = subint["set vlanid"][0]
    intf = subint['set interface']
    subint_template["vlanId"] = id
    subint_template["subIntfId"] = id
    subint_template["ifname"] = f"{intf}.{id}"
    ip_addr_mask = subint["set ip"][0].split()
    subint_template["ipv4"]["static"]["address"] = ip_addr_mask[0]
    subint_template["ipv4"]["static"]["netmask"] = ip_addr_mask[1]
    parent_intf = subint_map[intf]
    subint_template["name"] = parent_intf
    print(f"Creating subinterface {parent_intf}.{id}...")
    fmc.device.devicerecord.subinterface.create(data=subint_template, container_name=fwname)
subints = fmc.device.devicerecord.subinterface.get(container_name=fwname)
print("Completed:")
print_subints(subints)
