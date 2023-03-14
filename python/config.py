from fireREST import FMC


fmc = FMC(
    hostname="10.1.1.1", 
    username="TEST", 
    password="TEST", 
    domain="Global"
)

fwname = "ftd1"
parent_intf = "GigabitEthernet0/0"

subint_map = {
    "internal": "GigabitEthernet0/0",
    "external": "GigabitEthernet0/1",
}