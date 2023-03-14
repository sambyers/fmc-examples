from config import fmc, fwname, parent_intf
from utils import print_subints


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
    "ifname": "child3",
    "name": parent_intf,
}

for i in range(1, 10):
    id = f"{i}0"
    subint_template["vlanId"] = id
    subint_template["subIntfId"] = id
    subint_template["ifname"] = f"subInt{i}"
    print(f"Creating subinterface {parent_intf}.{id}...")
    fmc.device.devicerecord.subinterface.create(data=subint_template, container_name=fwname)
subints = fmc.device.devicerecord.subinterface.get(container_name=fwname)
print("Completed:")
print_subints(subints)
