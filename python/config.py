from fireREST import FMC


fmc = FMC(
    hostname="10.1.1.1", 
    username="TEST", 
    password="TEST", 
    domain="Global"
)

fwname = "ftd1"

subint_map = {
    "internal": "GigabitEthernet0/0",
    "core2": "GigabitEthernet0/0",
    "external": "GigabitEthernet0/1",
    "npu2_vlink0": "GigabitEthernet0/1",
    "npu2_vlink1": "GigabitEthernet0/1"
}