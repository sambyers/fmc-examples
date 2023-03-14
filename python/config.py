from fireREST import FMC


fmc = FMC(
    hostname="10.1.1.1", 
    username="test", 
    password="test", 
    domain="Global"
)

fwname = "ftd1"
parent_intf = "GigabitEthernet0/0"
