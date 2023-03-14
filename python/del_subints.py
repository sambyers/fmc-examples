from config import fmc, fwname


subints = fmc.device.devicerecord.subinterface.get(container_name=fwname)
for subint in subints:
    subint_id = subint["subIntfId"]
    parent_intf = subint["name"]
    print(f"Deleting subinterface {parent_intf}.{subint_id}")
    fmc.device.devicerecord.subinterface.delete(container_name=fwname, uuid=subint["id"])
