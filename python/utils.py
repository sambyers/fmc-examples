from pyfgtconflib import Parser
from config import subint_map


def print_subints(subints):
    if len(subints) <= 0:
        print("No subinterfaces.")
    for subint in subints:
        name = subint["name"]
        id = subint["subIntfId"]
        print(f"{name}.{id}")

def parse_file(path):
	with open(path) as f:
		conf = Parser()
		conf.parse_text(f)
		return conf.section_dict

def parse_subints(config):
    interfaces_cfg = config["config system interface"]
    result_cfg = []
    for k,v in interfaces_cfg.items():
        interface_cfg = interfaces_cfg[k]
        interface_name = interface_cfg['set interface']
        if isinstance(interface_name, list):
             interface_cfg['set interface'] = interface_name[0].strip('"')
             if interface_cfg['set interface'] in subint_map.keys():
                result_cfg.append(interface_cfg)
    return result_cfg