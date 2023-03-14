from config import fmc, fwname
from utils import print_subints


subints = fmc.device.devicerecord.subinterface.get(container_name=fwname)
print(f"Current subinterfaces on {fwname}:")
print_subints(subints)
